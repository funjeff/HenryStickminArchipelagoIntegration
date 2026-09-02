from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location
from rule_builder.rules import Has, HasAll, Rule

from .henryHelpers import *
from .items import HenryStickminItem

if TYPE_CHECKING:
    from . import HenryStickminWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.
LOCATION_NAME_TO_ID = {
    "BtB Bank: Shovel Fail": 1,
    "BtB Bank: Explosives Fail": 2,
    "BtB Bank: Teleporter Fail": 3,
    "BtB Bank: Laser Fail": 4,
    "BtB Bank: Wrecking Ball Fail": 5,
    "BtB: The Story Begins": 6,
    "EtP Cell: Nrg Drink Fail": 7,
    "EtP Cell: Teleporter Fail": 8,
    "EtP Cell: Rocket Launcher Fail": 9,
    "EtP Cell: File Window Fail": 10,
    "EtP Cell Block: Rupert Kick Fail": 11,
    "EtP Cell Block: Dave Taser Fail": 12,
    "EtP Closet: Belt of Grenades Fail": 13,
    "EtP Closet: Broken Pipe Fail": 14,
    "EtP Rooftop: Rope Fail": 15,
    "EtP Rooftop: Parachute Fail": 16,
    "EtP Rooftop: JetPack Fail": 17,
    "EtP: Sneaky Escapist": 18,
    "EtP Courtroom: Declared Guilty Fail": 19,
    "EtP: Lawyered Up": 20,
    "EtP Bathroom: Opacitator Fail" : 21,
    "EtP Back Lobby: Pillar Fail" : 22,
    "EtP Back Lobby: Shot Fail" : 23,
    "EtP Lobby Turn: Brawl Fail" : 24,
    "EtP Lobby Turn: Crash Fail: " : 25,
    "EtP Prison Entrance: Quicktime event Fail" : 26,
    "EtP: Baddass Bust Out" : 27,
    "StD Outer Wall: Liquidificator Fail" : 28,
    "StD Outer Wall: Shrink Ray Fail" : 29,
    "StD Outer Wall: Anti-Gravity Cap Fail" : 30,
    "StD Outer Wall: Jumble Hoppers Fail" : 31,
    "StD Rooftop: Falcon Punch Fail" : 32,
    "StD Rooftop: Tranquilizer Fail" : 33,
    "StD Rooftop: Invisibility Pill Fail" : 34,
    "StD Catwalk: Drop Fail" : 35,
    "StD Catwalk: Wormhole Rifle Fail" : 36,
    "StD Diamond Exhibit: Laser Cutter Fail" : 37,
    "StD Storage Room: Cannon Fail" : 38,
    "StD Storage Room: Cheese Fail" : 39,
    "StD Backdoor: Snap Neck Fail" : 40,
    "StD Backdoor: Rifle Fail" : 41,
    "StD Backdoor: Jump Fail" : 42,
    "StD: Unseen Burglar" : 52,
    "StD WW2 Exhibit: Dave Conversation Fail" : 43,
    "StD WW2 Exhibit: Bomb Fail" : 44,
    "StD WW2 Exhibit: Gun Fail" : 45,
    "StD Diamond Exhibit Entrance: Light Sleeper Fail" : 46,
    "StD Retro Exhibit: Alien Fail" : 47,
    "StD Retro Exhibit: Goodball Fail" : 48,
    "StD Retro Exhibit: Crowbar Fail" : 49,
    "StD Center For Chaos Containment: Nuclear Bomb Fail" : 50,
    "StD Center For Chaos Containment: Divide by Zero Fail" : 51,
    "StD Center For Chaos Containment: Shoop da Whoop Fail" : 53,
    "StD: Just Plain Epic" : 54,
    "StD Parking Lot: Kick Fail" : 55,
    "StD Parking Lot: Jump Fail" : 56,
    "StD Parking Lot: Great Start Fail" : 57,
    "StD Medieval Hall: Lance Fail" : 58,
    "StD Medieval Hall: Flail Fail" : 59,
    "StD Medieval Hall: Janitor Fail" : 60,
    "StD Diamond Exhibit (Scooter): Basket Fail" : 61,
    "StD Diamond Exhibit (Scooter): Stand Around Fail" : 62,
    "StD Police Chase Car: Reflexes Fail" : 63,
    "StD Police Chase Car: Branch Fail" : 64,
    "StD Police Chase Helicopter: Headshot Fail" : 65,
    "StD Police Chase Helicopter: Sticky Grenade Fail" : 66,
    "StD Bridge: Do Something Fail" : 67,
    "StD Bridge: Drive Fail" : 68,
    "StD Bridge: Bribe Fail" : 69,
    "StD: Intruder On A Scooter" : 70,
    "ItA Cargo Bay: Zero-Point Energy Fail" : 71,
    "ItA Cargo Bay: Ball 'n' Chain Fail" : 72,
    "ItA Viewing Platform: Bomb Fail" : 73,
    "ItA Viewing Platform: Joy Buzzer Fail" : 74,
    "ItA Viewing Platform: Expanding Foam Fail" : 75,
    "ItA Survalliance Room: Computer Fail" : 76,
    "ItA Survalliance Room: Elevator Fail" : 134,
    "ItA Engine Room Records Side: Stretch Chewies Fail" : 77,
    "ItA Engine Room Records Side: Magic Pencil Fail" : 78,
    "ItA Engine Room Records Side: Teleporter Fail" : 79,
    "ItA Brig: Hack Fail" : 80,
    "ItA Brig: Wizard Magic Fail" : 81,
    "ItA Brig: Retroglove Fail" : 82,
    "ItA Vault: Gravity Manipulator Fail" : 83,
    "ItA Vault: Clawpack Fail" : 84,
    "ItA Outer Wing: Umbrella Fail" : 85,
    "ItA Outer Wing: Propane Tank Fail" : 86,
    "ItA Outer Wing: Shell Fail" : 87,
    "ItA Center For Chaos Containment: D.E.B Fail" : 88,
    "ItA Center For Chaos Containment: L. Cut mk. II Fail" : 89,
    "ItA Center For Chaos Containment: Gaben Fail" : 90,
    "ItA: Pure Blooded Thief":91,
    "ItA Airship Topside: Acid Fail":92,
    "ItA Airship Topside: Knock Fail":93,
    "ItA Airship Topside: C4 Fail":94,
    "ItA Boardroom: Disguise Fail":95,
    "ItA Boardroom: Transdimensionalizer Fail":96,
    "ItA Engine Room Vault Side: Charles Fail":97,
    "ItA Engine Room Vault Side: Gravity Bubble Fail":98,
    "ItA Engine Room Vault Side: Platform Fail":99,
    "ItA Engine Vents: Gatling Gun Fail":100,
    "ItA Engine Vents: Mind Control Fail":101,
    "ItA Engine Vents: Remote Access Fail":102,
    "ItA Records Library: Ninja Star Fail":103,
    "ItA Records Library: Duck Propeller Fail":104,
    "ItA Records Library: Falcon Kick Fail":105,
    "ItA Air Duct: Don't Need Help Fail":106,
    "ItA Air Duct: Shut off Power Fail":107,
    "ItA Cargo Bay Evidence: Banana Bomb Fail":108,
    "ItA Cargo Bay Evidence: Sleeping Gas Fail":109,
    "ItA Cargo Bay Evidence: Flashbang Fail":110,
    "ItA: Government Supported Private Investigator":111,
    "ItA Bridge: Laser Fail":112,
    "ItA Bridge: Thruster Fail":113,
    "ItA Warehouse: Spikes Fail":114,
    "ItA Warehouse: COAL-ossal Fail":115,
    "ItA Warehouse: Boost Fail":116,
    "ItA Quarters Hallway: Warp Fail":117,
    "ItA Quarters Hallway: Metal Fist Fail":118,
    "ItA Quarters Hallway: Doors Fail":119,
    "ItA Brig Damaged: Robo Pants Fail":120,
    "ItA Brig Damaged: Metal Bend Fail":121,
    "ItA Yo-Yo Fight: Bash Fail":122,
    "ItA Yo-Yo Fight: PSI Fail":123,
    "ItA Yo-Yo Fight: Defend Fail":124,
    "ItA Dirk Fight:Fight Fail":125,
    "ItA Dirk Fight: Blitz Fail":126,
    "ItA Dirk Fight: Magic Fail":127,
    "ItA Ventalation Shaft: JetBoots Fail":128,
    "ItA Ventalation Shaft: Beef Up Fail":129,
    "ItA Cargo Bay Hostage: Parachute Fail":130,
    "ItA Cargo Bay Hostage: Missile Fail":131,
    "ItA: Rapidly Promoted Executive":132,
    "ItA: Relentlesss Bounty Hunter":133,
    "FtC Transfer Cell: Play Dead Fail":199,
    "FtC Henry's Cell: Cookie Fail":135,
    "FtC Henry's Cell: Fake Illness Fail":136,
    "FtC Henry's Cell: Teleporter Fail":137,
    "FtC Henry's Cell: Sonic Pulse Fail":138,
    "FtC Cafeteria Toppat: Undercover Agent Fail":139,
    "FtC Cafeteria Toppat: Neurotoxin Fail":140,
    "FtC Airship: Magnet Fail":141,
    "FtC Airship: Slingshot Fail":142,
    "FtC: The Betrayed":167,
    "FtC Cafeteria Government: Earthbend Fail":143,
    "FtC Cafeteria Government: Bubble Shield Fail":144,
    "FtC Fire Escape: Charles Fail":145,
    "FtC Fire Escape: Snipe Fail":146,
    "FtC Helipad: Poor Coordination Fail":147,
    "FtC Helipad: Helicopter Jump Fail":148,
    "FtC Helipad: There Goes Your Ride Fail":149,
    "FtC: International Rescue Operative":168,
    "FtC Transfer Cells Hallway: Terrible Reflexes Fail":150,
    "FtC Transfer Cells Hallway: Hide Fail":151,
    "FtC Transfer Cells Hallway: Speed Shoes Fail":152,
    "FtC Transfer Cells Blockade: Tool Gun Fail":153,
    "FtC Transfer Cells Blockade: Web Throw Fail":154,
    "FtC Transfer Cells Blockade: Speed Loss Fail":155,
    "FtC The Yard Tactical: Tank Fail":156,
    "FtC The Yard Tactical: Boxing Fail":157,
    "FtC The Yard Tactical: Jumpscare Fail":158,
    "FtC Behind The Truck: Sandwich Fail":159,
    "FtC Behind The Truck: Costume Fail":160,
    "FtC Car Chase: Shoot Fail":161,
    "FtC Car Chase: Bail Fail":162,
    "FtC Car Chase: Not Even Close Fail":163,
    "FtC Clifside Wreck: Warp Star Fail":164,
    "FtC Clifside Wreck: Airbag Fail":165,
    "FtC Clifside Wreck: Surrender Fail":166,
    "FtC: Presumed Dead":169,
    "FtC Storage Room Solo: Sprint Fail": 170,
    "FtC Storage Room Solo: Pickpocket Fail": 171,
    "FtC Storage Room Solo: Command Melody Fail": 172,
    "FtC Outside Security Solo: Longshot Fail": 173,
    "FtC Outside Security Solo: Spring Fail": 174,
    "FtC Elevator: Button Fail": 175,
    "FtC Elevator: Bungee Fail": 176,
    "FtC Bowels of the Complex: Plunger Boots Fail": 177,
    "FtC Bowels of the Complex: Balance Fail": 178,
    "FtC Docks: Box Fail": 179,
    "FtC Docks: Shadozer Fail": 180,
    "FtC Outer Docks: S. S. Annie Fail": 181,
    "FtC Outer Docks: Rocket Fail": 182,
    "FtC: Ghost Inmate":195,
    "FtC Storage Room Ellie: Bounce Bros Fail": 183,
    "FtC Storage Room Ellie: Tall Guy Fail": 184,
    "FtC Storage Room Ellie: Distract Fail": 185,
    "FtC Outside Security Ellie: GraviToR v2.0 Fail": 186,
    "FtC Outside Security Ellie: Judo Throw Fail": 187,
    "FtC Hallway Standoff: Crazy Explosion Fail": 188,
    "FtC Hallway Standoff: Instant Replay Fail": 189,
    "FtC Hallway Standoff: Neverrrrr Fail": 190,
    "FtC Two Elevators: Blend In Fail": 191,
    "FtC Two Elevators: Pass By Fail": 192,
    "FtC The Yard Captured: Adrenaline Fail": 193,
    "FtC The Yard Captured: The KNEE Fail": 194,
    "FtC The Yard Escape Route: Truck Fail": 196,
    "FtC The Yard Escape Route: Lemmings Fail": 197,
    "FtC: Convict Allies": 198,
    "CtM Control Tower: Super Punch Fail":200,
    "CtM Control Tower: Very Accurate Targetting System Fail":201,
    "CtM Inside Helicopter: Abandon Fail":202,
    "CtM Inside Helicopter: Helicopter Fail":203,
    "CtM Under The Rocket: Revolver Fail":204,
    "CtM Under The Rocket: Boomerang Fail":205,
    "CtM Back To Back: Charge Fail":206,
    "CtM Back To Back: Summon Fail":207,
    "CtM Back To Back: Style on 'em Fail":208,
    "CtM Driving Up the Ramp: Ellie Fail":209,
    "CtM Driving Up the Ramp: Right Hand Man Fail":210,
    "CtM Driving Up the Ramp: Seatbelts Fail":211,
    "CtM Left Behind: Cloud Fail":212,
    "CtM Left Behind: G-Inverter Fail":213,
    "CtM: Toppat King":214,
    "CtM Orbital Cell: Remote Fail":215,
    "CtM Orbital Cell: Inner Strength Fail":216,
    "CtM Orbital Cell Still: Lockpick Fail":217,
    "CtM Orbital Cell Still: Melt Ray Fail":218,
    "CtM Orbital Cell Still: Bomb Fail":219,
    "CtM Choose Your Weapon: Big Sword Fail":220,
    "CtM Choose Your Weapon: Underbarel Grenade Launcher Fail":221,
    "CtM Cafeteria Space: Harden Fail":222,
    "CtM Cafeteria Space: Sweep The Legs Fail":223,
    "CtM Solar Panel Dash: Instruction Manual Fail":224,
    "CtM Solar Panel Dash: Fire Missiles Fail":225,
    "CtM Solar Panel Dash: Positron Reflector Fail":226,
    "CtM Escape Plan: Comunications Satalite Fail":227,
    "CtM Escape Plan: Earth Fail":228,
    "CtM Escape Plan: Towards Enemy Fail":229,
    "CtM Free Man":230,
    "CtM Sam Turret Roof: Cupcake Fail":231,
    "CtM Sam Turret Roof: Panel Fail":232,
    "CtM Sam Turret Roof: Stomp Fail":233,
    "CtM Cross Over: JetPod Fail":234,
    "CtM Cross Over: Invisible Bridge Fail":235,
    "CtM Storage Bay Charles: TV Broadcast Fail":236,
    "CtM Storage Bay Charles: Subsonic Wave Fail":237,
    "CtM Engine Room: Wrench Fail":238,
    "CtM Engine Room: Power Button Fail":239,
    "CtM Hall Of Leaders: Painting Portal Fail":240,
    "CtM Hall Of Leaders: Bug Juice Fail":241,
    "CtM Cockpit: IR Sniper Fail":242,
    "CtM Cockpit: Sleep Dart Fail":243,
    "CtM: Special BROvert Ops":244,
    "CtM Where We Droppin: Parking Lot Fail":245,
    "CtM Where We Droppin: Control Tower Fail":246,
    "CtM Where We Droppin: Rocket Entrance Fail":247,
    "CtM Rocket Boarding Last Call: Build Fail":248,
    "CtM Rocket Boarding Last Call: Climb Down and Run Fail":249,
    "CtM Rocket Boarding Last Call: Throw Fail":250,
    "CtM Combo Time: Net Fail":251,
    "CtM Combo Time: Hand Fail":252,
    "CtM Combo Time: Came Out Of Nowhere Fail":253,
    "CtM Cafeteria Jungle: Downgrader Fail":254,
    "CtM Cafeteria Jungle: Fusion Fail":255,
    "CtM Improvise a Plan: Charles' Plan Fail":256,
    "CtM Improvise a Plan: Ellie's Plan Fail":257,
    "CtM: Triple Threat":258,
    "CtM Jungle Trail: Limbo Fail":259,
    "CtM Jungle Trail: Jump Fail":260,
    "CtM Jungle Trail: Good Start Fail":261,
    "CtM Onramp: Ramp Fail":262,
    "CtM Onramp: Item Crate Fail":263,
    "CtM Closed Entrance: Battering Ram Fail":265,
    "CtM Closed Entrance: Drill Fail":266,
    "CtM Closed Entrance: Lag Fail":267,
    "CtM Top of the Rocket: First Try Fail":268,
    "CtM Top of the Rocket: Hammer Yourself Fail":269,
    "CtM Top of the Rocket: 95 More Hits Fail":270,
    "CtM Tethered: Stage Fail":271,
    "CtM Tethered: Full Speed Fail":272,
    "CtM Tethered: Return to Sender Fail":273,
    "CtM: Stickmin Space Resort":274,
    "CtM Space Scooter: Barrel Roll Fail":275,
    "CtM Space Scooter: Straight Fail":276,
    "CtM Space Scooter: Light Speed Fail":277,
    "CtM Gravity Pit: Leap Fail":278,
    "CtM Gravity Pit: Pole Vault Fail":279,
    "CtM Gravity Pit: Catapult Fail":280,
    "CtM Gravity Pit: Ramp Fail":281,
    "CtM Gravity Pit: Rocket Fail":282,
    "CtM Gravity Pit: Bridge Fail":283,
    "CtM Gravity Pit: Cannon Fail":284,
    "CtM Station Vault: Eject Fail":285,
    "CtM Station Vault: Wallclip Fail":286,
    "CtM Station Vault: SMASH Fail":287,
    "CtM Gamma Lounge: Emerald Fail":288,
    "CtM Gamma Lounge: Chance Time Fail":289,
    "CtM Secret Weapon: Super Henry Fail":290,
    "CtM: Jewel Baron":291,
    "CtM Tank Attack: Fire Fail":292,
    "CtM Tank Attack: Join the Caravan Fail":293,
    "CtM Traintop Sprint: Bullet Time Fail":294,
    "CtM Traintop Sprint: Inside Fail":295,
    "CtM Traintop Sprint: Commandeer Fail":296,
    "CtM Conductor Battle: Fight Fail":297,
    "CtM Conductor Battle: Act Fail":298,
    "CtM Conductor Battle: Mercy Fail":299,
    "CtM Getaway Means: By Air Fail":300,
    "CtM Getaway Means: By Land Fail":301,
    "CtM: Little Nest Egg":302,
    "CtM Parking Lot: Very Cool Fail":303,
    "CtM Parking Lot: Wrong Type Fail":304,
    "CtM Parking Lot: What Plan Fail":305,
    "CtM Launch Tower Hallway: CorrupTick Fail":306,
    "CtM Launch Tower Hallway: Disguise Kit Fail":307,
    "CtM Collapse: Henry 7 Fail":308,
    "CtM Collapse: Grapple Fail":309,
    "CtM Collapse: Catch Fail":310,
    "CtM Faction Friction: The Wall Fail":311,
    "CtM Faction Friction: None Fail":312,
    "CtM: Pardoned Pals":313,
    "CtM: Toppat Recruits":314,
    "CtM Cliffside: Rope Fail":315,
    "CtM Cliffside: Climb Fail":316,
    "CtM The Watchtower: Knife Fail":317,
    "CtM The Watchtower: Duplicatorange Fail":318,
    "CtM Big Boy: Walkthrough Fail":319,
    "CtM Big Boy: Hijack Fail":320,
    "CtM CCC Mobile Unit: Ultimate Freeze Fail":321,
    "CtM CCC Mobile Unit: Moon Fail":322,
    "CtM CCC Mobile Unit: Nuclear Bomb Fail":323,
    "CtM: Toppat 4 Life":324,
    "CtM Cargo Stopped: Toppat Box Fail":325,
    "CtM Cargo Stopped: Prop Fail":326,
    "CtM Passenger Car: Mannequin Fail":327,
    "CtM Passenger Car: Sit Fail":328,
    "CtM Top of the Train: Window Fail":329,
    "CtM Top of the Train: Pincher Fail":380,
    "CtM Top of the Train: Last Stop Fail":330,
    "CtM Storage Bay: Leafmode Fail":331,
    "CtM Storage Bay: Infini3 Fail":332,
    "CtM: Cleaned 'em Out":333,
    "CtM Front Gate: Close-Quarters Combat Fail":334,
    "CtM Front Gate: Stealth Fail":335,
    "CtM Front Gate: Dance-Off Fail":336,
    "CtM Doorway: Cluster Charge Fail":337,
    "CtM Doorway: Dogpile Fail":338,
    "CtM Doorway: Dance-Off Fail":339,
    "CtM Face to Face: Dance-Off Fail":340,
    "CtM Face to Face: Rock Paper Scissors Fail":341,
    "CtM Face to Face: Self-Destruct Fail":342,
    "CtM Bounty's Fate: Dance-Off Fail":343,
    "CtM Bounty's Fate: Finish Him Fail":344,
    "CtM Bounty's Fate: Rewire Fail":345,
    "CtM: Master Bounty Hunter":346,
    "CtM Infiltrating the Orbital Station: Air Cannon Fail":347,
    "CtM Infiltrating the Orbital Station: Drop Off Fail":348,
    "CtM Infiltrating the Orbital Station: Beam Aboard Fail":349,
    "CtM Orbital Hull: Super Accurate Lase Shot Fail":350,
    "CtM Orbital Hull: Hot Knife Fail":351,
    "CtM Door's Stuck!: Lift Fail":352,
    "CtM Door's Stuck!: Hack Fail":353,
    "CtM Escape Pods: Luxury Fail":354,
    "CtM Escape Pods: Reverse Thruster Fail":355,
    "CtM: Valliant Hero":356,
    "CtM The Plank: Chainsaw Fail":357,
    "CtM The Plank: Plead Fail":358,
    "CtM The Plank: Save State Fail":359,
    "CtM The Brig: Toppy Fail":360,
    "CtM The Brig: Mind Crystal Fail":361,
    "CtM A Few Ideas: The Good Gents Fail":362,
    "CtM A Few Ideas: Midnight Surprise Fail":363,
    "CtM: Toppat Civil Warfare":364,
    "CtM Train Assault: Swords Fail":365,
    "CtM Train Assault: Hunker Fail":366,
    "CtM Train Assault: Don't Stop Fail":367,
    "CtM Crash Site: Purse of Holding Fail":368,
    "CtM Crash Site: Force Lift Fail":369,
    "CtM The Floating Cart: Needle Fail":370,
    "CtM The Floating Cart: Shell Bounce Fail":371,
    "CtM: Capital Gains":372,
    "CtM Showdown: Spirit Forme Fail":373,
    "CtM Showdown: Gun Forme Fail":374,
    "CtM Finishing Move: Absorb Fail":375,
    "CtM Finishing Move: Baseball Bat Fail":376,
    "CtM Claim Revenge: Airship Fail":377,
    "CtM Claim Revenge: Drop Fail":378,
    "CtM: Revenged":379,
    "EtP Bathroom: Opacitator Donut":381,
    "EtP Closet: Break Room Donut 1":382,
    "EtP Closet: Break Room Donut 2":383,
    "EtP Closet: Break Room Donut 3":384,
    "EtP Cell: NRGDrink Donut":385,


}


