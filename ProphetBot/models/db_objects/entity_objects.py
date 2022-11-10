import math
from typing import List
import discord
from ProphetBot.models.db_objects.category_objects import *


class PlayerCharacterClass(object):
    character_id: int
    primary_class: CharacterClass
    subclass: CharacterSubclass
    active: bool

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_formatted_class(self):
        if self.subclass is not None:
            return f"{self.subclass.value} {self.primary_class.value}"
        else:
            return f"{self.primary_class.value}"


class PlayerCharacter(object):
    # Attributes based on queries: total_level, div_gold, max_gold, div_xp, max_xp, l1_arena, l2_arena, l1_rp, l2_rp
    player_id: int
    guild_id: int
    name: str
    race: CharacterRace
    subrace: CharacterSubrace
    xp: int
    div_xp: int
    gold: int
    div_gold: int
    active: bool
    faction: Faction
    reroll: bool

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_level(self):
        level = math.ceil((self.xp + 1) / 1000)
        return level if level <= 20 else 20

    def get_member(self, ctx: ApplicationContext) -> discord.Member:
        return discord.utils.get(ctx.guild.members, id=self.player_id)

    def mention(self) -> str:
        return f"<@{self.player_id}>"

    def get_formatted_race(self):
        if self.subrace is not None:
            return f"{self.subrace.value} {self.race.value}"
        else:
            return f"{self.race.value}"


class PlayerGuild(object):
    id: int
    max_level: int
    server_xp: int
    weeks: int
    week_xp: int
    max_reroll: int

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_reset_day(self):
        if hasattr(self, "reset_day"):
            weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
            return weekDays[self.reset_day]


class Adventure(object):
    name: str
    role_id: int
    dms: List[int]
    tier: AdventureTier
    category_channel_id: int
    ep: int

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_adventure_role(self, ctx: ApplicationContext) -> Role:
        return discord.utils.get(ctx.guild.roles, id=self.role_id)


class DBLog(object):
    author: int
    xp: int
    server_xp: int
    gold: int
    character_id: int
    activity: Activity
    notes: str
    shop_id: int | None
    adventure_id: int | None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_author(self, ctx: ApplicationContext) -> discord.Member:
        return discord.utils.get(ctx.guild.members, id=self.author)


class Arena(object):
    channel_id: int
    role_id: int
    host_id: int
    tier: ArenaTier
    completed_phases: int

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_role(self, ctx: ApplicationContext | discord.Interaction) -> Role:
        return discord.utils.get(ctx.guild.roles, id=self.role_id)

    def get_host(self, ctx: ApplicationContext | discord.Interaction) -> discord.Member:
        return discord.utils.get(ctx.guild.members, id=self.host_id)
