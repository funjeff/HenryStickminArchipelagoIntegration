from __future__ import annotations

from typing import TYPE_CHECKING

from rule_builder.options import OptionFilter
from rule_builder.rules import Has, HasAll, Rule, HasFromListUnique, HasAny
from .options import BtB,EtP, ItA,StD,Required_Ranks

from .henryHelpers import *


if TYPE_CHECKING:
    from .world import HenryStickminWorld



def set_all_rules(world: HenryStickminWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_location_rules(world)
    set_completion_condition(world)


    # Conditions can also depend on event items. TODO use this for CtM

def set_location_rule(world,location,rule):
    loc = world.get_location(location)
    world.set_rule(loc,rule)


def set_all_location_rules(world: HenryStickminWorld) -> None:
    if (use_BtB(world)):
        set_location_rule(world,"BtB Bank: Shovel Fail",Has("Shovel"))
        set_location_rule(world,"BtB Bank: Explosives Fail",Has("Explosives"))
        set_location_rule(world,"BtB Bank: Teleporter Fail",Has("Teleporter"))
        set_location_rule(world,"BtB Bank: Laser Fail",Has("Laser"))
        set_location_rule(world,"BtB Bank: Wrecking Ball Fail",Has("Wrecking Ball"))
        set_location_rule(world,"BtB: The Story Begins",Has("Money Bag Disguise"))
                
    if (use_EtP(world)):
        set_location_rule(world,"EtP Cell: Nrg Drink Fail",Has("Nrg Drink"))
        set_location_rule(world,"EtP Cell: Teleporter Fail",Has("Teleporter"))
        set_location_rule(world,"EtP Cell: Rocket Launcher Fail",Has("Rocket Launcher"))
        set_location_rule(world,"EtP Closet: Belt of Grenades Fail",Has("Belt of Grenades"))
        set_location_rule(world,"EtP Closet: Broken Pipe Fail",Has("Chair"))
        set_location_rule(world,"EtP Rooftop: Rope Fail",Has("Rope Launcher"))
        set_location_rule(world,"EtP Rooftop: Parachute Fail",Has("Parachute"))
        set_location_rule(world,"EtP Rooftop: JetPack Fail",Has("JetPack"))
        set_location_rule(world,"EtP: Sneaky Escapist",Has("Plungers"))

        set_location_rule(world,"EtP Courtroom: Declared Guilty Fail",Has("Attorney's Badge") | Has("Floor Plans of Bank") | Has("Doctor's Analysis") | Has("Security Footage") | Has("Teleporter"))
        set_location_rule(world,"EtP: Lawyered Up",Has("Money Bag Disguise"))
        
        set_location_rule(world,"EtP Bathroom: Opacitator Fail",Has("Opacitator"))

    if (use_StD(world)):
        set_location_rule(world,"StD Outer Wall: Liquidificator Fail",Has("Liquidificator"))
        set_location_rule(world,"StD Outer Wall: Shrink Ray Fail",Has("Shrink Ray"))
        set_location_rule(world,"StD Outer Wall: Anti-Gravity Cap Fail",Has("Anti-Gravity Cap"))
        set_location_rule(world,"StD Outer Wall: Jumble Hoppers Fail",Has("Jumble Hoppers"))
        set_location_rule(world,"StD Rooftop: Falcon Punch Fail",Has("Falcon Punch"))
        set_location_rule(world,"StD Rooftop: Tranquilizer Fail",Has("Tranquilizer"))
        set_location_rule(world,"StD Rooftop: Invisibility Pill Fail",Has("Invisibility Pill"))
        set_location_rule(world,"StD Catwalk: Wormhole Rifle Fail",Has("Wormhole Rifle"))
        set_location_rule(world,"StD Diamond Exhibit: Laser Cutter Fail",Has("Laser Cutter"))
        set_location_rule(world,"StD Storage Room: Cannon Fail",Has("Cannon"))
        set_location_rule(world,"StD Storage Room: Cheese Fail",Has("Cheese"))
        set_location_rule(world,"StD Backdoor: Rifle Fail",Has("Rifle"))
        set_location_rule(world,"StD: Unseen Burglar",Has("Tunisian Diamond"))

        set_location_rule(world,"StD WW2 Exhibit: Bomb Fail",Has("WW2 Bomb"))
        set_location_rule(world,"StD WW2 Exhibit: Gun Fail",Has("WW2 Gun"))
        set_location_rule(world,"StD Retro Exhibit: Alien Fail",Has("Metroid"))
        set_location_rule(world,"StD Retro Exhibit: Goodball Fail",Has("Goodball"))
        set_location_rule(world,"StD Retro Exhibit: Crowbar Fail",Has("Crowbar"))
        set_location_rule(world,"StD Center For Chaos Containment: Nuclear Bomb Fail",Has("Nuclear Bomb"))
        set_location_rule(world,"StD Center For Chaos Containment: Divide by Zero Fail",Has("Division By Zero"))
        set_location_rule(world,"StD: Just Plain Epic",Has("Giant CCC Robot"))

        set_location_rule(world,"StD Medieval Hall: Lance Fail",Has("Lance"))
        set_location_rule(world,"StD Medieval Hall: Flail Fail",Has("Flail"))
        set_location_rule(world,"StD Diamond Exhibit (Scooter): Basket Fail",Has("Basket"))
        set_location_rule(world,"StD Police Chase Car: Branch Fail",Has("Branch"))
        set_location_rule(world,"StD Police Chase Helicopter: Sticky Grenade Fail",Has("Sticky Grenade"))
        set_location_rule(world,"StD: Intruder On A Scooter",Has("Tunisian Diamond"))
    
    if (use_ItA(world)):

        set_location_rule(world,"ItA Cargo Bay: Zero-Point Energy Fail",Has("Zero-Point Energy"))
        set_location_rule(world,"ItA Cargo Bay: Ball 'n' Chain Fail",Has("Ball 'n Chain"))

        set_location_rule(world,"ItA Viewing Platform: Bomb Fail",Has("Bomb"))
        set_location_rule(world,"ItA Viewing Platform: Joy Buzzer Fail",Has("Joy Buzzer"))
        set_location_rule(world,"ItA Viewing Platform: Expanding Foam Fail",Has("Expanding Foam"))
        set_location_rule(world,"ItA Engine Room Records Side: Stretch Chewies Fail",Has("Stretch Chewies"))
        set_location_rule(world,"ItA Engine Room Records Side: Magic Pencil Fail",Has("Magic Pencil"))
        set_location_rule(world,"ItA Engine Room Records Side: Teleporter Fail",Has("Teleporter"))
        set_location_rule(world,"ItA Brig: Wizard Magic Fail",Has("Wizard Magic"))
        set_location_rule(world,"ItA Brig: Retroglove Fail",Has("Retroglove"))
        set_location_rule(world,"ItA Vault: Gravity Manipulator Fail",Has("Gravity Manipulator"))
        set_location_rule(world,"ItA Vault: Clawpack Fail",Has("Clawpack"))
        set_location_rule(world,"ItA Outer Wing: Umbrella Fail",Has("Umbrella"))
        set_location_rule(world,"ItA Outer Wing: Propane Tank Fail",Has("Propane Tank"))
        set_location_rule(world,"ItA Outer Wing: Shell Fail",Has("Shell"))
        set_location_rule(world,"ItA Center For Chaos Containment: D.E.B Fail",Has("D.E.B Disk"))
        set_location_rule(world,"ItA Center For Chaos Containment: L. Cut mk. II Fail",Has("L. Cut mk. II Disk"))
        set_location_rule(world,"ItA Center For Chaos Containment: Gaben Fail",Has("Scratched Disk"))
        set_location_rule(world,"ItA: Pure Blooded Thief",Has("Prototype Disk"))

        set_location_rule(world,"ItA Airship Topside: Acid Fail",Has("Acid"))
        set_location_rule(world,"ItA Airship Topside: C4 Fail",Has("C4"))
        set_location_rule(world,"ItA Boardroom: Disguise Fail",Has("Toppat Disguise"))
        set_location_rule(world,"ItA Boardroom: Transdimensionalizer Fail",Has("Transdimensionalizer"))
        set_location_rule(world,"ItA Engine Room Vault Side: Gravity Bubble Fail",Has("Gravity Bubble"))
        set_location_rule(world,"ItA Engine Room Vault Side: Platform Fail",Has("Platform"))
        set_location_rule(world,"ItA Engine Vents: Gatling Gun Fail",Has("Gatling Gun"))
        set_location_rule(world,"ItA Engine Vents: Mind Control Fail",Has("Mind Control"))
        set_location_rule(world,"ItA Engine Vents: Remote Access Fail",Has("Remote Access"))
        set_location_rule(world,"ItA Records Library: Ninja Star Fail",Has("Ninja Star"))
        set_location_rule(world,"ItA Records Library: Falcon Kick Fail",Has("Falcon Kick"))
        set_location_rule(world,"ItA Cargo Bay Evidence: Banana Bomb Fail",Has("Banana Bomb"))
        set_location_rule(world,"ItA Cargo Bay Evidence: Sleeping Gas Fail",Has("Sleeping Gas"))
        set_location_rule(world,"ItA Cargo Bay Evidence: Flashbang Fail",Has("Flashbang"))
        set_location_rule(world,"ItA: Government Supported Private Investigator",Has("Force Gun"))

        set_location_rule(world,"ItA Bridge: Laser Fail",Has("Cannon Ball Laser"))
        set_location_rule(world,"ItA Bridge: Thruster Fail",Has("Cannon Ball Thruster"))
        set_location_rule(world,"ItA Warehouse: Spikes Fail",Has("Cannon Ball Spikes"))
        set_location_rule(world,"ItA Warehouse: Boost Fail",Has("Cannon Ball Boost"))
        set_location_rule(world,"ItA Quarters Hallway: Warp Fail",Has("Warp"))
        set_location_rule(world,"ItA Quarters Hallway: Metal Fist Fail",Has("Metal Fist"))
        set_location_rule(world,"ItA Brig Damaged: Robo Pants Fail",Has("Robo Pants"))        
        set_location_rule(world,"ItA Brig Damaged: Metal Bend Fail",Has("Metalbending"))
        set_location_rule(world,"ItA Yo-Yo Fight: PSI Fail",Has("PSI Flash"))
        set_location_rule(world,"ItA Dirk Fight: Magic Fail",Has("Fire Magic"))
        set_location_rule(world,"ItA Ventalation Shaft: JetBoots Fail",Has("JetBoots"))
        set_location_rule(world,"ItA Ventalation Shaft: Beef Up Fail",Has("Beef Up"))
        set_location_rule(world,"ItA Cargo Bay Hostage: Parachute Fail",Has("Parachute"))
        set_location_rule(world,"ItA Cargo Bay Hostage: Missile Fail",Has("Missile"))
        set_location_rule(world,"ItA: Rapidly Promoted Executive",Has("Dummies"))
        set_location_rule(world,"ItA: Relentlesss Bounty Hunter",Has("Tank"))
    
    if (use_FtC(world)):
        set_location_rule(world,"FtC Henry's Cell: Cookie Fail",Has("Cookie"))      
        set_location_rule(world,"FtC Henry's Cell: Teleporter Fail",Has("Teleporter"))      
        set_location_rule(world,"FtC Henry's Cell: Sonic Pulse Fail",Has("Sonic Pulse"))

        set_location_rule(world,"FtC Cafeteria Toppat: Undercover Agent Fail",Has("Undercover Agent"))      
        set_location_rule(world,"FtC Cafeteria Toppat: Neurotoxin Fail",Has("Neurotoxin"))      
        set_location_rule(world,"FtC Airship: Magnet Fail",Has("Magnet"))      
        set_location_rule(world,"FtC Airship: Slingshot Fail",Has("Slingshot"))      
        set_location_rule(world,"FtC: The Betrayed",Has("Sick Ride"))

        set_location_rule(world,"FtC Cafeteria Government: Earthbend Fail",Has("Earthbending"))      
        set_location_rule(world,"FtC Cafeteria Government: Bubble Shield Fail",Has("Bubble Shield"))
        set_location_rule(world,"FtC Fire Escape: Snipe Fail",Has("Sniper Rifle"))

        set_location_rule(world,"FtC Transfer Cells Hallway: Speed Shoes Fail",Has("Speed Shoes"))
        set_location_rule(world,"FtC Transfer Cells Blockade: Tool Gun Fail",Has("Tool Gun"))      
        set_location_rule(world,"FtC Behind The Truck: Sandwich Fail",Has("Sandwich"))
        set_location_rule(world,"FtC Behind The Truck: Costume Fail",Has("Snowman Costume"))
        set_location_rule(world,"FtC Car Chase: Shoot Fail",Has("Pistol"))
        set_location_rule(world,"FtC Car Chase: Bail Fail",Has("Parachute"))
        set_location_rule(world,"FtC Clifside Wreck: Warp Star Fail",Has("Warpstar"))
        set_location_rule(world,"FtC Clifside Wreck: Airbag Fail",Has("Airbag"))

        set_location_rule(world,"FtC Storage Room Solo: Command Melody Fail",Has("Command Melody"))
        set_location_rule(world,"FtC Outside Security Solo: Longshot Fail",Has("Longshot"))
        set_location_rule(world,"FtC Outside Security Solo: Spring Fail",Has("Spring"))
        set_location_rule(world,"FtC Elevator: Bungee Fail",Has("Rope"))
        set_location_rule(world,"FtC Bowels of the Complex: Plunger Boots Fail",Has("Plunger Boots"))
        set_location_rule(world,"FtC Docks: Box Fail",Has("Cardboard Box"))
        set_location_rule(world,"FtC Docks: Shadozer Fail",Has("Shadozer"))
        set_location_rule(world,"FtC Outer Docks: S. S. Annie Fail",Has("S.S. Annie"))
        set_location_rule(world,"FtC Outer Docks: Rocket Fail",Has("Rocket"))
        set_location_rule(world,"FtC: Ghost Inmate",Has("Dinghy"))

        set_location_rule(world,"FtC Storage Room Ellie: Bounce Bros Fail",Has("Bounce Bros"))
        set_location_rule(world,"FtC Storage Room Ellie: Tall Guy Fail",Has("Trenchcoat"))
        set_location_rule(world,"FtC Outside Security Ellie: GraviToR v2.0 Fail",Has("GraviToR v2.0"))
        set_location_rule(world,"FtC Hallway Standoff: Crazy Explosion Fail",Has("Grenade") & Has("Taser"))
        set_location_rule(world,"FtC Hallway Standoff: Instant Replay Fail",Has("Crossbow") & Has("Sniper Rifle"))
        set_location_rule(world,"FtC Hallway Standoff: Neverrrrr Fail",Has("Crossbow") & Has("Grenade"))
        set_location_rule(world,"FtC Two Elevators: Blend In Fail",Has("The Wall Hat"))
        set_location_rule(world,"FtC Two Elevators: Pass By Fail",Has("The Wall Hat"))
        set_location_rule(world,"FtC The Yard Captured: Adrenaline Fail",Has("Adrenaline"))
        set_location_rule(world,"FtC The Yard Captured: The KNEE Fail",Has("The KNEE"))
        set_location_rule(world,"FtC: Convict Allies",Has("Motercycle"))
    
    if (use_CtM(world)):
        set_location_rule(world,"CtM Control Tower: Super Punch Fail",Has("Super Punch")) 
        set_location_rule(world,"CtM Control Tower: Very Accurate Targetting System Fail",Has("Very Accurate Targetting System")) 
        set_location_rule(world,"CtM Inside Helicopter: Helicopter Fail",Has("Helicopter")) 
        set_location_rule(world,"CtM Under The Rocket: Revolver Fail",Has("Revolver")) 
        set_location_rule(world,"CtM Under The Rocket: Boomerang Fail",Has("Boomerang")) 
        set_location_rule(world,"CtM Back To Back: Summon Fail",Has("Summon")) 
        set_location_rule(world,"CtM Back To Back: Style on 'em Fail",Has("Stylish Moves")) 
        set_location_rule(world,"CtM Left Behind: Cloud Fail",Has("Cloud")) 
        set_location_rule(world,"CtM Left Behind: G-Inverter Fail",Has("G-Inverter")) 
        set_location_rule(world,"CtM: Toppat King",Has("Tank")) 


        set_location_rule(world,"CtM Orbital Cell Still: Lockpick Fail",Has("Lockpick")) 
        set_location_rule(world,"CtM Orbital Cell Still: Melt Ray Fail",Has("Melt Ray")) 
        set_location_rule(world,"CtM Orbital Cell Still: Bomb Fail",Has("Bomb")) 
        set_location_rule(world,"CtM Choose Your Weapon: Big Sword Fail",Has("Big Sword")) 
        set_location_rule(world,"CtM Choose Your Weapon: Underbarel Grenade Launcher Fail",Has("Underbarrel Grenade Launcher")) 
        set_location_rule(world,"CtM Cafeteria Space: Harden Fail",Has("Harden")) 
        set_location_rule(world,"CtM Solar Panel Dash: Fire Missiles Fail",Has("Nano-Suit Missiles")) 
        set_location_rule(world,"CtM Solar Panel Dash: Positron Reflector Fail",Has("Positron Reflector")) 
        set_location_rule(world,"CtM Escape Plan: Comunications Satalite Fail",Has("Communications Satellite")) 
        set_location_rule(world,"CtM Escape Plan: Towards Enemy Fail",Has("Backwards Satellite")) 
        set_location_rule(world,"CtM Free Man",Has("Offsite Drop Pod"))

        set_location_rule(world,"CtM Sam Turret Roof: Cupcake Fail",Has("Cupcake")) 
        set_location_rule(world,"CtM Cross Over: JetPod Fail",Has("JetPod")) 
        set_location_rule(world,"CtM Cross Over: Invisible Bridge Fail",Has("Invisible Bridge")) 
        set_location_rule(world,"CtM Storage Bay Charles: TV Broadcast Fail",Has("TV Broadcast")) 
        set_location_rule(world,"CtM Storage Bay Charles: Subsonic Wave Fail",Has("Subsonic Wave")) 
        set_location_rule(world,"CtM Engine Room: Wrench Fail",Has("Wrench")) 
        set_location_rule(world,"CtM Hall Of Leaders: Painting Portal Fail",Has("Painting Portal")) 
        set_location_rule(world,"CtM Hall Of Leaders: Bug Juice Fail",Has("Bug Juice")) 
        set_location_rule(world,"CtM Cockpit: IR Sniper Fail",Has("IR Sniper")) 
        set_location_rule(world,"CtM Cockpit: Sleep Dart Fail",Has("Sleep Dart")) 
        set_location_rule(world,"CtM: Special BROvert Ops",Has("Horn")) 

        set_location_rule(world,"CtM Where We Droppin: Parking Lot Fail",Has("Parachute")) 
        set_location_rule(world,"CtM Where We Droppin: Control Tower Fail",Has("Umbrella Glider")) 
        set_location_rule(world,"CtM Where We Droppin: Rocket Entrance Fail",Has("Wings")) 
        set_location_rule(world,"CtM Rocket Boarding Last Call: Build Fail",Has("Dirt Blocks")) 
        set_location_rule(world,"CtM Rocket Boarding Last Call: Climb Down and Run Fail",Has("Rope")) 
        set_location_rule(world,"CtM Combo Time: Net Fail",Has("Net Launcher")) 
        set_location_rule(world,"CtM Cafeteria Jungle: Downgrader Fail",Has("Downgrader")) 
        set_location_rule(world,"CtM Cafeteria Jungle: Fusion Fail",Has("Fusion Earings"))

        set_location_rule(world,"CtM Closed Entrance: Battering Ram Fail",Has("Battering Ram")) 
        set_location_rule(world,"CtM Closed Entrance: Drill Fail",Has("Scooter Drill")) 
        set_location_rule(world,"CtM Top of the Rocket: Hammer Yourself Fail",Has("Hammer")) 
        set_location_rule(world,"CtM Top of the Rocket: 95 More Hits Fail",Has("Hammer")) 
        set_location_rule(world,"CtM: Stickmin Space Resort",Has("Sniper Rifle")) 
        
        set_location_rule(world,"CtM Space Scooter: Light Speed Fail",Has("Light Speed")) 
        set_location_rule(world,"CtM Gravity Pit: Pole Vault Fail",Has("Pole Vault Stick")) 
        set_location_rule(world,"CtM Gravity Pit: Catapult Fail",Has("Catapult")) 
        set_location_rule(world,"CtM Gravity Pit: Ramp Fail",Has("Wooden Ramp")) 
        set_location_rule(world,"CtM Gravity Pit: Rocket Fail",Has("Paper Rocket")) 
        set_location_rule(world,"CtM Gravity Pit: Bridge Fail",Has("Bridge")) 
        set_location_rule(world,"CtM Gravity Pit: Cannon Fail",Has("Cannon")) 
        set_location_rule(world,"CtM Station Vault: SMASH Fail",Has("SMASH")) 
        set_location_rule(world,"CtM Gamma Lounge: Emerald Fail",Has("Norwegian Emerald")) 
        set_location_rule(world,"CtM Gamma Lounge: Chance Time Fail",Has("Chance Dice")) 
        set_location_rule(world,"CtM Secret Weapon: Super Henry Fail",Has("Norwegian Emerald")) 
        set_location_rule(world,"CtM: Jewel Baron",Has("Grow 'n Shrink"))

        set_location_rule(world,"CtM Tank Attack: Fire Fail",Has("Tank")) 
        set_location_rule(world,"CtM Tank Attack: Join the Caravan Fail",Has("Tank")) 
        set_location_rule(world,"CtM Getaway Means: By Air Fail",Has("Train Car Spring")) 
        set_location_rule(world,"CtM: Little Nest Egg",Has("Inflatable Raft"))

        set_location_rule(world,"CtM Parking Lot: Very Cool Fail",Has("Controller") & Has("Wings")) 
        set_location_rule(world,"CtM Parking Lot: Wrong Type Fail",Has("Controller") & Has("Rocket Launcher")) 
        set_location_rule(world,"CtM Parking Lot: What Plan Fail",Has("Rope") & Has("Rocket Launcher"))
        set_location_rule(world,"CtM Launch Tower Hallway: CorrupTick Fail",Has("CorrupTick")) 
        set_location_rule(world,"CtM Launch Tower Hallway: Disguise Kit Fail",Has("Disguise Kit")) 
        set_location_rule(world,"CtM Collapse: Grapple Fail",Has("Grapple Gun")) 
        set_location_rule(world,"CtM Faction Friction: None Fail",Has("Knife"))
        
        set_location_rule(world,"CtM Cliffside: Rope Fail",Has("Rope Launcher")) 
        set_location_rule(world,"CtM The Watchtower: Knife Fail",Has("Knife")) 
        set_location_rule(world,"CtM The Watchtower: Duplicatorange Fail",Has("Duplicatorange")) 
        set_location_rule(world,"CtM Big Boy: Walkthrough Fail",Has("Walkthrough")) 
        set_location_rule(world,"CtM CCC Mobile Unit: Ultimate Freeze Fail",Has("Ultimate Freeze")) 
        set_location_rule(world,"CtM CCC Mobile Unit: Moon Fail",Has("Evil Moon")) 
        set_location_rule(world,"CtM CCC Mobile Unit: Nuclear Bomb Fail",Has("Nuclear Bomb")) 
        set_location_rule(world,"CtM: Toppat 4 Life",Has("G.A.B.E.G.G"))

        set_location_rule(world,"CtM Cargo Stopped: Toppat Box Fail",Has("Toppat Box")) 
        set_location_rule(world,"CtM Cargo Stopped: Prop Fail",Has("Prop"))
        set_location_rule(world,"CtM Top of the Train: Pincher Fail",Has("Pinchers"))
        set_location_rule(world,"CtM Storage Bay: Leafmode Fail",Has("LeafMode")) 
        set_location_rule(world,"CtM Storage Bay: Infini3 Fail",Has("Infini3")) 
        set_location_rule(world,"CtM: Cleaned 'em Out",Has("SuccPak")) 

        set_location_rule(world,"CtM Doorway: Cluster Charge Fail",Has("Cluster Charge")) 
        set_location_rule(world,"CtM Face to Face: Self-Destruct Fail",Has("Self Destruct")) 
        set_location_rule(world,"CtM: Master Bounty Hunter",Has("Ocarina"))

        set_location_rule(world,"CtM Infiltrating the Orbital Station: Air Cannon Fail",Has("Air Cannon")) 
        set_location_rule(world,"CtM Infiltrating the Orbital Station: Beam Aboard Fail",Has("Warp Beam")) 
        set_location_rule(world,"CtM Orbital Hull: Super Accurate Lase Shot Fail",Has("Super Accurate Laser Shot")) 
        set_location_rule(world,"CtM Orbital Hull: Hot Knife Fail",Has("Hot Knife")) 
        set_location_rule(world,"CtM Escape Pods: Luxury Fail",Has("Luxury Escape Pod")) 
        set_location_rule(world,"CtM Escape Pods: Reverse Thruster Fail",Has("Normal Escape Pod")) 
        set_location_rule(world,"CtM: Valliant Hero",Has("Damaged Escape Pod")) 

        set_location_rule(world,"CtM The Plank: Chainsaw Fail",Has("Chainsaw")) 
        set_location_rule(world,"CtM The Plank: Save State Fail",Has("Save States")) 
        set_location_rule(world,"CtM The Brig: Toppy Fail",Has("Toppy")) 
        set_location_rule(world,"CtM The Brig: Mind Crystal Fail",Has("Mind Crystal")) 
        set_location_rule(world,"CtM A Few Ideas: The Good Gents Fail",Has("Good Gents Doc")) 
        set_location_rule(world,"CtM A Few Ideas: Midnight Surprise Fail",Has("Midnight Surprise Doc")) 
        set_location_rule(world,"CtM: Toppat Civil Warfare",Has("Deuces! Doc"))

        set_location_rule(world,"CtM Train Assault: Swords Fail",Has("Sword")) 
        set_location_rule(world,"CtM Crash Site: Purse of Holding Fail",Has("Purse of Holding"))
        set_location_rule(world,"CtM Crash Site: Force Lift Fail",Has("The Force")) 
        set_location_rule(world,"CtM The Floating Cart: Needle Fail",Has("Needle")) 
        set_location_rule(world,"CtM The Floating Cart: Shell Bounce Fail",Has("Shell Bounce")) 
        set_location_rule(world,"CtM: Capital Gains",Has("Wombo Combo"))

        set_location_rule(world,"CtM Showdown: Spirit Forme Fail",Has("Spirit Forme")) 
        set_location_rule(world,"CtM Showdown: Gun Forme Fail",Has("Gun Forme")) 
        set_location_rule(world,"CtM Finishing Move: Baseball Bat Fail",Has("Baseball Bat")) 
        set_location_rule(world,"CtM: Revenged",Has("Staple")) 

def set_completion_condition(world: HenryStickminWorld) -> None:
    if world.options.Goal == 0:
        obtainable_ranks = []
        if use_BtB(world):
            obtainable_ranks.extend(get_BtB_rank_event_item_names())
        if use_EtP(world):
            obtainable_ranks.extend(get_EtP_rank_event_item_names())
        if use_StD(world):
            obtainable_ranks.extend(get_StD_rank_event_item_names())
        if use_ItA(world):
            obtainable_ranks.extend(get_ItA_rank_event_item_names())
        if (use_FtC(world)):
            obtainable_ranks.extend(get_FtC_rank_event_item_names())
        if (use_CtM(world)):
            obtainable_ranks.extend(get_CtM_rank_event_item_names())
        
        world.set_completion_rule(HasFromListUnique(*obtainable_ranks,count=get_usable_rank_goal_num_from_world(world)))
    
    if world.options.Goal == 1 and use_CtM(world):
        world.set_completion_rule(HasAny(*get_CtM_rank_event_item_names()))

    if world.options.Goal == 2 or (world.options.Goal == 1 and not use_CtM(world)):
        btbCheck = HasAny(*get_BtB_rank_event_item_names(),options=[OptionFilter(BtB,BtB.option_no,operator="ne")],filtered_resolution=True)
        etpCheck = HasAny(*get_EtP_rank_event_item_names(),options=[OptionFilter(EtP,EtP.option_no,operator="ne")],filtered_resolution=True)
        stdCheck = HasAny(*get_StD_rank_event_item_names(),options=[OptionFilter(StD,StD.option_no,operator="ne")],filtered_resolution=True)
        itaCheck = HasAny(*get_ItA_rank_event_item_names(),options=[OptionFilter(ItA,ItA.option_no,operator="ne")],filtered_resolution=True)
        ftcCheck = HasAny(*get_FtC_rank_event_item_names(),options=[OptionFilter(FtC,FtC.option_no,operator="ne")],filtered_resolution=True)
        ctmCheck = HasAny(*get_CtM_rank_event_item_names(),options=[OptionFilter(CtM,CtM.option_no,operator="ne")],filtered_resolution=True)
        world.set_completion_rule(btbCheck & etpCheck & stdCheck & itaCheck & ftcCheck & ctmCheck)



# One final comment about rules:
# If your world exclusively uses Rule Builder rules (like APQuest), it's worth trying CachedRuleBuilderWorld.
# CachedRuleBuilderWorld is a subclass of World that has a bunch of caching magic to make rules faster.
# Just have your world class subclass CachedRuleBuilderWorld instead of World:
#   class APQuestWorld(CachedRuleBuilderWorld): ...
# This may speed up your world, or it may make it slower.
# The exact factors are complex and not well understood, but there is no harm in trying it.
# Generate a few seeds and see if there is a noticeable difference!
# If you're wondering, author has checked: APQuest is too simple to see any benefits, so we'll stick with "World".
