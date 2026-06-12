HENRY_NAME_TO_LOC_NAME = {
    "shovel":"BtB Bank: Shovel Fail",
    "explosives":"BtB Bank: Explosives Fail",
    "teleporter":"BtB Bank: Teleporter Fail",
    "laser":"BtB Bank: Laser Fail",
    "wreckingball":"BtB Bank: Wrecking Ball Fail",
    "The Story Begins":"BtB: The Story Begins",
    "etp_nrg":"EtP Cell: Nrg Drink Fail",
    "etp_teleporter":"EtP Cell: Teleporter Fail",
    "etp_rocket":"EtP Cell: Rocket Launcher Fail",
    "etp_fileWindow":"EtP Cell: File Window Fail",
    "etp_timed1":"EtP Cell Block: Rupert Kick Fail",
    "etp_timed2":"EtP Cell Block: Dave Taser Fail",
    "etp_grenade":"EtP Closet: Belt of Grenades Fail",
    "etp_ventLeft":"EtP Closet: Broken Pipe Fail",
    "etp_rope":"EtP Rooftop: Rope Fail",
    "etp_parachute":"EtP Rooftop: Parachute Fail",
    "etp_jetpack":"EtP Rooftop: JetPack Fail",
    "Sneaky Escapist":"EtP: Sneaky Escapist",
    "etp_cellphone":"EtP Courtroom: Declared Guilty Fail",
    "Lawyered Up":"EtP: Lawyered Up",
    "etp_opacitator":"EtP Bathroom: Opacitator Fail",
    "etp_chase1Up":"EtP Back Lobby: Pillar Fail",
    "etp_chase1Time":"EtP Back Lobby: Shot Fail",
    "etp_chase2Down":"EtP Lobby Turn: Brawl Fail",
    "etp_chase2Time":"EtP Lobby Turn: Crash Fail: ",
    "etp_timedFinal":"EtP Prison Entrance: Quicktime event Fail",
    "Baddass Bust Out":"EtP: Baddass Bust Out",
    "std_liquid":"StD Outer Wall: Liquidificator Fail",
    "std_shrinkray":"StD Outer Wall: Shrink Ray Fail",
    "std_teleporter":"StD Outer Wall: Anti-Gravity Cap Fail", #no this isen't a bug the internal name for this is just std_teleporter for some reason
    "std_jumble":"StD Outer Wall: Jumble Hoppers Fail",
    "std_fpunch":"StD Rooftop: Falcon Punch Fail",
    "std_tranq":"StD Rooftop: Tranquilizer Fail",
    "std_invisible":"StD Rooftop: Invisibility Pill Fail",
    "std_drop":"StD Catwalk: Drop Fail",
    "std_wormhole":"StD Catwalk: Wormhole Rifle Fail",
    "std_lasercut":"StD Diamond Exhibit: Laser Cutter Fail",
    "std_cannon":"StD Storage Room: Cannon Fail",
    "std_cheese":"StD Storage Room: Cheese Fail",
    "std_neck":"StD Backdoor: Snap Neck Fail",
    "std_rifle":"StD Backdoor: Rifle Fail",
    "std_jump":"StD Backdoor: Jump Fail",
    "Unseen Burglar":"StD: Unseen Burglar",
    "std_timedwwii":"StD WW2 Exhibit: Dave Conversation Fail",
    "std_bomb":"StD WW2 Exhibit: Bomb Fail",
    "std_gun":"StD WW2 Exhibit: Gun Fail",
    "std_sleepdiamond":"StD Diamond Exhibit Entrance: Light Sleeper Fail",
    "std_alien":"StD Retro Exhibit: Alien Fail",
    "std_goodball":"StD Retro Exhibit: Goodball Fail",
    "std_crowbar":"StD Retro Exhibit: Crowbar Fail",
    "std_nuke":"StD Center For Chaos Containment: Nuclear Bomb Fail",
    "std_zero":"StD Center For Chaos Containment: Divide by Zero Fail",
    "std_satellite":"StD Center For Chaos Containment: Shoop da Whoop Fail",
    "Just Plain Epic":"StD: Just Plain Epic",
    "std_timed1kick":"StD Parking Lot: Kick Fail",
    "std_timed1jump":"StD Parking Lot: Jump Fail",
    "std_timed1miss":"StD Parking Lot: Great Start Fail",
    "std_timed2lance":"StD Medieval Hall: Lance Fail",
    "std_timed2flail":"StD Medieval Hall: Flail Fail",
    "std_timed2miss":"StD Medieval Hall: Janitor Fail",
    "std_timed3basket":"StD Diamond Exhibit (Scooter): Basket Fail",
    "std_timed3miss":"StD Diamond Exhibit (Scooter): Stand Around Fail",
    "std_timed4miss":"StD Police Chase Car: Reflexes Fail",
    "std_timed4branch":"StD Police Chase Car: Branch Fail",
    "std_timed5miss":"StD Police Chase Helicopter: Headshot Fail",
    "std_timed5snade":"StD Police Chase Helicopter: Sticky Grenade Fail",
    "std_timed6miss":"StD Bridge: Do Something Fail",
    "std_timed6drive":"StD Bridge: Drive Fail",
    "std_timed6bribe":"StD Bridge: Bribe Fail",
    "Intruder On A Scooter":"StD: Intruder On A Scooter"
}