class HenryStickminLocation(Location):
    game = "Henry Stickmin"


def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: HenryStickminWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def set_locations_for_region(world,regionName,locations):
    region = world.get_region(regionName)
    locations = get_location_names_with_ids(locations)
    region.add_locations(locations,HenryStickminLocation)

def create_regular_locations(world: HenryStickminWorld) -> None:

    if (use_BtB(world)):
        set_locations_for_region(world,"btbIntro",["BtB Bank: Shovel Fail", "BtB Bank: Explosives Fail", "BtB Bank: Teleporter Fail", "BtB Bank: Laser Fail", "BtB Bank: Wrecking Ball Fail", "BtB: The Story Begins"])

    if (use_EtP(world)):
        set_locations_for_region(world,"etpCell",["EtP Cell: Nrg Drink Fail", "EtP Cell: Teleporter Fail", "EtP Cell: Rocket Launcher Fail"])

        set_locations_for_region(world,"etpCourtroom",["EtP Courtroom: Declared Guilty Fail", "EtP: Lawyered Up"])
        
        set_locations_for_region(world,"etpCloset",["EtP Cell: File Window Fail", "EtP Cell Block: Rupert Kick Fail", "EtP Cell Block: Dave Taser Fail", "EtP Closet: Belt of Grenades Fail", "EtP Closet: Broken Pipe Fail"])
        set_locations_for_region(world,"etpRooftop",["EtP Rooftop: Rope Fail", "EtP Rooftop: Parachute Fail", "EtP Rooftop: JetPack Fail", "EtP: Sneaky Escapist"])
        
        set_locations_for_region(world,"etpBathroom",["EtP Bathroom: Opacitator Fail"])
        set_locations_for_region(world,"etpLobby",["EtP Back Lobby: Pillar Fail", "EtP Back Lobby: Shot Fail", "EtP Lobby Turn: Brawl Fail", "EtP Lobby Turn: Crash Fail: ", "EtP Prison Entrance: Quicktime event Fail", "EtP: Baddass Bust Out"])

    if (use_StD(world)):
        set_locations_for_region(world,"stdLookout",["StD Outer Wall: Liquidificator Fail", "StD Outer Wall: Shrink Ray Fail","StD Outer Wall: Anti-Gravity Cap Fail","StD Outer Wall: Jumble Hoppers Fail","StD Parking Lot: Kick Fail","StD Parking Lot: Jump Fail","StD Parking Lot: Great Start Fail","StD Medieval Hall: Lance Fail","StD Medieval Hall: Flail Fail","StD Medieval Hall: Janitor Fail"])
        
        set_locations_for_region(world,"stdDiamondExhibitScooter",["StD Diamond Exhibit (Scooter): Basket Fail","StD Diamond Exhibit (Scooter): Stand Around Fail"])
        set_locations_for_region(world,"stdPoliceChaseCar",["StD Police Chase Car: Reflexes Fail","StD Police Chase Car: Branch Fail"])
        set_locations_for_region(world,"stdPoliceChaseHeli",["StD Police Chase Helicopter: Headshot Fail","StD Police Chase Helicopter: Sticky Grenade Fail"])
        set_locations_for_region(world,"stdBridge",["StD Bridge: Do Something Fail","StD Bridge: Drive Fail","StD Bridge: Bribe Fail","StD: Intruder On A Scooter"])
        
        set_locations_for_region(world,"stdRooftop",["StD Rooftop: Falcon Punch Fail","StD Rooftop: Tranquilizer Fail","StD Rooftop: Invisibility Pill Fail"])
        set_locations_for_region(world,"stdCatwalk",["StD Catwalk: Drop Fail","StD Catwalk: Wormhole Rifle Fail"])
        set_locations_for_region(world,"stdDiamondExhibit",["StD Diamond Exhibit: Laser Cutter Fail"])
        set_locations_for_region(world,"stdStorageRoom",["StD Storage Room: Cannon Fail","StD Storage Room: Cheese Fail"])
        set_locations_for_region(world,"stdBackdoor",["StD Backdoor: Snap Neck Fail","StD Backdoor: Rifle Fail","StD Backdoor: Jump Fail","StD: Unseen Burglar"])
        
        set_locations_for_region(world,"stdWW2Exhibit",["StD WW2 Exhibit: Dave Conversation Fail","StD WW2 Exhibit: Bomb Fail","StD WW2 Exhibit: Gun Fail"])
        set_locations_for_region(world,"stdRetroExhibit",["StD Diamond Exhibit Entrance: Light Sleeper Fail","StD Retro Exhibit: Alien Fail","StD Retro Exhibit: Goodball Fail","StD Retro Exhibit: Crowbar Fail"])
        set_locations_for_region(world,"stdCenterForChaosContainment",["StD Center For Chaos Containment: Nuclear Bomb Fail","StD Center For Chaos Containment: Divide by Zero Fail","StD Center For Chaos Containment: Shoop da Whoop Fail","StD: Just Plain Epic"])
        
    if (use_ItA(world)):
        set_locations_for_region(world,"itaCargoBay",["ItA Cargo Bay: Zero-Point Energy Fail","ItA Cargo Bay: Ball 'n' Chain Fail"])
        
        set_locations_for_region(world,"itaViewingPlatform",["ItA Viewing Platform: Bomb Fail","ItA Viewing Platform: Joy Buzzer Fail","ItA Viewing Platform: Expanding Foam Fail", "ItA Survalliance Room: Computer Fail","ItA Survalliance Room: Elevator Fail", "ItA Engine Room Records Side: Stretch Chewies Fail","ItA Engine Room Records Side: Magic Pencil Fail","ItA Engine Room Records Side: Teleporter Fail","ItA Brig: Hack Fail","ItA Brig: Wizard Magic Fail","ItA Brig: Retroglove Fail"])
        set_locations_for_region(world,"itaVault",["ItA Vault: Gravity Manipulator Fail","ItA Vault: Clawpack Fail"])
        set_locations_for_region(world,"itaOuterWing",["ItA Outer Wing: Umbrella Fail","ItA Outer Wing: Propane Tank Fail","ItA Outer Wing: Shell Fail"])
        set_locations_for_region(world,"itaCenterForChaosContainment",["ItA Center For Chaos Containment: D.E.B Fail","ItA Center For Chaos Containment: L. Cut mk. II Fail","ItA Center For Chaos Containment: Gaben Fail","ItA: Pure Blooded Thief"])

        set_locations_for_region(world,"itaAirshipTopside",["ItA Airship Topside: Acid Fail","ItA Airship Topside: Knock Fail","ItA Airship Topside: C4 Fail"])
        set_locations_for_region(world,"itaBoardroom",["ItA Boardroom: Disguise Fail","ItA Boardroom: Transdimensionalizer Fail"])
        set_locations_for_region(world,"itaEngineRoomVaultSide",["ItA Engine Room Vault Side: Charles Fail","ItA Engine Room Vault Side: Gravity Bubble Fail","ItA Engine Room Vault Side: Platform Fail"])
        set_locations_for_region(world,"itaEngineVents",["ItA Engine Vents: Gatling Gun Fail","ItA Engine Vents: Mind Control Fail","ItA Engine Vents: Remote Access Fail"])
        set_locations_for_region(world,"itaRecordsLibrary",["ItA Records Library: Ninja Star Fail","ItA Records Library: Duck Propeller Fail","ItA Records Library: Falcon Kick Fail"])
        set_locations_for_region(world,"itaAirDuct",["ItA Air Duct: Don't Need Help Fail","ItA Air Duct: Shut off Power Fail","ItA Cargo Bay Evidence: Banana Bomb Fail","ItA Cargo Bay Evidence: Sleeping Gas Fail","ItA Cargo Bay Evidence: Flashbang Fail","ItA: Government Supported Private Investigator"])

        set_locations_for_region(world,"itaBridge",["ItA Bridge: Laser Fail","ItA Bridge: Thruster Fail"])
        set_locations_for_region(world,"itaWarehouse",["ItA Warehouse: Spikes Fail","ItA Warehouse: COAL-ossal Fail","ItA Warehouse: Boost Fail"])
        set_locations_for_region(world,"itaQuartersHallway",["ItA Quarters Hallway: Warp Fail","ItA Quarters Hallway: Metal Fist Fail","ItA Quarters Hallway: Doors Fail"])
        set_locations_for_region(world,"itaBrigDamaged",["ItA Brig Damaged: Robo Pants Fail","ItA Brig Damaged: Metal Bend Fail"])
        set_locations_for_region(world,"itaShowdownFF",["ItA Dirk Fight:Fight Fail","ItA Dirk Fight: Blitz Fail","ItA Dirk Fight: Magic Fail"])
        set_locations_for_region(world,"itaShowdownEB",["ItA Yo-Yo Fight: Bash Fail","ItA Yo-Yo Fight: PSI Fail","ItA Yo-Yo Fight: Defend Fail"])
        set_locations_for_region(world,"itaVentalationShaft",["ItA Ventalation Shaft: JetBoots Fail","ItA Ventalation Shaft: Beef Up Fail"])
        set_locations_for_region(world,"itaCargoBayHostage",["ItA Cargo Bay Hostage: Parachute Fail","ItA Cargo Bay Hostage: Missile Fail","ItA: Rapidly Promoted Executive","ItA: Relentlesss Bounty Hunter"])
    
    if (use_FtC(world)):
        set_locations_for_region(world,"ftcTransferCell",["FtC Transfer Cell: Play Dead Fail","FtC Henry's Cell: Cookie Fail","FtC Henry's Cell: Fake Illness Fail","FtC Henry's Cell: Teleporter Fail","FtC Henry's Cell: Sonic Pulse Fail","FtC Transfer Cells Hallway: Terrible Reflexes Fail","FtC Transfer Cells Hallway: Hide Fail","FtC Transfer Cells Hallway: Speed Shoes Fail","FtC Transfer Cells Blockade: Tool Gun Fail","FtC Transfer Cells Blockade: Web Throw Fail","FtC Transfer Cells Blockade: Speed Loss Fail","FtC Storage Room Solo: Sprint Fail","FtC Storage Room Solo: Pickpocket Fail","FtC Storage Room Solo: Command Melody Fail","FtC Storage Room Ellie: Bounce Bros Fail","FtC Storage Room Ellie: Tall Guy Fail","FtC Storage Room Ellie: Distract Fail","FtC Outside Security Ellie: GraviToR v2.0 Fail","FtC Outside Security Ellie: Judo Throw Fail"])

        set_locations_for_region(world,"ftcTheYardTactical",["FtC The Yard Tactical: Tank Fail","FtC The Yard Tactical: Boxing Fail","FtC The Yard Tactical: Jumpscare Fail"])
        set_locations_for_region(world,"ftcBehindTheTruck",["FtC Behind The Truck: Sandwich Fail","FtC Behind The Truck: Costume Fail"])
        set_locations_for_region(world,"ftcCarChase",["FtC Car Chase: Shoot Fail","FtC Car Chase: Bail Fail","FtC Car Chase: Not Even Close Fail","FtC Clifside Wreck: Warp Star Fail","FtC Clifside Wreck: Airbag Fail","FtC Clifside Wreck: Surrender Fail","FtC: Presumed Dead"])

        set_locations_for_region(world,"ftcCafeteriaGovernment",["FtC Cafeteria Government: Earthbend Fail","FtC Cafeteria Government: Bubble Shield Fail"])
        set_locations_for_region(world,"ftcFireEscape",["FtC Fire Escape: Charles Fail","FtC Fire Escape: Snipe Fail"])
        set_locations_for_region(world,"ftcHelipad",["FtC Helipad: Poor Coordination Fail","FtC Helipad: Helicopter Jump Fail","FtC Helipad: There Goes Your Ride Fail","FtC: International Rescue Operative"])

        set_locations_for_region(world,"ftcCafeteriaToppat",["FtC Cafeteria Toppat: Undercover Agent Fail","FtC Cafeteria Toppat: Neurotoxin Fail"])
        set_locations_for_region(world,"ftcAirship",["FtC Airship: Magnet Fail","FtC Airship: Slingshot Fail","FtC: The Betrayed"])

        set_locations_for_region(world,"ftcOutsideSecuritySolo",["FtC Outside Security Solo: Longshot Fail","FtC Outside Security Solo: Spring Fail"])
        set_locations_for_region(world,"ftcElevator",["FtC Elevator: Button Fail","FtC Elevator: Bungee Fail"])
        set_locations_for_region(world,"ftcBowelsOfTheComplex",["FtC Bowels of the Complex: Plunger Boots Fail","FtC Bowels of the Complex: Balance Fail"])
        set_locations_for_region(world,"ftcDocks",["FtC Docks: Box Fail","FtC Docks: Shadozer Fail"])
        set_locations_for_region(world,"ftcOuterDocks",["FtC Outer Docks: S. S. Annie Fail","FtC Outer Docks: Rocket Fail","FtC: Ghost Inmate"])

        set_locations_for_region(world,"ftcHallwayStandoff",["FtC Hallway Standoff: Crazy Explosion Fail","FtC Hallway Standoff: Instant Replay Fail","FtC Hallway Standoff: Neverrrrr Fail"])
        set_locations_for_region(world,"ftcTwoElevators",["FtC Two Elevators: Blend In Fail","FtC Two Elevators: Pass By Fail"])
        set_locations_for_region(world,"ftcTheYardCaptured",["FtC The Yard Captured: Adrenaline Fail","FtC The Yard Captured: The KNEE Fail","FtC The Yard Escape Route: Truck Fail","FtC The Yard Escape Route: Lemmings Fail","FtC: Convict Allies"])

    if (use_CtM(world)):
        set_locations_for_region(world,"ctmControlTower",["CtM Control Tower: Super Punch Fail","CtM Control Tower: Very Accurate Targetting System Fail"])
        set_locations_for_region(world,"ctmInsideHelicopter",["CtM Inside Helicopter: Abandon Fail","CtM Inside Helicopter: Helicopter Fail"])
        set_locations_for_region(world,"ctmUnderTheRocket",["CtM Under The Rocket: Revolver Fail","CtM Under The Rocket: Boomerang Fail"])
        set_locations_for_region(world,"ctmBackToBack",["CtM Back To Back: Charge Fail","CtM Back To Back: Summon Fail","CtM Back To Back: Style on 'em Fail"])
        set_locations_for_region(world,"ctmDrivingUpTheRamp",["CtM Driving Up the Ramp: Ellie Fail","CtM Driving Up the Ramp: Right Hand Man Fail","CtM Driving Up the Ramp: Seatbelts Fail","CtM Left Behind: Cloud Fail","CtM Left Behind: G-Inverter Fail","CtM: Toppat King"])

        set_locations_for_region(world,"ctmOrbitalCell",["CtM Orbital Cell: Remote Fail","CtM Orbital Cell: Inner Strength Fail"])
        set_locations_for_region(world,"ctmOrbitalCellStill",["CtM Orbital Cell Still: Lockpick Fail","CtM Orbital Cell Still: Melt Ray Fail","CtM Orbital Cell Still: Bomb Fail"])
        set_locations_for_region(world,"ctmChooseYourWeapon",["CtM Choose Your Weapon: Big Sword Fail","CtM Choose Your Weapon: Underbarel Grenade Launcher Fail"])
        set_locations_for_region(world,"ctmCafeteriaSpace",["CtM Cafeteria Space: Harden Fail","CtM Cafeteria Space: Sweep The Legs Fail"])
        set_locations_for_region(world,"ctmSolarPanelDash",["CtM Solar Panel Dash: Instruction Manual Fail","CtM Solar Panel Dash: Fire Missiles Fail","CtM Solar Panel Dash: Positron Reflector Fail"])
        set_locations_for_region(world,"ctmEscapePlan",["CtM Escape Plan: Comunications Satalite Fail","CtM Escape Plan: Earth Fail","CtM Escape Plan: Towards Enemy Fail","CtM Free Man"])

        set_locations_for_region(world,"ctmSAMTurretRoof",["CtM Sam Turret Roof: Cupcake Fail","CtM Sam Turret Roof: Panel Fail","CtM Sam Turret Roof: Stomp Fail"])
        set_locations_for_region(world,"ctmCrossOver",["CtM Cross Over: JetPod Fail","CtM Cross Over: Invisible Bridge Fail"])
        set_locations_for_region(world,"ctmStorageBayCharles",["CtM Storage Bay Charles: TV Broadcast Fail","CtM Storage Bay Charles: Subsonic Wave Fail"])
        set_locations_for_region(world,"ctmEngineRoom",["CtM Engine Room: Wrench Fail","CtM Engine Room: Power Button Fail"])
        set_locations_for_region(world,"ctmHallOfLeaders",["CtM Hall Of Leaders: Painting Portal Fail","CtM Hall Of Leaders: Bug Juice Fail"])
        set_locations_for_region(world,"ctmCockpit",["CtM Cockpit: IR Sniper Fail","CtM Cockpit: Sleep Dart Fail","CtM: Special BROvert Ops"])

        set_locations_for_region(world,"ctmWhereWeDroppin",["CtM Where We Droppin: Parking Lot Fail","CtM Where We Droppin: Control Tower Fail","CtM Where We Droppin: Rocket Entrance Fail"])
        set_locations_for_region(world,"ctmRocketBoardingLastCall",["CtM Rocket Boarding Last Call: Build Fail","CtM Rocket Boarding Last Call: Climb Down and Run Fail","CtM Rocket Boarding Last Call: Throw Fail"])
        set_locations_for_region(world,"ctmComboTime",["CtM Combo Time: Net Fail","CtM Combo Time: Hand Fail","CtM Combo Time: Came Out Of Nowhere Fail"])
        set_locations_for_region(world,"ctmCafeteriaJungle",["CtM Cafeteria Jungle: Downgrader Fail","CtM Cafeteria Jungle: Fusion Fail","CtM Improvise a Plan: Charles' Plan Fail","CtM Improvise a Plan: Ellie's Plan Fail","CtM: Triple Threat"])

        set_locations_for_region(world,"ctmJungleTrail",["CtM Jungle Trail: Limbo Fail","CtM Jungle Trail: Jump Fail","CtM Jungle Trail: Good Start Fail","CtM Onramp: Ramp Fail","CtM Onramp: Item Crate Fail","CtM Closed Entrance: Battering Ram Fail","CtM Closed Entrance: Drill Fail","CtM Closed Entrance: Lag Fail"])
        set_locations_for_region(world,"ctmTopOfTheRocket",["CtM Top of the Rocket: First Try Fail","CtM Top of the Rocket: Hammer Yourself Fail","CtM Top of the Rocket: 95 More Hits Fail"])
        set_locations_for_region(world,"ctmTethered",["CtM Tethered: Stage Fail","CtM Tethered: Full Speed Fail","CtM Tethered: Return to Sender Fail","CtM: Stickmin Space Resort"])

        set_locations_for_region(world,"ctmSpaceScooter",["CtM Space Scooter: Barrel Roll Fail","CtM Space Scooter: Straight Fail","CtM Space Scooter: Light Speed Fail"])
        set_locations_for_region(world,"ctmGravityPit",["CtM Gravity Pit: Leap Fail","CtM Gravity Pit: Pole Vault Fail","CtM Gravity Pit: Catapult Fail","CtM Gravity Pit: Ramp Fail","CtM Gravity Pit: Rocket Fail","CtM Gravity Pit: Bridge Fail","CtM Gravity Pit: Cannon Fail"])
        set_locations_for_region(world,"ctmStationVault",["CtM Station Vault: Eject Fail","CtM Station Vault: Wallclip Fail","CtM Station Vault: SMASH Fail","CtM Gamma Lounge: Emerald Fail","CtM Gamma Lounge: Chance Time Fail"])
        set_locations_for_region(world,"ctmSecretWeapon",["CtM Secret Weapon: Super Henry Fail","CtM: Jewel Baron"])
       
        set_locations_for_region(world,"ctmTankAttack",["CtM Tank Attack: Fire Fail","CtM Tank Attack: Join the Caravan Fail"])
        set_locations_for_region(world,"ctmTraintopSprint",["CtM Traintop Sprint: Bullet Time Fail","CtM Traintop Sprint: Inside Fail","CtM Traintop Sprint: Commandeer Fail","CtM Conductor Battle: Fight Fail","CtM Conductor Battle: Act Fail","CtM Conductor Battle: Mercy Fail"])
        set_locations_for_region(world,"ctmGetawayMeans",["CtM Getaway Means: By Air Fail","CtM Getaway Means: By Land Fail","CtM: Little Nest Egg"])

        set_locations_for_region(world,"ctmParkingLot",["CtM Parking Lot: Very Cool Fail","CtM Parking Lot: Wrong Type Fail","CtM Parking Lot: What Plan Fail"])
        set_locations_for_region(world,"ctmLaunchTowerHallway",["CtM Launch Tower Hallway: CorrupTick Fail","CtM Launch Tower Hallway: Disguise Kit Fail"])
        set_locations_for_region(world,"ctmCollapse",["CtM Collapse: Henry 7 Fail","CtM Collapse: Grapple Fail","CtM Collapse: Catch Fail"])
        set_locations_for_region(world,"ctmFactionFriction",["CtM Faction Friction: The Wall Fail","CtM Faction Friction: None Fail","CtM: Pardoned Pals","CtM: Toppat Recruits"])

        set_locations_for_region(world,"ctmCliffside",["CtM Cliffside: Rope Fail","CtM Cliffside: Climb Fail"])
        set_locations_for_region(world,"ctmTheWatchtower",["CtM The Watchtower: Knife Fail","CtM The Watchtower: Duplicatorange Fail"])
        set_locations_for_region(world,"ctmBigBoy",["CtM Big Boy: Walkthrough Fail","CtM Big Boy: Hijack Fail"])
        set_locations_for_region(world,"ctmCCCMobileUnit",["CtM CCC Mobile Unit: Ultimate Freeze Fail","CtM CCC Mobile Unit: Moon Fail","CtM CCC Mobile Unit: Nuclear Bomb Fail","CtM: Toppat 4 Life"])

        set_locations_for_region(world,"ctmCargoStopped",["CtM Cargo Stopped: Toppat Box Fail","CtM Cargo Stopped: Prop Fail"])
        set_locations_for_region(world,"ctmPassangerCar",["CtM Passenger Car: Mannequin Fail","CtM Passenger Car: Sit Fail","CtM Top of the Train: Window Fail","CtM Top of the Train: Last Stop Fail","CtM Top of the Train: Pincher Fail"])
        set_locations_for_region(world,"ctmStorageBay",["CtM Storage Bay: Leafmode Fail","CtM Storage Bay: Infini3 Fail","CtM: Cleaned 'em Out"])

        set_locations_for_region(world,"ctmFrontGate",["CtM Front Gate: Close-Quarters Combat Fail","CtM Front Gate: Stealth Fail","CtM Front Gate: Dance-Off Fail"])
        set_locations_for_region(world,"ctmDoorway",["CtM Doorway: Cluster Charge Fail","CtM Doorway: Dogpile Fail","CtM Doorway: Dance-Off Fail","CtM Face to Face: Dance-Off Fail","CtM Face to Face: Rock Paper Scissors Fail","CtM Face to Face: Self-Destruct Fail"])
        set_locations_for_region(world,"ctmBountysFate",["CtM Bounty's Fate: Dance-Off Fail","CtM Bounty's Fate: Finish Him Fail","CtM Bounty's Fate: Rewire Fail","CtM: Master Bounty Hunter"])

        set_locations_for_region(world,"ctmInfiltratingTheOrbitalStation",["CtM Infiltrating the Orbital Station: Air Cannon Fail","CtM Infiltrating the Orbital Station: Drop Off Fail","CtM Infiltrating the Orbital Station: Beam Aboard Fail"])
        set_locations_for_region(world,"ctmOrbitalHull",["CtM Orbital Hull: Super Accurate Lase Shot Fail","CtM Orbital Hull: Hot Knife Fail","CtM Door's Stuck!: Lift Fail","CtM Door's Stuck!: Hack Fail","CtM Escape Pods: Luxury Fail","CtM Escape Pods: Reverse Thruster Fail","CtM: Valliant Hero"])
        
        set_locations_for_region(world,"ctmThePlank",["CtM The Plank: Chainsaw Fail","CtM The Plank: Plead Fail","CtM The Plank: Save State Fail"])
        set_locations_for_region(world,"ctmTheBrig",["CtM The Brig: Toppy Fail","CtM The Brig: Mind Crystal Fail","CtM A Few Ideas: The Good Gents Fail","CtM A Few Ideas: Midnight Surprise Fail","CtM: Toppat Civil Warfare"])

        set_locations_for_region(world,"ctmTrainAssault",["CtM Train Assault: Swords Fail","CtM Train Assault: Hunker Fail","CtM Train Assault: Don't Stop Fail"])
        set_locations_for_region(world,"ctmCrashSite",["CtM Crash Site: Purse of Holding Fail","CtM Crash Site: Force Lift Fail"])
        set_locations_for_region(world,"ctmFloatingCart",["CtM The Floating Cart: Needle Fail","CtM The Floating Cart: Shell Bounce Fail","CtM: Capital Gains"])

        set_locations_for_region(world,"ctmShowdown",["CtM Showdown: Spirit Forme Fail","CtM Showdown: Gun Forme Fail"])
        set_locations_for_region(world,"ctmFinishingMove",["CtM Finishing Move: Absorb Fail","CtM Finishing Move: Baseball Bat Fail"])
        set_locations_for_region(world,"ctmClaimRevenge",["CtM Claim Revenge: Airship Fail","CtM Claim Revenge: Drop Fail","CtM: Revenged"])



