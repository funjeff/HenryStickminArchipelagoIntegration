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
    "Part 66 of my Henry Stickmin Playthrough":72,
    "Earpiece":73,
    "Cannon Ball":74,
    "Sticky Hand":75,
    "Grapple Gun":76,
    "Ball 'n Chain":77,
    "Zero-Point Energy":78,
    "Joy Buzzer":79,
    "Expanding Foam":80,
    "Bomb":81,
    "Stretch Chewies":82,
    "Magic Pencil":83,
    "Wizard Magic":84,
    "Retroglove":85,
    "Clawpack":86,
    "Paperizor":138,
    "Shrink 'n Grow":87,
    "Gravity Manipulator":88,
    "Shell":89,
    "Armor":90,
    "Propane Tank":91,
    "Umbrella":92,
    "D.E.B Disk":93,
    "L. Cut mk. II Disk":94,
    "Prototype Disk":95,
    "Scratched Disk":96,
    "Cannon Ball Laser":97,
    "Cannon Ball Chair":98,
    "Cannon Ball Thruster":99,
    "Cannon Ball Spikes":100,
    "Cannon Ball Boost":101,
    "Cannon Ball Eject Button":102,
    "Warp":103,
    "Beans":104,
    "Metal Fist":105,
    "Robo Pants":106,
    "Metalbending":107,
    "Dirk":108,
    "Yo-Yo":109,
    "Multi bottle rocket":110,
    "Chainsaw":111,
    "Glider":112,
    "JetBoots":113,
    "Beef Up":114,
    "Tank":115,
    "Missile":116,
    "Dummies":117,
    "C4":118,
    "Acid":119,
    "Vacuum":120,
    "Toppat Disguise":121,
    "Glue":122,
    "Transdimensionalizer":123,
    "Platform":124,
    "Gravity Bubble":125,
    "Robo Helper":126,
    "Bone Melt":127,
    "Mind Control":128,
    "Gatling Gun":129,
    "Remote Access":130,
    "Ninja Star":131,
    "Falcon Kick":132,
    "Spider On A Stick":133,
    "Sleeping Gas":134,
    "Banana Bomb":135,
    "Flashbang":136,
    "Force Gun":137,
    "PSI Flash":138,
    "Fire Magic":139

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
    "Earpiece":ItemClassification.progression,
    "Cannon Ball":ItemClassification.progression,
    "Sticky Hand":ItemClassification.progression,
    "Grapple Gun":ItemClassification.progression,
    "Ball 'n Chain":ItemClassification.progression,
    "Zero-Point Energy":ItemClassification.progression,
    "Joy Buzzer":ItemClassification.progression,
    "Expanding Foam":ItemClassification.progression,
    "Bomb":ItemClassification.progression,
    "Stretch Chewies":ItemClassification.progression,
    "Magic Pencil":ItemClassification.progression,
    "Wizard Magic":ItemClassification.progression,
    "Retroglove":ItemClassification.progression,
    "Clawpack":ItemClassification.progression,
    "Shrink 'n Grow":ItemClassification.progression,
    "Gravity Manipulator":ItemClassification.progression,
    "Shell":ItemClassification.progression,
    "Armor":ItemClassification.progression,
    "Propane Tank":ItemClassification.progression,
    "Umbrella":ItemClassification.progression,
    "D.E.B Disk":ItemClassification.progression,
    "L. Cut mk. II Disk":ItemClassification.progression,
    "Prototype Disk":ItemClassification.progression,
    "Scratched Disk":ItemClassification.progression,
    "Cannon Ball Laser":ItemClassification.progression,
    "Cannon Ball Chair":ItemClassification.progression,
    "Cannon Ball Thruster":ItemClassification.progression,
    "Cannon Ball Spikes":ItemClassification.progression,
    "Cannon Ball Boost":ItemClassification.progression,
    "Cannon Ball Eject Button":ItemClassification.progression,
    "Warp":ItemClassification.progression,
    "Beans":ItemClassification.progression,
    "Metal Fist":ItemClassification.progression,
    "Robo Pants":ItemClassification.progression,
    "Metalbending":ItemClassification.progression,
    "Dirk":ItemClassification.progression,
    "Yo-Yo":ItemClassification.progression,
    "Multi bottle rocket":ItemClassification.progression,
    "Chainsaw":ItemClassification.progression,
    "Glider":ItemClassification.progression,
    "JetBoots":ItemClassification.progression,
    "Beef Up":ItemClassification.progression,
    "Tank":ItemClassification.progression,
    "Missile":ItemClassification.progression,
    "Dummies":ItemClassification.progression,
    "C4":ItemClassification.progression,
    "Acid":ItemClassification.progression,
    "Vacuum":ItemClassification.progression,
    "Toppat Disguise":ItemClassification.progression,
    "Glue":ItemClassification.progression,
    "Transdimensionalizer":ItemClassification.progression,
    "Platform":ItemClassification.progression,
    "Gravity Bubble":ItemClassification.progression,
    "Robo Helper":ItemClassification.progression,
    "Bone Melt":ItemClassification.progression,
    "Mind Control":ItemClassification.progression,
    "Gatling Gun":ItemClassification.progression,
    "Remote Access":ItemClassification.progression,
    "Ninja Star":ItemClassification.progression,
    "Falcon Kick":ItemClassification.progression,
    "Spider On A Stick":ItemClassification.progression,
    "Sleeping Gas":ItemClassification.progression,
    "Banana Bomb":ItemClassification.progression,
    "Flashbang":ItemClassification.progression,
    "Force Gun":ItemClassification.progression,
    "Paperizor":ItemClassification.progression,
    "PSI Flash":ItemClassification.progression,
    "Fire Magic":ItemClassification.progression
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
        

    if use_BtB(world) or use_EtP(world) or use_StD(world) or use_ItA(world):
        teleporter_item = world.create_item("Teleporter") 
        if world.options.Teleporter_Start == 1:
            world.push_precollected(teleporter_item)

    if use_EtP(world):
        itempool.append(world.create_item("File"))
        itempool.append(world.create_item("Nrg Drink"))

        itempool.append(world.create_item("Cellphone"))
        itempool.append(world.create_item("Drill"))
        itempool.append(world.create_item("Belt of Grenades"))
        itempool.append(world.create_item("Chair"))
        itempool.append(world.create_item("Rope Launcher"))
        itempool.append(world.create_item("Plungers"))
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

    if use_EtP(world) or use_ItA(world):
        itempool.append(world.create_item("Rocket Launcher"))
        itempool.append(world.create_item("Parachute"))
    
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
    
    if use_ItA(world):
        itempool.append(world.create_item("Earpiece"))
        itempool.append(world.create_item("Cannon Ball"))
        itempool.append(world.create_item("Sticky Hand"))
        itempool.append(world.create_item("Grapple Gun"))
        itempool.append(world.create_item("Ball 'n Chain"))
        itempool.append(world.create_item("Zero-Point Energy"))
        itempool.append(world.create_item("Joy Buzzer"))
        itempool.append(world.create_item("Expanding Foam"))
        itempool.append(world.create_item("Bomb"))
        itempool.append(world.create_item("Stretch Chewies"))
        itempool.append(world.create_item("Magic Pencil"))
        itempool.append(world.create_item("Wizard Magic"))
        itempool.append(world.create_item("Retroglove"))
        itempool.append(world.create_item("Clawpack"))
        itempool.append(world.create_item("Shrink 'n Grow"))
        itempool.append(world.create_item("Gravity Manipulator"))
        itempool.append(world.create_item("Shell"))
        itempool.append(world.create_item("Armor"))
        itempool.append(world.create_item("Propane Tank"))
        itempool.append(world.create_item("Umbrella"))
        itempool.append(world.create_item("D.E.B Disk"))
        itempool.append(world.create_item("L. Cut mk. II Disk"))
        itempool.append(world.create_item("Prototype Disk"))
        itempool.append(world.create_item("Scratched Disk"))
        itempool.append(world.create_item("Cannon Ball Laser"))
        itempool.append(world.create_item("Cannon Ball Chair"))
        itempool.append(world.create_item("Cannon Ball Thruster"))
        itempool.append(world.create_item("Cannon Ball Spikes"))
        itempool.append(world.create_item("Cannon Ball Boost"))
        itempool.append(world.create_item("Cannon Ball Eject Button"))
        itempool.append(world.create_item("Warp"))
        itempool.append(world.create_item("Beans"))
        itempool.append(world.create_item("Metal Fist"))
        itempool.append(world.create_item("Robo Pants"))
        itempool.append(world.create_item("Metalbending"))
        itempool.append(world.create_item("Dirk"))
        itempool.append(world.create_item("Yo-Yo"))
        itempool.append(world.create_item("Multi bottle rocket"))
        itempool.append(world.create_item("Chainsaw"))
        itempool.append(world.create_item("Glider"))
        itempool.append(world.create_item("JetBoots"))
        itempool.append(world.create_item("Beef Up"))
        itempool.append(world.create_item("Tank"))
        itempool.append(world.create_item("Missile"))
        itempool.append(world.create_item("Dummies"))
        itempool.append(world.create_item("C4"))
        itempool.append(world.create_item("Acid"))
        itempool.append(world.create_item("Vacuum"))
        itempool.append(world.create_item("Toppat Disguise"))
        itempool.append(world.create_item("Glue"))
        itempool.append(world.create_item("Transdimensionalizer"))
        itempool.append(world.create_item("Platform"))
        itempool.append(world.create_item("Gravity Bubble"))
        itempool.append(world.create_item("Robo Helper"))
        itempool.append(world.create_item("Bone Melt"))
        itempool.append(world.create_item("Mind Control"))
        itempool.append(world.create_item("Gatling Gun"))
        itempool.append(world.create_item("Remote Access"))
        itempool.append(world.create_item("Ninja Star"))
        itempool.append(world.create_item("Falcon Kick"))
        itempool.append(world.create_item("Spider On A Stick"))
        itempool.append(world.create_item("Sleeping Gas"))
        itempool.append(world.create_item("Banana Bomb"))
        itempool.append(world.create_item("Flashbang"))
        itempool.append(world.create_item("Force Gun"))
        itempool.append(world.create_item("Fire Magic"))
        itempool.append(world.create_item("PSI Flash"))
        if world.options.ItA != 3: 
            ita_item = world.create_item("Infiltraiting The Airship")
            if world.options.ItA == 1:
                world.push_precollected(ita_item)


    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
    
