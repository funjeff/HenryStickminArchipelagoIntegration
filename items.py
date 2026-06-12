from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from .henryHelpers import *

if TYPE_CHECKING:
    from .world import HenryStickminWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.
ITEM_NAME_TO_ID = {
    "Shovel": 1,
    "Explosives": 2,
    "Teleporter": 3,
    "Laser": 4,
    "Wrecking Ball": 5,
    "Money Bag Disguise": 6,
    "File": 7,
    "Nrg Drink": 8,
    "Rocket Launcher": 9,
    "Cellphone": 10,
    "Drill": 11,
    "Belt of Grenades": 12,
    "Chair": 13,
    "Rope Launcher": 14,
    "Parachute": 15,
    "Plungers": 16,
    "JetPack": 17,
    "Opacitator": 18,
    "Crowbar": 19,
    "Attorney's Badge": 20,
    "Floor Plans of Bank": 21,
    "Security Footage": 22,
    "Doctor's Analysis": 23,
    "Breaking The Bank": 24,
    "Escaping The Prison": 25,
    "Distraction": 26,
    "Obscure Refrence": 27,
    "Completing The Mission": 28,
    "Fleeing The Complex": 29,
    "Infiltraiting The Airship":30,
    "Stealing The Diamond": 31,
    "Shield": 32,
    "Lance": 33,
    "Flail": 34,
    "Tow Cable": 35,
    "Basket": 36,
    "Rock": 37,
    "Branch": 38,
    "Sticky Grenade": 39,
    "Bubble": 40,
    "Tunisian Diamond": 41,
    "Jumble Hoppers": 42,
    "StDAntiGravityCapFail": 43,
    "Shrink Ray": 44,
    "Pick": 45,
    "Liquidificator": 46,
    "Penny": 47,
    "Tranquilizer": 48,
    "Falcon Punch": 49,
    "Invisibility Pill": 50,
    "Wire": 51,
    "Wormhole Rifle": 52,
    "Laser Cutter": 53,
    "Hammer": 54,
    "Cannon": 55,
    "Plank": 56,
    "Cheese": 57,
    "Rifle": 58,
    "WW2 Gun": 59,
    "WW2 Bomb": 60,
    "WW2 Plane": 61,
    "Metroid": 62,
    "Goodball": 63,
    "Mushroom": 64, #thats awesome that that worked out like that
    "Division By Zero": 65,
    "Nuclear Bomb": 66,
    "Shoop da Whoop": 67,
    "Giant CCC Robot": 68,
    "Useless Device": 69,
    "Really Stupid Idea":70,
    "Poorly Thought Out Plan":71,
    "Part 66 of my Henry Stickmin Playthrough":72

        
}

ID_TO_ITEM_NAME = {v: k for k, v in ITEM_NAME_TO_ID.items()}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Shovel": ItemClassification.progression,
    "Explosives": ItemClassification.progression,
    "Teleporter": ItemClassification.progression,
    "Laser": ItemClassification.progression,
    "Wrecking Ball": ItemClassification.progression,
    "Money Bag Disguise": ItemClassification.progression,
    "File": ItemClassification.progression,
    "Nrg Drink": ItemClassification.progression,
    "Rocket Launcher": ItemClassification.progression,
    "Cellphone": ItemClassification.progression,
    "Drill": ItemClassification.progression,
    "Belt of Grenades": ItemClassification.progression,
    "Chair": ItemClassification.progression,
    "Rope Launcher": ItemClassification.progression,
    "Parachute": ItemClassification.progression,
    "Plungers": ItemClassification.progression,
    "JetPack": ItemClassification.progression,
    "Opacitator": ItemClassification.progression,
    "Crowbar": ItemClassification.progression,
    "Attorney's Badge": ItemClassification.useful,
    "Floor Plans of Bank": ItemClassification.useful,
    "Security Footage": ItemClassification.useful,
    "Doctor's Analysis": ItemClassification.useful,
    "Breaking The Bank": ItemClassification.progression,
    "Escaping The Prison": ItemClassification.progression,
    "Distraction": ItemClassification.filler,
    "Obscure Refrence": ItemClassification.filler,
    "Completing The Mission": ItemClassification.progression,
    "Fleeing The Complex": ItemClassification.progression,
    "Infiltraiting The Airship":ItemClassification.progression,
    "Stealing The Diamond": ItemClassification.progression,
    "Shield": ItemClassification.progression,
    "Lance": ItemClassification.progression,
    "Flail": ItemClassification.progression,
    "Tow Cable": ItemClassification.progression,
    "Basket": ItemClassification.progression,
    "Rock": ItemClassification.progression,
    "Branch": ItemClassification.progression,
    "Sticky Grenade": ItemClassification.progression,
    "Bubble": ItemClassification.progression,
    "Tunisian Diamond": ItemClassification.progression,
    "Jumble Hoppers": ItemClassification.progression,
    "Anti-Gravity Cap": ItemClassification.progression,
    "Shrink Ray": ItemClassification.progression,
    "Pick": ItemClassification.progression,
    "Liquidificator": ItemClassification.progression,
    "Penny": ItemClassification.progression,
    "Tranquilizer": ItemClassification.progression,
    "Falcon Punch": ItemClassification.progression,
    "Invisibility Pill": ItemClassification.progression,
    "Wire": ItemClassification.progression,
    "Wormhole Rifle": ItemClassification.progression,
    "Laser Cutter": ItemClassification.progression,
    "Hammer": ItemClassification.progression,
    "Cannon": ItemClassification.progression,
    "Plank": ItemClassification.progression,
    "Cheese": ItemClassification.progression,
    "Rifle": ItemClassification.progression,
    "WW2 Gun": ItemClassification.progression,
    "WW2 Bomb": ItemClassification.progression,
    "WW2 Plane": ItemClassification.progression,
    "Metroid": ItemClassification.progression,
    "Goodball": ItemClassification.progression,
    "Mushroom": ItemClassification.progression, #thats awesome that that worked out like that
    "Division By Zero": ItemClassification.progression,
    "Nuclear Bomb": ItemClassification.progression,
    "Shoop da Whoop": ItemClassification.progression,
    "Giant CCC Robot": ItemClassification.progression,
    "Useless Device": ItemClassification.filler,
    "Really Stupid Idea": ItemClassification.filler,
    "Poorly Thought Out Plan":ItemClassification.filler,
    "Part 66 of my Henry Stickmin Playthrough":ItemClassification.filler,
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class HenryStickminItem(Item):
    game = "Henry Stickmin"


