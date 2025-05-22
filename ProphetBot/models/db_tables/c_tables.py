import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, Numeric, BOOLEAN, BigInteger
from ProphetBot.models.db_tables.base import metadata

















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

