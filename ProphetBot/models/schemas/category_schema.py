from marshmallow import Schema, fields, post_load

from ProphetBot.models.db_objects.category_objects import *




class ActivitySchema(Schema):
    id = fields.Integer(data_key="id", required=True)
    value = fields.String(data_key="value", required=True)
    ratio = fields.Float(data_key="ratio", required=False, allow_none=True)
    diversion = fields.Boolean(data_key="diversion", required=True)

    @post_load
    def make_c_activity(self, data, **kwargs):
        return Activity(**data)


class FactionSchema(Schema):
    id = fields.Integer(data_key="id", required=True)
    value = fields.String(data_key="value", required=True)

    @post_load
    def make_c_faction(self, data, **kwargs):
        return Faction(**data)


class DashboardTypeSchema(Schema):
    id = fields.Integer(data_key="id", required=True)
    value = fields.String(data_key="value", required=True)

    @post_load
    def make_c_dashboard_type(self, data, **kwargs):
        return DashboardType(**data)


class LevelCapsSchema(Schema):
    id = fields.Integer(data_key="id", required=True)
    max_gold = fields.Integer(data_key="max_gold", required=True)
    max_xp = fields.Integer(data_key="max_xp", required=True)

    @post_load
    def make_level_caps(self, data, **kwargs):
        return LevelCaps(**data)


class AdventureRewardsSchema(Schema):
    id = fields.Integer(data_key="id", required=True)
    ep = fields.Integer(data_key="ep", required=True)
    tier = fields.Integer(data_key="tier", required=True)
    rarity = fields.Integer(data_key="rarity", required=False, allow_none=True)

    @post_load
    def make_adventure_reward(self, data, **kwargs):
        return AdventureRewards(**data)


class ShopTierSchema(Schema):
    id = fields.Integer(data_key="id", required=True)
    rarity = fields.Integer(data_key="rarity", required=True)

    @post_load
    def make_shop_tier(self, data, **kwargs):
        return ShopTier(**data)
