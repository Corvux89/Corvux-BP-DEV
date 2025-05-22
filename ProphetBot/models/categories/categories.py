import sqlalchemy as sa

from marshmallow import Schema, post_load, fields
from sqlalchemy import Column, Integer, String, Numeric, BOOLEAN

from ProphetBot.models import metadata
from ProphetBot.models.db_tables.base import metadata

class CompendiumObject:
    __key__: str
    __table__: sa.Table
    __Schema__: Schema



class Rarity(CompendiumObject):
    __key__ = "c_rarity"

    __table__ = sa.Table(
        "c_rarity",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False),
        Column("abbreviation", sa.ARRAY(String), nullable=True),
        Column("seek_dc", Integer, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)
        abbreviation = fields.List(fields.String, data_key="abbreviation", required=True)
        seek_dc = fields.Integer(data_key="seek_dc", required=True)

        @post_load
        def make_c_rarity(self, data, **kwargs):
            return Rarity(**data)

    def __init__(self, id, value, abbreviation, seek_dc):
        """
        :param id: int
        :param value: str
        :param abbreviation: List[str]
        """

        self.id = id
        self.value = value
        self.abbreviation = abbreviation
        self.seek_dc = seek_dc



class BlacksmithType(CompendiumObject):
    __key__ = "c_blacksmith_type"

    __table__ = sa.Table(
        "c_blacksmith_type",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_blacksmith_type(self, data, **kwargs):
            return BlacksmithType(**data)

    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value

class ConsumableType(CompendiumObject):
    __key__ = "c_consumable_type"

    __table__ = sa.Table(
        "c_consumable_type",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_consumable_type(self, data, **kwargs):
            return ConsumableType(**data)

    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value

class MagicSchool(CompendiumObject):
    __key__ = "c_magic_school"

    __table__ = sa.Table(
        "c_magic_school",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_magic_school(self, data, **kwargs):
            return MagicSchool(**data)

    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value 

class CharacterClass(CompendiumObject):
    __key__ = "c_character_class"

    __table__ = sa.Table(
        "c_character_class",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_character_class(self, data, **kwargs):
            return CharacterClass(**data)

    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value

class CharacterSubclass(CompendiumObject):
    __key__ = "c_character_subclass"

    __table__ = sa.Table(
        "c_character_subclass",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("parent", Integer, nullable=False),  # ref: > c_character_class.id
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        parent = fields.Integer(data_key="parent", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_character_subclass(self, data, **kwargs):
            return CharacterSubclass(**data)

    def __init__(self, id, parent, value):
        """
        :param id: int
        :param parent: int
        :param value: str
        """

        self.id = id
        self.parent = parent
        self.value = value

class CharacterRace(CompendiumObject):
    __key__ = "c_character_race"

    __table__ = sa.Table(
        "c_character_race",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_character_race(self, data, **kwargs):
            return CharacterRace(**data)

    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value

class CharacterSubrace(CompendiumObject):
    __key__ = "c_character_subrace"

    __table__ = sa.Table(
        "c_character_subrace",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("parent", Integer, nullable=False),  # ref: > c_character_race.id
        Column("value", String, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        parent = fields.Integer(data_key="parent", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_character_subrace(self, data, **kwargs):
            return CharacterSubrace(**data)

    def __init__(self, id, parent, value):
        """
        :param id: int
        :param parent: int
        :param value: str
        """

        self.id = id
        self.parent = parent
        self.value = value

class GlobalModifier(CompendiumObject):
    __key__ = "c_global_modifier"

    __table__ = sa.Table(
        "c_global_modifier",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False),
        Column("adjustment", Numeric(precision=5, scale=2), nullable=False),
        Column("max", Integer, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)
        adjustment = fields.Float(data_key="adjustment", required=True)
        max = fields.Integer(data_key="max", required=True)

        @post_load
        def make_c_global_modifier(self, data, **kwargs):
            return GlobalModifier(**data)

    def __init__(self, id, value, adjustment, max):
        """
        :param id: int
        :param value: str
        :param adjustment: float
        :param max: int
        """

        self.id = id
        self.value = value
        self.adjustment = adjustment
        self.max = max

class HostStatus(CompendiumObject):
    __key__ = "c_host_status"

    __table__ = sa.Table(
        "c_host_status",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class HostStatusSchema(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)

        @post_load
        def make_c_host_status(self, data, **kwargs):
            return HostStatus(**data)

    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value

class ArenaTier(CompendiumObject):
    __key__ = "c_arena_tier"

    __table__ = sa.Table(
        "c_arena_tier",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("avg_level", Integer, nullable=False),
        Column("max_phases", Integer, nullable=False)
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        avg_level = fields.Integer(data_key="avg_level", required=True)
        max_phases = fields.Integer(data_key="max_phases", required=True)

        @post_load
        def make_c_arena_tier(self, data, **kwargs):
            return ArenaTier(**data)


    def __init__(self, id, avg_level, max_phases):
        """
        :param id: int
        :param avg_level: int
        :param max_phases: int
        """

        self.id = id
        self.avg_level = avg_level
        self.max_phases = max_phases

class AdventureTier(CompendiumObject):
    __key__ = "c_adventure_tier"

    __table__ = sa.Table(
        "c_adventure_tier",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("avg_level", Integer, nullable=False),
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        avg_level = fields.Integer(data_key="avg_level", required=True)

        @post_load
        def make_c_adventure_tier(self, data, **kwargs):
            return AdventureTier(**data)

    def __init__(self, id, avg_level):
        """
        :param id: int
        :param avg_level: int
        """

        self.id = id
        self.avg_level = avg_level

class ShopType(object):
    __key__ = "c_shop_type"

    __table__ = sa.Table(
        "c_shop_type",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False),
        Column("synonyms", sa.ARRAY(String), nullable=True, default=[]),
        Column("tools", sa.ARRAY(String), nullable=True, default=[])
    )

    class __Schema__(Schema):
        id = fields.Integer(data_key="id", required=True)
        value = fields.String(data_key="value", required=True)
        synonyms = fields.List(fields.String, data_key="synonyms", required=False, default=[])
        tools = fields.List(fields.String, data_key="tools", required=False, default=[])

        @post_load
        def make_c_shop_type(self, data, **kwargs):
            return ShopType(**data)

    def __init__(self, id, value, synonyms, tools):
        """
        :param id: int
        :param value: str
        :param synonyms: List[str]
        :param tools: List[str]
        """

        self.id = id
        self.value = value
        self.synonyms = synonyms
        self.tools = tools


CATEGORY_LIST = [
    Rarity,
    BlacksmithType,
    ConsumableType,
    MagicSchool,
    CharacterClass,
    CharacterSubclass,
    CharacterRace,
    CharacterSubrace,
    GlobalModifier,
    HostStatus,
    ArenaTier,
    AdventureTier,
    ShopType,
]