from .locations import LOCATION_NAME_TO_ID

from .items import ID_TO_ITEM_NAME




def henry_name_to_arc_id(henryName):
    arcIds = []
    for name in henryName:
        arcName = HENRY_NAME_TO_LOC_NAME[name]
        arcIds.append(LOCATION_NAME_TO_ID[arcName])
    return arcIds

def arc_id_to_henry_input_name(id):
    henryInputNames = []
    for idnum in id:
        inputName = ID_TO_ITEM_NAME[idnum.item]
        henryInputNames.append(inputName)
    return henryInputNames


def get_num_BtB_ranks_achived(ctx):
    num_btb_ranks = 0
    if LOCATION_NAME_TO_ID["BtB: The Story Begins"] in ctx.locations_checked:
        num_btb_ranks = num_btb_ranks + 1
    return num_btb_ranks

def get_num_EtP_ranks_achived(ctx):
    num_etp_ranks = 0
    if LOCATION_NAME_TO_ID["EtP: Lawyered Up"] in ctx.locations_checked:
        num_etp_ranks = num_etp_ranks + 1

    if LOCATION_NAME_TO_ID["EtP Rooftop: Rope Fail"] in ctx.locations_checked:
        num_etp_ranks = num_etp_ranks + 1

    if LOCATION_NAME_TO_ID["EtP: Baddass Bust Out"] in ctx.locations_checked:
        num_etp_ranks = num_etp_ranks + 1

    return num_etp_ranks

def check_if_goal_completed(ctx):
    if ctx.henryslotdata['Goal'] == 0:
        total_ranks = 0
        if ctx.henryslotdata['BtB'] != 0:
            total_ranks = total_ranks + get_num_BtB_ranks_achived(ctx)
        if ctx.henryslotdata['EtP'] != 0:
            total_ranks = total_ranks + get_num_EtP_ranks_achived(ctx)
        if total_ranks >= ctx.henryslotdata['Required_Ranks']:
            return True
    elif ctx.henryslotdata['Goal'] == 2:
        if ctx.henryslotdata['BtB'] != 0 and get_num_BtB_ranks_achived(ctx) < 1:
            return False
        if ctx.henryslotdata['EtP'] != 0 and get_num_EtP_ranks_achived(ctx) < 1:
            return False
        return True
    return False

def get_henry_deathlink_reason(henryNames, playerName):
    for name in henryNames:
        match name:
            case "shovel":
                return f"{playerName} dug strate down"
            case "explosives":
                return f"{playerName} used no care"
            case "laser":
                return f"{playerName} cut into the bank"
            case "etp_nrg":
                return f"{playerName} had nausea, headache, rapid heartrate, and stroke or heart attack"
            case "etp_rocket":
                return f"{playerName} had very poor aim"
            case "etp_fileWindow":
                return f"{playerName} leaped before looking"
            case "etp_grenade":
                return f"{playerName} diden't check themself"
            case "etp_rope":
                return f"{playerName} was sent to another world"
            case "etp_parachute":
                return f"{playerName} made an ass out of u and me"
            case "etp_opacitator":
                return f"{playerName} was part of the beta test"
            case "etp_chase1Time":
                return f"{playerName} was a n00b"
            case "etp_timedFinal":
                return f"{playerName} was so close"
            case "std_liquid":
                return f"{playerName} turned into liquid"
            case "std_shrinkray":
                return f"{playerName} fought a worm"
            case "std_teleporter":
                return f"{playerName} went to space"
            case "std_wormhole":
                return f"{playerName} achived terminal velocity"
            case "std_lasercut":
                return f"{playerName} get cut"
            case "std_bomb":
                return f"{playerName} threw a bomb"
            case "std_alien":
                return f"{playerName} tried to give orders"
            case "std_crowbar":
                return f"{playerName} was overwhelmed"
            case "std_nuke":
                return f"{playerName} got camped"
            case "std_zero":
                return f"                                                                  "
            case "std_satellite":
                return f"IMMA FIRIN MY LAZAR"
            case "std_timed4miss":
                return f"{playerName} has dull reflexes"
            case "std_timed5miss":
                return f"{playerName} waved goodbye to their head"
            case "std_timed5snade":
                return f"{playerName} got stuck"
            case "std_timed6bribe":
                return f"{playerName} commited a federal offense"
            case "std_timed6miss":
                return f"{playerName} left him no choice"
            case "std_timed6drive":
                return f"{playerName} diden't get very far"

    return "None"
        