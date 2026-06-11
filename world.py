from collections.abc import Mapping
from typing import Any

# Imports of base Archipelago modules must be absolute.
from . import locations, regions
from worlds.AutoWorld import World

# Imports of your world's files must be relative.
from . import items, rules, web_world
from . import options as game_options  # rename due to a name conflict with World.options

class HenryStickminWorld(World):
    """
    The classic newground choose-your-own-adventure where failing is more fun than succeeding.
    """


    # You must override the "game" field to say the name of the game.
    game = "The Henry Stickmin Collection"

    # The WebWorld is a definition class that governs how this world will be displayed on the website.
    web = web_world.HenryStickminWebWorld()

    # This is how we associate the options defined in our options.py with our world.
    # (Note: options.py has been imported as "apquest_options" at the top of this file to avoid a name conflict)
    options_dataclass = game_options.HenryStickminOptions
    options: game_options.HenryStickminOptions  # Common mistake: This has to be a colon (:), not an equals sign (=).

    # Our world class must have a static location_name_to_id and item_name_to_id defined.
    # We define these in regions.py and items.py respectively, so we just set them here.
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "chapterSelect"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    # Our world class must also have a create_item function that can create any one of our items by name at any time.
    def create_item(self, name: str) -> items.HenryStickminItem:
        return items.create_item_with_correct_classification(self, name)

    # For features such as item links and panic-method start inventory, AP may ask your world to create extra filler.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return self.options.as_dict(
            "BtB", "EtP","Goal","Required_Ranks"
        )
