from datetime import datetime
from ProphetBot.models.db import arenas_table
from sqlalchemy import null
from sqlalchemy.sql.selectable import FromClause, TableClause


def select_active_arena_by_channel(channel_id: int) -> FromClause:
    return arenas_table.select().where(
        (arenas_table.c.channel_id == channel_id)
        and
        (arenas_table.c.end_ts is null or datetime.utcnow() < arenas_table.c.end_ts)
    )


def insert_new_arena(channel_id: int, role_id: int, host_id: int) -> TableClause:
    return arenas_table.insert().values(
        channel_id=channel_id,
        role_id=role_id,
        host_id=host_id
    )


def update_arena_tier(arena_id: int, new_tier: int):
    return arenas_table.update()\
        .where(arenas_table.c.id == arena_id)\
        .values(tier=new_tier)


def update_arena_completed_phases(arena_id: int, completed_phases: int):
    return arenas_table.update() \
        .where(arenas_table.c.id == arena_id) \
        .values(tier=completed_phases)


def close_arena_by_id(arena_id: int):
    return arenas_table.update() \
        .where(arenas_table.c.id == arena_id) \
        .values(end_ts=datetime.utcnow())
