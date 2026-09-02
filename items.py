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
    "Anti-Gravity Cap": 43,
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
    "Giant CCC Robot": 68, #yes I removed index 67 no it wasen't intentaional (CCC is a softlock if you don't have anything so one of them has to be avilable from the start)
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
    "Paperizor":140,
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
    "Fire Magic":139,
    "Sonic Pulse":141,
    "Cookie":142,
    "Laser Plane":143,
    "Bubble Shield":144,
    "Earthbending":145,
    "Flash":146,
    "Sniper Rifle":147,
    "Mini Helicopter":148,
    "Undercover Agent":149,
    "Neurotoxin":150,
    "Drill Pod":151,
    "Slingshot":152,
    "Magnet":153,
    "Sick Ride":154,
    "Speed Shoes":155,
    "Tool Gun":156,
    "Item Box":157,
    "Sword":158,
    "Wall Truck Keys":159,
    "Sandwich":160,
    "Snowman Costume":161,
    "Pistol":162,
    "Warpstar":163,
    "Airbag":164,
    "Whoopee Cushion":165,
    "Command Melody":166,
    "Power Jump":167,
    "Longshot":168,
    "Spring":169,
    "Balloon":170,
    "Helium":172,
    "Plunger Boots":173,
    "Cardboard Box":174,
    "Super Leaf":175,
    "Shadozer":176,
    "S.S. Annie":177,
    "Dinghy":178,
    "Rocket":179,
    "Trenchcoat":180,
    "Bounce Bros":181,
    "The Force":182,
    "GraviToR v2.0":183,
    "Grenade":184,
    "Crossbow":185,
    "Taser":186,
    "The Wall Hat":187,
    "Adrenaline":188,
    "The KNEE":189,
    "Motercycle":190,
    "Charles's Phone Number":191,
    "Reginald's Phone Number":192,
    "Super Punch":193,
    "Wrist Strapped Grapple Hook":194,
    "Very Accurate Targetting System":195,
    "Mounted Gun":196,
    "Helicopter":197,
    "Flute":198,
    "Revolver":199,
    "Boomerang":200,
    "Summon":201,
    "Stylish Moves":202,
    "Dual Tech":203,
    "G-Inverter":204,
    "Cloud":205,
    "Thunder II":206,
    "Lockpick":207,
    "Metal Hat":208,
    "Melt Ray":209,
    "Big Sword":210,
    "Underbarrel Grenade Launcher":211,
    "Pew Pew Gun":212,
    "Harden":213,
    "Nano-Suit":214,
    "Max Gravity Boots":215,
    "Nano-Suit Missiles":216,
    "Positron Reflector":217,
    "Communications Satellite":218,
    "Backwards Satellite":219,
    "Offsite Drop Pod":220,
    "Drawing":221,
    "Cupcake":222,
    "JetPod":223,
    "Trapeze":224,
    "Invisible Bridge":225,
    "TV Broadcast":226,
    "Subsonic Wave":227,
    "Remote Toppat":228,
    "Wrench":229,
    "Red Herring":230,
    "Swapper":231,
    "Painting Portal":232,
    "Bug Juice":233,
    "Sleep Dart":234,
    "Horn":235,
    "IR Sniper":236,
    "Umbrella Glider":237,
    "Wings":239,
    "Dirt Blocks":238,
    "Barrel":240,
    "Human Cannon":241,
    "Net Launcher":242,
    "Downgrader":243,
    "Fusion Earings":244,
    "Scooter Drill":245,
    "Spiked Wheels":246,
    "Battering Ram":247,
    "Mosquito Mode":248,
    "Light Speed":249,
    "Bridge":250,
    "Catapult":251,
    "Pole Vault Stick":252,
    "Wooden Ramp":253,
    "Paper Rocket":254,
    "SMASH":255,
    "Chance Dice":256,
    "Norwegian Emerald":257,
    "Rah Doh FOO":258,
    "Save States":259,
    "Grow 'n Shrink":260,
    "Mirror":261,
    "Train Car Spring":262,
    "Inflatable Raft":263,
    "Rope":264,
    "Controller":265,
    "Time Machine":266,
    "CorrupTick":267,
    "Disguise Kit":268,
    "Block":269,
    "Glitchy Physics Engine":270,
    "Knife":271,
    "Lagswitch":272,
    "Duplicatorange":273,
    "Scrambler":274,
    "Walkthrough":275,
    "Evil Moon":276,
    "Ultimate Freeze":277,
    "G.A.B.E.G.G":288,
    "Toppat Box":289,
    "Prop":290,
    "Magic Hat":291,
    "Pinchers":292,
    "Free Transform":293,
    "Infini3":294,
    "LeafMode":295,
    "SuccPak":296,
    "Woolooloo":297,
    "Cluster Charge":298,
    "Cheap Fighting Combo":299,
    "Self Destruct":300,
    "Ocarina":301,
    "Trash Ball":302,
    "Air Cannon":303,
    "Warp Beam":304,
    "Hot Knife":305,
    "Super Accurate Laser Shot":306,
    "Luxury Escape Pod":307,
    "Normal Escape Pod":308,
    "Damaged Escape Pod":309,
    "Helicopter Hat":310,
    "Toppy":311,
    "Mind Crystal":312,
    "Good Gents Doc":313,
    "Midnight Surprise Doc":314,
    "Deuces! Doc":315,
    "Fulton":316,
    "Purse of Holding":317,
    "Shell Bounce":318,
    "Needle":319,
    "Wombo Combo":320,
    "Blade Forme":321,
    "Spirit Forme":322,
    "Gun Forme":323,
    "Baseball Bat":324,
    "Y-Type Move":325,
    "Staple":326,
    "Relentless Bounty Hunter Timeline Unlock":327,
    "Government Supported Private Investigator Timeline Unlock":328,
    "Rapidly Promoted Executive Timeline Unlock":329,
    "Pure Blooded Thief Timeline Unlock":330,
    "Presumed Dead Timeline Unlock":331,
    "International Rescue Operative Timeline Unlock":332,
    "The Betrayed Timeline Unlock":333,
    "Ghost Inmate Timeline Unlock":334,
    "Convict Allies Timeline Unlock":335

    
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
    "Fire Magic":ItemClassification.progression,
    "Sonic Pulse":ItemClassification.progression,
    "Cookie":ItemClassification.progression,
    "Laser Plane":ItemClassification.progression,
    "Bubble Shield":ItemClassification.progression,
    "Earthbending":ItemClassification.progression,
    "Flash":ItemClassification.progression,
    "Sniper Rifle":ItemClassification.progression,
    "Mini Helicopter":ItemClassification.progression,
    "Undercover Agent":ItemClassification.progression,
    "Neurotoxin":ItemClassification.progression,
    "Drill Pod":ItemClassification.progression,
    "Slingshot":ItemClassification.progression,
    "Magnet":ItemClassification.progression,
    "Sick Ride":ItemClassification.progression,
    "Speed Shoes":ItemClassification.progression,
    "Tool Gun":ItemClassification.progression,
    "Item Box":ItemClassification.progression,
    "Sword":ItemClassification.progression,
    "Wall Truck Keys":ItemClassification.progression,
    "Sandwich":ItemClassification.progression,
    "Snowman Costume":ItemClassification.progression,
    "Pistol":ItemClassification.progression,
    "Warpstar":ItemClassification.progression,
    "Airbag":ItemClassification.progression,
    "Whoopee Cushion":ItemClassification.progression,
    "Command Melody":ItemClassification.progression,
    "Power Jump":ItemClassification.progression,
    "Longshot":ItemClassification.progression,
    "Spring":ItemClassification.progression,
    "Balloon":ItemClassification.progression,
    "Helium":ItemClassification.progression,
    "Plunger Boots":ItemClassification.progression,
    "Cardboard Box":ItemClassification.progression,
    "Super Leaf":ItemClassification.progression,
    "Shadozer":ItemClassification.progression,
    "S.S. Annie":ItemClassification.progression,
    "Dinghy":ItemClassification.progression,
    "Rocket":ItemClassification.progression,
    "Trenchcoat":ItemClassification.progression,
    "Bounce Bros":ItemClassification.progression,
    "The Force":ItemClassification.progression,
    "GraviToR v2.0":ItemClassification.progression,
    "Grenade":ItemClassification.progression,
    "Crossbow":ItemClassification.progression,
    "Taser":ItemClassification.progression,
    "The Wall Hat":ItemClassification.progression,
    "Adrenaline":ItemClassification.progression,
    "The KNEE":ItemClassification.progression,
    "Motercycle":ItemClassification.progression,
    "Charles's Phone Number":ItemClassification.progression,
    "Reginald's Phone Number":ItemClassification.progression,
    "Super Punch":ItemClassification.progression,
    "Wrist Strapped Grapple Hook":ItemClassification.progression,
    "Very Accurate Targetting System":ItemClassification.progression,
    "Mounted Gun":ItemClassification.progression,
    "Helicopter":ItemClassification.progression,
    "Flute":ItemClassification.progression,
    "Revolver":ItemClassification.progression,
    "Boomerang":ItemClassification.progression,
    "Summon":ItemClassification.progression,
    "Stylish Moves":ItemClassification.progression,
    "Dual Tech":ItemClassification.progression,
    "G-Inverter":ItemClassification.progression,
    "Cloud":ItemClassification.progression,
    "Thunder II":ItemClassification.progression,
    "Lockpick":ItemClassification.progression,
    "Metal Hat":ItemClassification.progression,
    "Melt Ray":ItemClassification.progression,
    "Big Sword":ItemClassification.progression,
    "Underbarrel Grenade Launcher":ItemClassification.progression,
    "Pew Pew Gun":ItemClassification.progression,
    "Harden":ItemClassification.progression,
    "Nano-Suit":ItemClassification.progression,
    "Max Gravity Boots":ItemClassification.progression,
    "Nano-Suit Missiles":ItemClassification.progression,
    "Positron Reflector":ItemClassification.progression,
    "Communications Satellite":ItemClassification.progression,
    "Backwards Satellite":ItemClassification.progression,
    "Offsite Drop Pod":ItemClassification.progression,
    "Drawing":ItemClassification.progression,
    "Cupcake":ItemClassification.progression,
    "JetPod":ItemClassification.progression,
    "Trapeze":ItemClassification.progression,
    "Invisible Bridge":ItemClassification.progression,
    "TV Broadcast":ItemClassification.progression,
    "Subsonic Wave":ItemClassification.progression,
    "Remote Toppat":ItemClassification.progression,
    "Wrench":ItemClassification.progression,
    "Red Herring":ItemClassification.progression,
    "Swapper":ItemClassification.progression,
    "Painting Portal":ItemClassification.progression,
    "Bug Juice":ItemClassification.progression,
    "Sleep Dart":ItemClassification.progression,
    "Horn":ItemClassification.progression,
    "IR Sniper":ItemClassification.progression,
    "Umbrella Glider":ItemClassification.progression,
    "Wings":ItemClassification.progression,
    "Dirt Blocks":ItemClassification.progression,
    "Barrel":ItemClassification.progression,
    "Human Cannon":ItemClassification.progression,
    "Net Launcher":ItemClassification.progression,
    "Downgrader":ItemClassification.progression,
    "Fusion Earings":ItemClassification.progression,
    "Scooter Drill":ItemClassification.progression,
    "Spiked Wheels":ItemClassification.progression,
    "Battering Ram":ItemClassification.progression,
    "Mosquito Mode":ItemClassification.progression,
    "Light Speed":ItemClassification.progression,
    "Bridge":ItemClassification.progression,
    "Catapult":ItemClassification.progression,
    "Pole Vault Stick":ItemClassification.progression,
    "Wooden Ramp":ItemClassification.progression,
    "Paper Rocket":ItemClassification.progression,
    "SMASH":ItemClassification.progression,
    "Chance Dice":ItemClassification.progression,
    "Norwegian Emerald":ItemClassification.progression,
    "Rah Doh FOO":ItemClassification.progression,
    "Save States":ItemClassification.progression,
    "Grow 'n Shrink":ItemClassification.progression,
    "Mirror":ItemClassification.progression,
    "Train Car Spring":ItemClassification.progression,
    "Inflatable Raft":ItemClassification.progression,
    "Rope":ItemClassification.progression,
    "Controller":ItemClassification.progression,
    "Time Machine":ItemClassification.progression,
    "CorrupTick":ItemClassification.progression,
    "Disguise Kit":ItemClassification.progression,
    "Block":ItemClassification.progression,
    "Glitchy Physics Engine":ItemClassification.progression,
    "Knife":ItemClassification.progression,
    "Lagswitch":ItemClassification.progression,
    "Duplicatorange":ItemClassification.progression,
    "Scrambler":ItemClassification.progression,
    "Walkthrough":ItemClassification.progression,
    "Evil Moon":ItemClassification.progression,
    "Ultimate Freeze":ItemClassification.progression,
    "G.A.B.E.G.G":ItemClassification.progression,
    "Toppat Box":ItemClassification.progression,
    "Prop":ItemClassification.progression,
    "Magic Hat":ItemClassification.progression,
    "Pinchers":ItemClassification.progression,
    "Free Transform":ItemClassification.progression,
    "Infini3":ItemClassification.progression,
    "LeafMode":ItemClassification.progression,
    "SuccPak":ItemClassification.progression,
    "Woolooloo":ItemClassification.progression,
    "Cluster Charge":ItemClassification.progression,
    "Cheap Fighting Combo":ItemClassification.progression,
    "Self Destruct":ItemClassification.progression,
    "Ocarina":ItemClassification.progression,
    "Trash Ball":ItemClassification.progression,
    "Air Cannon":ItemClassification.progression,
    "Warp Beam":ItemClassification.progression,
    "Hot Knife":ItemClassification.progression,
    "Super Accurate Laser Shot":ItemClassification.progression,
    "Luxury Escape Pod":ItemClassification.progression,
    "Normal Escape Pod":ItemClassification.progression,
    "Damaged Escape Pod":ItemClassification.progression,
    "Helicopter Hat":ItemClassification.progression,
    "Toppy":ItemClassification.progression,
    "Mind Crystal":ItemClassification.progression,
    "Good Gents Doc":ItemClassification.progression,
    "Midnight Surprise Doc":ItemClassification.progression,
    "Deuces! Doc":ItemClassification.progression,
    "Fulton":ItemClassification.progression,
    "Purse of Holding":ItemClassification.progression,
    "Shell Bounce":ItemClassification.progression,
    "Needle":ItemClassification.progression,
    "Wombo Combo":ItemClassification.progression,
    "Blade Forme":ItemClassification.progression,
    "Spirit Forme":ItemClassification.progression,
    "Gun Forme":ItemClassification.progression,
    "Baseball Bat":ItemClassification.progression,
    "Y-Type Move":ItemClassification.progression,
    "Staple":ItemClassification.progression,
    "Relentless Bounty Hunter Timeline Unlock":ItemClassification.progression,
    "Government Supported Private Investigator Timeline Unlock":ItemClassification.progression,
    "Rapidly Promoted Executive Timeline Unlock":ItemClassification.progression,
    "Pure Blooded Thief Timeline Unlock":ItemClassification.progression,
    "Presumed Dead Timeline Unlock":ItemClassification.progression,
    "International Rescue Operative Timeline Unlock":ItemClassification.progression,
    "The Betrayed Timeline Unlock":ItemClassification.progression,
    "Ghost Inmate Timeline Unlock":ItemClassification.progression,
    "Convict Allies Timeline Unlock":ItemClassification.progression
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class HenryStickminItem(Item):
    game = "Henry Stickmin"