def get_random_filler_item_name(world: HenryStickminWorld) -> str:
    
    fillNum = world.random.randint(0,6)
    match fillNum:
        case 0:
            return "Distraction"
        case 1:
            return "Obscure Refrence"
        case 2:
            return "Useless Device"
        case 3:
            return "Really Stupid Idea"
        case 4:
            return "Poorly Thought Out Plan"
        case 5:
            return "Part 66 of my Henry Stickmin Playthrough"
    


def create_item_with_correct_classification(world: HenryStickminWorld, name: str) -> HenryStickminItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return HenryStickminItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: HenryStickminWorld) -> None:

    itempool: list[Item] = []
    if use_BtB(world):
        itempool.append(world.create_item("Shovel"))
        itempool.append(world.create_item("Explosives"))
        itempool.append(world.create_item("Laser"))
        itempool.append(world.create_item("Wrecking Ball"))
        btb_item = world.create_item("Breaking The Bank")
        if world.options.BtB == 1:
            world.push_precollected(btb_item)


    if use_BtB(world) or use_EtP(world):
        itempool.append(world.create_item("Money Bag Disguise"))
        

    if use_BtB(world) or use_EtP(world) or use_StD(world):
        teleporter_item = world.create_item("Teleporter") 
        if world.options.Teleporter_Start == 1:
            world.push_precollected(teleporter_item)

    if use_EtP(world):
        itempool.append(world.create_item("File"))
        itempool.append(world.create_item("Nrg Drink"))
        itempool.append(world.create_item("Rocket Launcher"))
        itempool.append(world.create_item("Cellphone"))
        itempool.append(world.create_item("Drill"))
        itempool.append(world.create_item("Belt of Grenades"))
        itempool.append(world.create_item("Chair"))
        itempool.append(world.create_item("Rope Launcher"))
        itempool.append(world.create_item("Plungers"))
        itempool.append(world.create_item("Parachute"))
        itempool.append(world.create_item("JetPack"))
        itempool.append(world.create_item("Opacitator"))
        itempool.append(world.create_item("Attorney's Badge"))
        itempool.append(world.create_item("Floor Plans of Bank"))
        itempool.append(world.create_item("Security Footage"))
        itempool.append(world.create_item("Doctor's Analysis"))
        if world.options.EtP != 3: 
            etp_item = world.create_item("Escaping The Prison")
            if world.options.EtP == 1:
                world.push_precollected(etp_item)
    
    if use_EtP(world) or use_StD(world):
        itempool.append(world.create_item("Crowbar"))
    
    if use_StD(world):
        itempool.append(world.create_item("Shield"))
        itempool.append(world.create_item("Lance"))
        itempool.append(world.create_item("Flail"))
        itempool.append(world.create_item("Tow Cable"))
        itempool.append(world.create_item("Basket"))
        itempool.append(world.create_item("Rock"))
        itempool.append(world.create_item("Branch"))
        itempool.append(world.create_item("Sticky Grenade"))
        itempool.append(world.create_item("Bubble"))
        itempool.append(world.create_item("Tunisian Diamond"))
        itempool.append(world.create_item("Jumble Hoppers"))
        itempool.append(world.create_item("Anti-Gravity Cap"))
        itempool.append(world.create_item("Shrink Ray"))
        itempool.append(world.create_item("Pick"))
        itempool.append(world.create_item("Liquidificator"))
        itempool.append(world.create_item("Penny"))
        itempool.append(world.create_item("Tranquilizer"))
        itempool.append(world.create_item("Falcon Punch"))
        itempool.append(world.create_item("Invisibility Pill"))
        itempool.append(world.create_item("Wire"))
        itempool.append(world.create_item("Wormhole Rifle"))
        itempool.append(world.create_item("Laser Cutter"))
        itempool.append(world.create_item("Hammer"))
        itempool.append(world.create_item("Cannon"))
        itempool.append(world.create_item("Plank"))
        itempool.append(world.create_item("Cheese"))
        itempool.append(world.create_item("Rifle"))
        itempool.append(world.create_item("WW2 Gun"))
        itempool.append(world.create_item("WW2 Bomb"))
        itempool.append(world.create_item("WW2 Plane"))
        itempool.append(world.create_item("Metroid"))
        itempool.append(world.create_item("Goodball"))
        itempool.append(world.create_item("Mushroom"))
        itempool.append(world.create_item("Division By Zero"))
        itempool.append(world.create_item("Nuclear Bomb"))
        itempool.append(world.create_item("Shoop da Whoop"))
        itempool.append(world.create_item("Giant CCC Robot"))
        if world.options.StD != 3: 
            std_item = world.create_item("Stealing The Diamond")
            if world.options.StD == 1:
                world.push_precollected(std_item)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
    
