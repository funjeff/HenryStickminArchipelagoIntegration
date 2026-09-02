from typing import TYPE_CHECKING
from rule_builder.rules import Has, HasAny

from .options import BtB,EtP, ItA,StD,FtC,Required_Ranks,CtM

if TYPE_CHECKING:
    from .world import HenryStickminWorld


def use_BtB(world):
    if world.options.BtB == 1 or world.options.BtB == 2:
        return True
    return False


def use_EtP(world):
    if world.options.EtP == 1 or world.options.EtP == 2 or world.options.EtP == 3:
        return True
    return False

def use_StD(world):
    if world.options.StD == 1 or world.options.StD == 2 or world.options.StD == 3:
        return True
    return False

def use_ItA(world):
    if world.options.ItA == 1 or world.options.ItA == 2 or world.options.ItA == 3:
        return True
    return False

def use_FtC(world):
    if world.options.FtC == 1 or world.options.FtC == 2 or world.options.FtC == 3:
        return True
    return False   

def use_CtM(world):
    if world.options.CtM == 1 or world.options.CtM == 2 or world.options.CtM == 3:
        return True
    return False   

def get_BtB_rank_event_item_names():
    return ["Story Begins Event Item"]

def get_EtP_rank_event_item_names():
    return["Lawyered Up Event Item","Sneaky Escapist Event Item","Badass Bust Out Event Item"]

def get_StD_rank_event_item_names():
    return["Unseen Burglar Event Item","Intruder On A Scooter Event Item","Just Plain Epic Event Item"]

def get_ItA_rank_event_item_names():
    return["Relentless Bounty Hunter Event Item","Government Supported Private Investigator Event Item","Rapidly Promoted Executive Event Item","Pure Blooded Thief Event Item"]

def get_FtC_rank_event_item_names():
    return["Presumed Dead Event Item","International Rescue Operative Event Item","The Betrayed Event Item","Ghost Inmate Event Item","Convict Allies Event Item"]

def get_CtM_rank_event_item_names():
    return["Toppat King Event Item","Free Man Event Item","Special BROvert Ops Event Item","Triple Threat Event Item","Stickmin Space Resort Event Item","Jewel Baron Event Item","Little Nest Egg Event Item","Toppat Recruits Event Item","Pardoned Pals Event Item","Toppat 4 Life Event Item","Cleaned 'em Out Event Item","Master Bounty Hunter Event Item","Valliant Hero Event Item","Toppat Civil Warfare Event Item","Capital Gains Event Item","Revenged Event Item"]

def get_num_avilable_ranks_from_world(world):
    num_avilable_ranks = 0
    if use_BtB(world):
        num_avilable_ranks = num_avilable_ranks + len(get_BtB_rank_event_item_names())
    if use_EtP(world):
        num_avilable_ranks = num_avilable_ranks + len(get_EtP_rank_event_item_names())
    if use_StD(world):
        num_avilable_ranks = num_avilable_ranks + len(get_StD_rank_event_item_names())
    if use_ItA(world):
        num_avilable_ranks = num_avilable_ranks + len(get_ItA_rank_event_item_names())
    if use_FtC(world):
        num_avilable_ranks = num_avilable_ranks + len(get_FtC_rank_event_item_names())
    return num_avilable_ranks

def get_usable_rank_goal_num_from_world(world):
    use_rank_goal = min(get_num_avilable_ranks_from_world(world),world.options.Required_Ranks.value)
    return use_rank_goal

def get_EtP_unlock_rule(world):
    if world.options.EtP == EtP.option_yes_vanilla:
        return HasAny(*get_BtB_rank_event_item_names())
    else: 
        return Has("Escaping The Prison")

def get_StD_unlock_rule(world):
    if world.options.StD == StD.option_yes_vanilla:
        return HasAny(*get_EtP_rank_event_item_names())
    else: 
        return Has("Stealing The Diamond")

def get_ItA_unlock_rule(world):
    if world.options.ItA == ItA.option_yes_vanilla:
        return HasAny(*get_StD_rank_event_item_names())
    else: 
        return Has("Infiltraiting The Airship")

def get_FtC_unlock_rule(world):
    if world.options.FtC == FtC.option_yes_vanilla:
        return HasAny(*get_ItA_rank_event_item_names())
    else: 
        return Has("Fleeing The Complex")

def get_CtM_unlock_rule(world):
    if world.options.CtM == CtM.option_yes_vanilla:
        return HasAny(*get_FtC_rank_event_item_names())
    else: 
        return Has("Completing The Mission")


def get_CtM_timeline_unlock_rule(world,itaEndingRequirement,ftcEndingReqirement):
    itaEndingRule = Has(f"{itaEndingRequirement} Timeline Unlock")
    ftcEndingRule = Has(f"{ftcEndingReqirement} Timeline Unlock")
    
    if world.options.CtMTimelineUnlockMode == 0:
        if (use_ItA(world)):
            itaEndingRule = Has(f"{itaEndingRequirement} Event Item")
        
        if (use_FtC(world)):
            ftcEndingRule = Has(f"{ftcEndingReqirement} Event Item")
    
    return itaEndingRule & ftcEndingRule & get_CtM_unlock_rule(world)

