import discord.utils
from discord import ApplicationContext, Role


class Rarity(object):
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
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class ConsumableType(object):
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class MagicSchool(object):
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class CharacterClass(object):
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class CharacterSubclass(object):
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
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class CharacterSubrace(object):
    def __init__(self, id, parent, value):
        """
        :param id: int
        :param parent: int
        :param value: str
        """

        self.id = id
        self.parent = parent
        self.value = value


class GlobalModifier(object):
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


class HostStatus(object):
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class ArenaTier(object):
    def __init__(self, id, avg_level, max_phases):
        """
        :param id: int
        :param avg_level: int
        :param max_phases: int
        """

        self.id = id
        self.avg_level = avg_level
        self.max_phases = max_phases


class AdventureTier(object):
    def __init__(self, id, avg_level):
        """
        :param id: int
        :param avg_level: int
        """

        self.id = id
        self.avg_level = avg_level


class ShopType(object):
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


class Activity(object):
    def __init__(self, id, value, ratio, diversion):
        """
        :param id: int
        :param value: str
        :param ratio: float
        :param diversion: bool
        """

        self.id = id
        self.value = value
        self.ratio = ratio
        self.diversion = diversion


class Faction(object):
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value

    def get_faction_role(self, ctx: ApplicationContext) -> Role:
        return discord.utils.get(ctx.guild.roles, name=self.value)


class DashboardType(object):
    def __init__(self, id, value):
        """
        :param id: int
        :param value: str
        """

        self.id = id
        self.value = value


class LevelCaps(object):
    def __init__(self, id, max_gold, max_xp):
        """
        :param id: int
        :param max_gold: int
        :param max_xp: int
        """

        self.id = id
        self.max_gold = max_gold
        self.max_xp = max_xp


class AdventureRewards(object):
    def __init__(self, id, ep, tier, rarity = None):
        """
        :param id: int
        :param ep: int
        :param tier: int
        :param rarity: int
        """

        self.id = id
        self.ep = ep
        self.tier = tier
        self.rarity = rarity


class ShopTier(object):
    def __init__(self, id, rarity):
        """
        :param id: int
        :param rarity: int
        """

        self.id = id
        self.rarity = rarity