def get_random_filler_item_name(world: HenryStickminWorld) -> str:
    
    fillNum = world.random.randint(0,5)

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
        else:
            itempool.append(btb_item)


    if use_BtB(world) or use_EtP(world):
        itempool.append(world.create_item("Money Bag Disguise"))
        

    if use_BtB(world) or use_EtP(world) or use_StD(world) or use_ItA(world) or use_FtC(world) or use_CtM(world):
        teleporter_item = world.create_item("Teleporter") 
        if world.options.Teleporter_Start == 1:
            world.push_precollected(teleporter_item)
        else:
            itempool.append(teleporter_item)

    if use_EtP(world):
        itempool.append(world.create_item("File"))
        itempool.append(world.create_item("Nrg Drink"))

        itempool.append(world.create_item("Cellphone"))
        itempool.append(world.create_item("Drill"))
        itempool.append(world.create_item("Belt of Grenades"))
        itempool.append(world.create_item("Chair"))
        itempool.append(world.create_item("Plungers"))
        itempool.append(world.create_item("Opacitator"))
        itempool.append(world.create_item("Attorney's Badge"))
        itempool.append(world.create_item("Floor Plans of Bank"))
        itempool.append(world.create_item("Security Footage"))
        itempool.append(world.create_item("Doctor's Analysis"))
        if world.options.EtP != 3: 
            etp_item = world.create_item("Escaping The Prison")
            if world.options.EtP == 1:
                world.push_precollected(etp_item)
            else:
                itempool.append(etp_item)

    if use_EtP(world) or use_CtM(world):
        itempool.append(world.create_item("JetPack"))
        itempool.append(world.create_item("Rope Launcher"))


    if use_EtP(world) or use_StD(world):
        itempool.append(world.create_item("Crowbar"))

    if use_EtP(world) or use_ItA(world) or use_FtC(world) or use_CtM(world):
        itempool.append(world.create_item("Rocket Launcher"))

    
    if use_EtP(world) or use_ItA(world) or use_FtC(world) or use_CtM(world):
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
        itempool.append(world.create_item("Giant CCC Robot"))
        if world.options.StD != 3: 
            std_item = world.create_item("Stealing The Diamond")
            if world.options.StD == 1:
                world.push_precollected(std_item)
            else:
                itempool.append(std_item)
    
    if use_StD(world) or use_CtM(world):
        itempool.append(world.create_item("Hammer"))
        itempool.append(world.create_item("Cannon"))
        itempool.append(world.create_item("Nuclear Bomb"))
    
    if use_ItA(world):
        itempool.append(world.create_item("Earpiece"))
        itempool.append(world.create_item("Cannon Ball"))
        itempool.append(world.create_item("Sticky Hand"))
        itempool.append(world.create_item("Ball 'n Chain"))
        itempool.append(world.create_item("Zero-Point Energy"))
        itempool.append(world.create_item("Joy Buzzer"))
        itempool.append(world.create_item("Expanding Foam"))
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
        itempool.append(world.create_item("Glider"))
        itempool.append(world.create_item("JetBoots"))
        itempool.append(world.create_item("Beef Up"))
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
        itempool.append(world.create_item("Paperizor"))
        if world.options.ItA != 3: 
            ita_item = world.create_item("Infiltraiting The Airship")
            if world.options.ItA == 1:
                world.push_precollected(ita_item)
            else:
                itempool.append(ita_item)
        
    if use_CtM(world) or use_ItA(world):
        itempool.append(world.create_item("Grapple Gun"))
        itempool.append(world.create_item("Bomb"))
        itempool.append(world.create_item("Tank"))
        itempool.append(world.create_item("Chainsaw"))
    
    if (use_FtC(world)):
        itempool.append(world.create_item("Sonic Pulse"))
        itempool.append(world.create_item("Cookie"))
        itempool.append(world.create_item("Laser Plane"))
        itempool.append(world.create_item("Bubble Shield"))
        itempool.append(world.create_item("Earthbending"))
        itempool.append(world.create_item("Flash"))
        itempool.append(world.create_item("Mini Helicopter"))
        itempool.append(world.create_item("Undercover Agent"))
        itempool.append(world.create_item("Neurotoxin"))
        itempool.append(world.create_item("Drill Pod"))
        itempool.append(world.create_item("Slingshot"))
        itempool.append(world.create_item("Magnet"))
        itempool.append(world.create_item("Sick Ride"))
        itempool.append(world.create_item("Speed Shoes"))
        itempool.append(world.create_item("Tool Gun"))
        itempool.append(world.create_item("Item Box"))
        itempool.append(world.create_item("Wall Truck Keys"))
        itempool.append(world.create_item("Sandwich"))
        itempool.append(world.create_item("Snowman Costume"))
        itempool.append(world.create_item("Pistol"))
        itempool.append(world.create_item("Warpstar"))
        itempool.append(world.create_item("Airbag"))
        itempool.append(world.create_item("Whoopee Cushion"))
        itempool.append(world.create_item("Command Melody"))
        itempool.append(world.create_item("Power Jump"))
        itempool.append(world.create_item("Longshot"))
        itempool.append(world.create_item("Spring"))
        itempool.append(world.create_item("Balloon"))
        itempool.append(world.create_item("Helium"))
        itempool.append(world.create_item("Plunger Boots"))
        itempool.append(world.create_item("Cardboard Box"))
        itempool.append(world.create_item("Super Leaf"))
        itempool.append(world.create_item("Shadozer"))
        itempool.append(world.create_item("S.S. Annie"))
        itempool.append(world.create_item("Dinghy"))
        itempool.append(world.create_item("Rocket"))
        itempool.append(world.create_item("Trenchcoat"))
        itempool.append(world.create_item("Bounce Bros"))
        itempool.append(world.create_item("GraviToR v2.0"))
        itempool.append(world.create_item("Grenade"))
        itempool.append(world.create_item("Crossbow"))
        itempool.append(world.create_item("Taser"))
        itempool.append(world.create_item("The Wall Hat"))
        itempool.append(world.create_item("Adrenaline"))
        itempool.append(world.create_item("The KNEE"))
        itempool.append(world.create_item("Motercycle"))
        if (not use_ItA(world) or world.options.FtCPhoneAFriendMode == 1):
            itempool.append(world.create_item("Charles's Phone Number"))
            itempool.append(world.create_item("Reginald's Phone Number"))
            
        if world.options.FtC != 3: 
            ftc_item = world.create_item("Fleeing The Complex")
            if world.options.FtC == 1:
                world.push_precollected(ftc_item)
            else:
                itempool.append(ftc_item)

    if use_FtC(world) or use_CtM(world):
        itempool.append(world.create_item("Sniper Rifle"))
        itempool.append(world.create_item("Rope"))
        itempool.append(world.create_item("Sword"))
        itempool.append(world.create_item("The Force"))
    
    if use_CtM(world):
        itempool.append(world.create_item("Super Punch"))
        itempool.append(world.create_item("Wrist Strapped Grapple Hook"))
        itempool.append(world.create_item("Very Accurate Targetting System"))
        itempool.append(world.create_item("Mounted Gun"))
        itempool.append(world.create_item("Helicopter"))
        itempool.append(world.create_item("Flute"))
        itempool.append(world.create_item("Revolver"))
        itempool.append(world.create_item("Boomerang"))
        itempool.append(world.create_item("Summon"))
        itempool.append(world.create_item("Stylish Moves"))
        itempool.append(world.create_item("Dual Tech"))
        itempool.append(world.create_item("G-Inverter"))
        itempool.append(world.create_item("Cloud"))
        itempool.append(world.create_item("Thunder II"))
        itempool.append(world.create_item("Lockpick"))
        itempool.append(world.create_item("Metal Hat"))
        itempool.append(world.create_item("Melt Ray"))
        itempool.append(world.create_item("Big Sword"))
        itempool.append(world.create_item("Underbarrel Grenade Launcher"))
        itempool.append(world.create_item("Pew Pew Gun"))
        itempool.append(world.create_item("Harden"))
        itempool.append(world.create_item("Nano-Suit"))
        itempool.append(world.create_item("Max Gravity Boots"))
        itempool.append(world.create_item("Nano-Suit Missiles"))
        itempool.append(world.create_item("Positron Reflector"))
        itempool.append(world.create_item("Communications Satellite"))
        itempool.append(world.create_item("Backwards Satellite"))
        itempool.append(world.create_item("Offsite Drop Pod"))
        itempool.append(world.create_item("Drawing"))
        itempool.append(world.create_item("Cupcake"))
        itempool.append(world.create_item("JetPod"))
        itempool.append(world.create_item("Trapeze"))
        itempool.append(world.create_item("Invisible Bridge"))
        itempool.append(world.create_item("TV Broadcast"))
        itempool.append(world.create_item("Subsonic Wave"))
        itempool.append(world.create_item("Remote Toppat"))
        itempool.append(world.create_item("Wrench"))
        itempool.append(world.create_item("Red Herring"))
        itempool.append(world.create_item("Swapper"))
        itempool.append(world.create_item("Painting Portal"))
        itempool.append(world.create_item("Bug Juice"))
        itempool.append(world.create_item("Sleep Dart"))
        itempool.append(world.create_item("Horn"))
        itempool.append(world.create_item("IR Sniper"))
        itempool.append(world.create_item("Umbrella Glider"))
        itempool.append(world.create_item("Wings"))
        itempool.append(world.create_item("Dirt Blocks"))
        itempool.append(world.create_item("Barrel"))
        itempool.append(world.create_item("Human Cannon"))
        itempool.append(world.create_item("Net Launcher"))
        itempool.append(world.create_item("Downgrader"))
        itempool.append(world.create_item("Fusion Earings"))
        itempool.append(world.create_item("Scooter Drill"))
        itempool.append(world.create_item("Spiked Wheels"))
        itempool.append(world.create_item("Battering Ram"))
        itempool.append(world.create_item("Mosquito Mode"))
        itempool.append(world.create_item("Light Speed"))
        itempool.append(world.create_item("Bridge"))
        itempool.append(world.create_item("Catapult"))
        itempool.append(world.create_item("Pole Vault Stick"))
        itempool.append(world.create_item("Wooden Ramp"))
        itempool.append(world.create_item("Paper Rocket"))
        itempool.append(world.create_item("SMASH"))
        itempool.append(world.create_item("Chance Dice"))
        itempool.append(world.create_item("Norwegian Emerald"))
        itempool.append(world.create_item("Rah Doh FOO"))
        itempool.append(world.create_item("Save States"))
        itempool.append(world.create_item("Grow 'n Shrink"))
        itempool.append(world.create_item("Mirror"))
        itempool.append(world.create_item("Train Car Spring"))
        itempool.append(world.create_item("Inflatable Raft"))
        itempool.append(world.create_item("Controller"))
        itempool.append(world.create_item("Time Machine"))
        itempool.append(world.create_item("CorrupTick"))
        itempool.append(world.create_item("Disguise Kit"))
        itempool.append(world.create_item("Block"))
        itempool.append(world.create_item("Glitchy Physics Engine"))
        itempool.append(world.create_item("Knife"))
        itempool.append(world.create_item("Lagswitch"))
        itempool.append(world.create_item("Duplicatorange"))
        itempool.append(world.create_item("Scrambler"))
        itempool.append(world.create_item("Walkthrough"))
        itempool.append(world.create_item("Evil Moon"))
        itempool.append(world.create_item("Ultimate Freeze"))
        itempool.append(world.create_item("G.A.B.E.G.G"))
        itempool.append(world.create_item("Toppat Box"))
        itempool.append(world.create_item("Prop"))
        itempool.append(world.create_item("Magic Hat"))
        itempool.append(world.create_item("Pinchers"))
        itempool.append(world.create_item("Free Transform"))
        itempool.append(world.create_item("Infini3"))
        itempool.append(world.create_item("LeafMode"))
        itempool.append(world.create_item("SuccPak"))
        itempool.append(world.create_item("Woolooloo"))
        itempool.append(world.create_item("Cluster Charge"))
        itempool.append(world.create_item("Cheap Fighting Combo"))
        itempool.append(world.create_item("Self Destruct"))
        itempool.append(world.create_item("Ocarina"))
        itempool.append(world.create_item("Trash Ball"))
        itempool.append(world.create_item("Air Cannon"))
        itempool.append(world.create_item("Warp Beam"))
        itempool.append(world.create_item("Hot Knife"))
        itempool.append(world.create_item("Super Accurate Laser Shot"))
        itempool.append(world.create_item("Luxury Escape Pod"))
        itempool.append(world.create_item("Normal Escape Pod"))
        itempool.append(world.create_item("Damaged Escape Pod"))
        itempool.append(world.create_item("Helicopter Hat"))
        itempool.append(world.create_item("Toppy"))
        itempool.append(world.create_item("Mind Crystal"))
        itempool.append(world.create_item("Good Gents Doc"))
        itempool.append(world.create_item("Midnight Surprise Doc"))
        itempool.append(world.create_item("Deuces! Doc"))
        itempool.append(world.create_item("Fulton"))
        itempool.append(world.create_item("Purse of Holding"))
        itempool.append(world.create_item("Shell Bounce"))
        itempool.append(world.create_item("Needle"))
        itempool.append(world.create_item("Wombo Combo"))
        itempool.append(world.create_item("Blade Forme"))
        itempool.append(world.create_item("Spirit Forme"))
        itempool.append(world.create_item("Gun Forme"))
        itempool.append(world.create_item("Baseball Bat"))
        itempool.append(world.create_item("Y-Type Move"))
        itempool.append(world.create_item("Staple"))

        if world.options.CtM != 3: 
            ctm_item = world.create_item("Completing The Mission")
            if world.options.CtM == 1:
                world.push_precollected(ctm_item)
            else:
                itempool.append(ctm_item)
        
        if world.options.CtMTimelineUnlockMode == world.options.CtMTimelineUnlockMode.option_open_world:
            world.push_precollected(world.create_item("Relentless Bounty Hunter Timeline Unlock"))
            world.push_precollected(world.create_item("Government Supported Private Investigator Timeline Unlock"))
            world.push_precollected(world.create_item("Rapidly Promoted Executive Timeline Unlock"))
            world.push_precollected(world.create_item("Pure Blooded Thief Timeline Unlock"))
            world.push_precollected(world.create_item("Presumed Dead Timeline Unlock"))
            world.push_precollected(world.create_item("International Rescue Operative Timeline Unlock"))
            world.push_precollected(world.create_item("The Betrayed Timeline Unlock"))
            world.push_precollected(world.create_item("Ghost Inmate Timeline Unlock"))
            world.push_precollected(world.create_item("Convict Allies Timeline Unlock"))
            
        else:
            if world.options.CtMTimelineUnlockMode != 0 or not use_ItA(world):
                itempool.append(world.create_item("Relentless Bounty Hunter Timeline Unlock"))
                itempool.append(world.create_item("Government Supported Private Investigator Timeline Unlock"))
                itempool.append(world.create_item("Rapidly Promoted Executive Timeline Unlock"))
                itempool.append(world.create_item("Pure Blooded Thief Timeline Unlock"))

            if world.options.CtMTimelineUnlockMode != 0 or not use_CtM(world):
                itempool.append(world.create_item("Presumed Dead Timeline Unlock"))
                itempool.append(world.create_item("International Rescue Operative Timeline Unlock"))
                itempool.append(world.create_item("The Betrayed Timeline Unlock"))
                itempool.append(world.create_item("Ghost Inmate Timeline Unlock"))
                itempool.append(world.create_item("Convict Allies Timeline Unlock"))





    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool
    
