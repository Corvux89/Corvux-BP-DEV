import logging
from timeit import default_timer as timer

from ProphetBot.models.categories.categories import CATEGORY_LIST, CompendiumObject
from ProphetBot.models.db_objects.item_objects import ItemBlacksmith, ItemWondrous, ItemConsumable, ItemScroll
from ProphetBot.models.objects.exceptions import ActivityNotFound, ObjectNotFound
from ProphetBot.models.schemas.category_schema import *
from ProphetBot.models.schemas.item_schema import ItemBlacksmithSchema, ItemWondrousSchema, ItemConsumableSchema, \
    ItemScrollSchema
from ProphetBot.queries import get_blacksmith_items, get_wondrous_items, get_consumable_items, get_scroll_items
from ProphetBot.queries.category_queries import *

log = logging.getLogger(__name__)


async def get_table_values(conn, comp: CompendiumObject) -> list:
    d1, d2 = {}, {}

    async for row in conn.execute(comp.table.select()):
        val = comp.schema().load(row)

        d1[val.id] = val
        attr_list = [
            "value",
            "avg_level",
            "name",
        ]
        key = next(
            (getattr(val, attr) for attr in attr_list if hasattr(val, attr)), None
        )

        if key is not None:
            d2[key] = val

    return [d1, d2]


class Compendium:

    # noinspection PyTypeHints
    def __init__(self):

        """
        Structure will generally be:
        self.attribute[0] = dict(object.id) = object
        self.attribute[1] = dict(object.value) = object

        This can help ensure o(1) for lookups on id/value. o(n) for any filtering
        """

        self.categories = CATEGORY_LIST

        for category in self.categories:
            setattr(self, category.key, [])

    async def reload_categories(self, bot):
        if not hasattr(bot, "db"):
            return
        
        start = timer()

        async with bot.db.acquire() as conn:
            for category in self.categories:
                setattr(self, category.key, await get_table_values(conn, category))

       
        end = timer()
        log.info(f'COMPENDIUM: Categories reloaded in [ {end - start:.2f} ]s')
        bot.dispatch("compendium_loaded")

    async def load_items(self, bot):
        if not hasattr(bot, "db"):
            return
        else:
            start = timer()
            async with bot.db.acquire() as conn:
                self.blacksmith = await get_table_values(conn, get_blacksmith_items(), ItemBlacksmith,
                                                         ItemBlacksmithSchema(self))
                self.wondrous = await get_table_values(conn, get_wondrous_items(), ItemWondrous,
                                                       ItemWondrousSchema(self))
                self.consumable = await get_table_values(conn, get_consumable_items(), ItemConsumable,
                                                         ItemConsumableSchema(self))
                self.scroll = await get_table_values(conn, get_scroll_items(), ItemScroll,
                                                     ItemScrollSchema(self))

            end = timer()
            log.info(f"COMPENDIUM: Items reloaded in [ {end - start:.2f} ]s")
            bot.dispatch("items_loaded")

    def get_object(self, cls, value: str | int = None):
        """
        Retrieve an object from the compendium based on the provided class and value.
        Args:
            cls: The class type of the object to retrieve.
            value (str | int, optional): The value to search for. Can be a string or an integer. Defaults to None.
        Returns:
            The object that matches the provided class and value, or None if no match is found.
        Raises:
            ObjectNotFound: If the object is not found in the compendium.
        """
        try:
            for category in self.categories:
                if category.obj == cls:
                    for cat_value in getattr(self, category.key)[
                        0 if isinstance(value, int) else 1
                    ]:
                        if isinstance(cat_value, str) and isinstance(value, str):
                            if cat_value.lower() == value.lower():
                                return getattr(self, category.key)[
                                    0 if isinstance(value, int) else 1
                                ][cat_value]
                        elif cat_value == value:
                            return getattr(self, category.key)[
                                0 if isinstance(value, int) else 1
                            ][cat_value]

                    # Approximate match for strings
                    for cat_value in getattr(self, category.key)[
                        0 if isinstance(value, int) else 1
                    ]:
                        if isinstance(cat_value, str) and isinstance(value, str):
                            if cat_value.lower().startswith(value.lower()):
                                return getattr(self, category.key)[
                                    0 if isinstance(value, int) else 1
                                ][cat_value]
        except:
            raise ObjectNotFound()
        return None

    def get_activity(self, activity: str | int = None):
        """
        Retrieve an activity by its name or ID.
        Args:
            activity (str | int, optional): The name or ID of the activity to retrieve.
                                            If not provided, defaults to None.
        Returns:
            Activity: The activity object if found.
        Raises:
            ActivityNotFound: If the activity is not found.
        """
        if act := self.get_object(Activity, activity):
            return act

        raise ActivityNotFound(activity)
