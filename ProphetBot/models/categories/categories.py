import sqlalchemy as sa

from marshmallow import Schema, post_load, fields
from sqlalchemy import Column, Integer, String

from ProphetBot.models import metadata
from ProphetBot.models.db_tables.base import metadata

class CompendiumObject:
    def __init__(self, key: str, obj: object, table: sa.Table, schema: Schema) -> None:
        self.key = key
        self. obj = obj
        self.table = table
        self.schema = schema


class Rarity(object):
    c_rarity_table = sa.Table(
        "c_rarity",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False),
        Column("abbreviation", sa.ARRAY(String), nullable=True),
        Column("seek_dc", Integer, nullable=False)
    )

    class RaritySchema(Schema):
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



class BlacksmithType(object):
    c_blacksmith_type_table = sa.Table(
        "c_blacksmith_type",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class BlacksmithTypeSchema(Schema):
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

class ConsumableType(object):
    c_consumable_type_table = sa.Table(
        "c_consumable_type",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class ConsumableTypeSchema(Schema):
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

class MagicSchool(object):
    c_magic_school_table = sa.Table(
        "c_magic_school",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class MagicSchoolSchema(Schema):
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

class CharacterClass(object):
    c_character_class_table = sa.Table(
        "c_character_class",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class CharacterClassSchema(Schema):
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

class CharacterSubclass(object):
    c_character_subclass_table = sa.Table(
        "c_character_subclass",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("parent", Integer, nullable=False),  # ref: > c_character_class.id
        Column("value", String, nullable=False)
    )

    class CharacterSubclassSchema(Schema):
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

class CharacterRace(object):
    c_character_race_table = sa.Table(
        "c_character_race",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("value", String, nullable=False)
    )

    class CharacterRaceSchema(Schema):
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

class CharacterSubrace(object):
    c_character_subrace_table = sa.Table(
        "c_character_subrace",
        metadata,
        Column("id", Integer, primary_key=True, autoincrement='auto'),
        Column("parent", Integer, nullable=False),  # ref: > c_character_race.id
        Column("value", String, nullable=False)
    )

    class CharacterSubraceSchema(Schema):
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

    


CATEGORY_LIST = [
    CompendiumObject("c_rarity", Rarity, Rarity.c_rarity_table, Rarity.RaritySchema),
    CompendiumObject("c_blacksmith_type", BlacksmithType, BlacksmithType.c_blacksmith_type_table, BlacksmithType.BlacksmithTypeSchema),
    CompendiumObject("c_consumable_type", ConsumableType, ConsumableType.c_consumable_type_table, ConsumableType.ConsumableTypeSchema),
    CompendiumObject("c_magic_school", MagicSchool, MagicSchool.c_magic_school_table, MagicSchool.MagicSchoolSchema),
    CompendiumObject("c_character_class", CharacterClass, CharacterClass.c_character_class_table, CharacterClass.CharacterClassSchema),
    CompendiumObject("c_character_subclass", CharacterSubclass, CharacterSubclass.c_character_subclass_table, CharacterSubclass.CharacterSubclassSchema),
    CompendiumObject("c_character_race", CharacterRace, CharacterRace.c_character_race_table, CharacterRace.CharacterRaceSchema),
    CompendiumObject("c_character_subrace", CharacterSubrace, CharacterSubrace.c_character_subrace_table, CharacterSubrace.CharacterSubraceSchema)
]