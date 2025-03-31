import asyncio
import logging
from signal import SIGINT, SIGTERM
import traceback
from typing import Optional, Union
import aiopg.sa
import discord
from aiopg.sa import create_engine, Engine, result
from discord.ext import commands
from timeit import default_timer as timer
from sqlalchemy.schema import CreateTable
from ProphetBot.compendium import Compendium
from ProphetBot.constants import DB_URL
from ProphetBot.helpers.character_helpers import get_character
from ProphetBot.helpers.entity_helpers import get_or_create_guild
from ProphetBot.models.db_objects.entity_objects import PlayerGuild, PlayerCharacter
from ProphetBot.models.db_tables import *
from ProphetBot.models.embeds import ErrorEmbed
from ProphetBot.models.objects.enums import QueryResultType
from ProphetBot.models.objects.exceptions import BPCommandError, BPError
from sqlalchemy.sql import FromClause, TableClause

log = logging.getLogger(__name__)


async def create_tables(conn: aiopg.sa.SAConnection):
    for table in metadata.sorted_tables:
        await conn.execute(CreateTable(table, if_not_exists=True))


class BPContext(discord.ApplicationContext):
    bot: "BpBot"

    def __init__(self, **kwargs):
        super(BPContext).__init__(**kwargs)
        self.player: PlayerCharacter = None
        self.playerGuild: PlayerGuild


class BpBot(commands.Bot):
    db: aiopg.sa.Engine
    compendium: Compendium
    player_guilds: dict = {}

    # Extending/overriding discord.ext.commands.Bot
    def __init__(self, **options):
        super(BpBot, self).__init__(**options)
        self.compendium = Compendium()

    async def on_ready(self):
        start = timer()
        self.db = await create_engine(DB_URL)
        self.dispatch("db_connected")
        end = timer()

        log.info(f"Time to create db engine: {end - start}")

        async with self.db.acquire() as conn:
            await create_tables(conn)

        log.info(f"Logged in as {self.user} (ID: {self.user.id})")
        log.info("------")

    async def close(self):
        log.info("Shutting down bot")
        
        if hasattr(self, "db"):
            self.db.close()
            await self.db.wait_closed()

        await super().close()

    def run(self, *args, **kwargs):
        for sig in (SIGINT, SIGTERM):
            try:
                self.loop.add_signal_handler(
                    sig, lambda: asyncio.create_task(self.close())
                )
            except (NotImplementedError, RuntimeError):
                pass
        super().run(*args, **kwargs)

    async def before_invoke_setup(self, ctx: commands.Context):
        ctx: BPContext = ctx

        ctx.player = await get_character(self, ctx.author.id, ctx.guild.id if ctx.guild else None)

        ctx.playerGuild = await get_or_create_guild(self.db, ctx.guild.id if ctx.guilld else None)

        params = "".join(
            [
                f" [{p['name']}: {p['value']}]"
                for p in (
                    ctx.selected_options
                    if hasattr(ctx, "selected_options") and ctx.selected_options
                    else []
                )
            ]
        )

        try:
            log.info(
                f"cmd: chan {ctx.channel} [{ctx.channel.id}], serv: {f'{ctx.guild.name} [{ctx.guild.id}]' if ctx.guild.id else 'DM'}, "
                f"auth: {ctx.author} [{ctx.author.id}]: {ctx.command}  {params}"
            )
        except AttributeError as e:
            log.info(
                f"Command in DM with {ctx.author} [{ctx.author.id}]: {ctx.command} {params}"
            )

    async def bot_check(self, ctx: Union(discord.ApplicationContext, commands.Context)):
        if (hasattr(self, "db") and self.db and hasattr(self, "compendium") and self.compendium):
            return True
        
        if isinstance(ctx, commands.Context):
            raise BPCommandError("Try again in a few seconds. I'm not fully awake yet.")
        
        raise BPError("Try again in a few seconds. I'm not fully awake yet.")
    
    async def error_handling(
            self, ctx: Union(discord.ApplicationContext|discord.Context), error):
        
        try:
            await ctx.defer()
            await ctx.delete()
        except:
            pass

        if isinstance(error, commands.CommandNotFound) and isinstance(ctx, commands.Context):
            if hasattr(ctx.command, "on_error") or isinstance(error, commands.CommandNotFound) or "Unknown interaction" in str(error):
                return
        elif isinstance(error, Union(BPError, discord.CheckFailure, BPCommandError, commands.CheckFailure)):
            return await ctx.send(embed=ErrorEmbed(error))
        

        if hasattr(ctx, "bot") and hasattr(ctx.bot, "db"):
            params = (
                "".join(
                    [
                        f" [{p['name']}: {p['value']}]"
                        for p in (ctx.selected_options or [])
                    ]
                )
                if hasattr(ctx, "selected_options") and ctx.selected_options
                else ""
            )
        
        out_str = (
                f"Error in command: cmd: chan {ctx.channel} [{ctx.channel.id}], {f'serv: {ctx.guild} [{ctx.guild.id}]' if ctx.guild else ''} auth: {ctx.author} [{ctx.author.id}]: {ctx.command} {params}\n```"
                f"{''.join(traceback.format_exception(type(error), error, error.__traceback__))}"
                f"```"
            )
        
        log.error(out_str)

    async def query(
            self,
            query: Union(FromClause | TableClause),
            result_type: QueryResultType = QueryResultType.single,
    ) -> Optional(result.RowProxy | list[result.RowProxy]):
        async with self.db.acquire() as conn:
            results = await conn.execute(query)

        if result_type == QueryResultType.single:
            return await results.first()
        elif result_type == QueryResultType.multiple:
            return await results.fetchall()
        elif result_type == QueryResultType.scalar:
            return await results.scalar()
        
        return None
