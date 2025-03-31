import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Numeric, BOOLEAN, BigInteger
from ProphetBot.models.db_tables.base import metadata








c_global_modifier_table = sa.Table(
    "c_global_modifier",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("value", String, nullable=False),
    Column("adjustment", Numeric(precision=5, scale=2), nullable=False),
    Column("max", Integer, nullable=False)
)

c_host_status_table = sa.Table(
    "c_host_status",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("value", String, nullable=False)
)

c_arena_tier_table = sa.Table(
    "c_arena_tier",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("avg_level", Integer, nullable=False),
    Column("max_phases", Integer, nullable=False)
)

c_adventure_tier_table = sa.Table(
    "c_adventure_tier",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("avg_level", Integer, nullable=False),
)

c_shop_type_table = sa.Table(
    "c_shop_type",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("value", String, nullable=False),
    Column("synonyms", sa.ARRAY(String), nullable=True, default=[]),
    Column("tools", sa.ARRAY(String), nullable=True, default=[])
)

c_activity_table = sa.Table(
    "c_activity",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("value", String, nullable=False),
    Column("ratio", Numeric(precision=5, scale=2), nullable=True),
    Column("diversion", BOOLEAN, nullable=False)
)

c_faction_table = sa.Table(
    "c_faction",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("value", String, nullable=False),
)

c_dashboard_type_table = sa.Table(
    "c_dashboard_type",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement='auto'),
    Column("value", String, nullable=False),
)

c_level_caps_table = sa.Table(
    "c_level_caps",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("max_gold", Integer, nullable=False),
    Column("max_xp", Integer, nullable=False)
)


c_adventure_rewards_table = sa.Table(
    "c_adventure_rewards",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("ep", Integer, nullable=False),
    Column("tier", Integer, nullable=False),
    Column("rarity", Integer, nullable=True)  # ref: > c_rarity.id
)

c_shop_tier_table = sa.Table(
    "c_shop_tier",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("rarity", Integer, nullable=False),  # ref: > c_rarity.id
)