def create_rank_event(world,region,name,rule=None):
    region = world.get_region(region)
    event_location = HenryStickminLocation(world.player, f"{name} Event", None, region)
    region.locations.append(event_location)

    if (rule is not None):
        world.set_rule(event_location,rule)

    event_item = HenryStickminItem(f"{name} Event Item",ItemClassification.progression,None,world.player)
    event_location.place_locked_item(event_item)
    pass


def create_events(world: HenryStickminWorld) -> None:

    # Copy of rank locations as event locations to use for goal checking
    if (use_BtB(world)):
        create_rank_event(world,"btbIntro","Story Begins",Has("Money Bag Disguise"))


    if (use_EtP(world)):
        create_rank_event(world,"etpCourtroom","Lawyered Up",Has("Money Bag Disguise"))
        create_rank_event(world,"etpRooftop","Sneaky Escapist",Has("Plungers"))
        create_rank_event(world,"etpLobby","Badass Bust Out")

    if (use_StD(world)):
        create_rank_event(world,"stdBackdoor","Unseen Burglar",Has("Tunisian Diamond"))
        create_rank_event(world,"stdBridge","Intruder On A Scooter",Has("Tunisian Diamond"))
        create_rank_event(world,"stdCenterForChaosContainment","Just Plain Epic",Has("Giant CCC Robot"))
    
    if (use_ItA(world)):
        create_rank_event(world,"itaCargoBayHostage","Rapidly Promoted Executive",Has("Dummies"))
        create_rank_event(world,"itaCargoBayHostage","Relentless Bounty Hunter",Has("Tank"))
        create_rank_event(world,"itaCenterForChaosContainment","Pure Blooded Thief",Has("Prototype Disk"))
        create_rank_event(world,"itaAirDuct","Government Supported Private Investigator",Has("Force Gun"))

    if (use_FtC(world)):
        create_rank_event(world,"ftcCarChase","Presumed Dead")
        create_rank_event(world,"ftcHelipad","International Rescue Operative")
        create_rank_event(world,"ftcAirship","The Betrayed",Has("Sick Ride"))
        create_rank_event(world,"ftcOuterDocks","Ghost Inmate",Has("Dinghy"))
        create_rank_event(world,"ftcTheYardCaptured","Convict Allies",Has("Motercycle"))
        
    if (use_CtM(world)):
        create_rank_event(world,"ctmDrivingUpTheRamp","Toppat King",Has("Tank"))
        create_rank_event(world,"ctmEscapePlan","Free Man",Has("Offsite Drop Pod"))
        create_rank_event(world,"ctmCockpit","Special BROvert Ops",Has("Horn"))
        create_rank_event(world,"ctmCafeteriaJungle","Triple Threat")
        create_rank_event(world,"ctmTethered","Stickmin Space Resort",Has("Sniper Rifle"))
        create_rank_event(world,"ctmSecretWeapon","Jewel Baron",Has("Grow 'n Shrink"))
        create_rank_event(world,"ctmGetawayMeans","Little Nest Egg",Has("Inflatable Raft"))
        create_rank_event(world,"ctmFactionFriction","Toppat Recruits")
        create_rank_event(world,"ctmFactionFriction","Pardoned Pals")
        create_rank_event(world,"ctmCCCMobileUnit","Toppat 4 Life",Has("G.A.B.E.G.G"))
        create_rank_event(world,"ctmStorageBay","Cleaned 'em Out",Has("SuccPak"))
        create_rank_event(world,"ctmBountysFate","Master Bounty Hunter",Has("Ocarina"))
        create_rank_event(world,"ctmOrbitalHull","Valliant Hero",Has("Damaged Escape Pod"))
        create_rank_event(world,"ctmTheBrig","Toppat Civil Warfare",Has("Deuces! Doc"))
        create_rank_event(world,"ctmFloatingCart","Capital Gains",Has("Wombo Combo"))
        create_rank_event(world,"ctmClaimRevenge","Revenged",Has("Staple"))
