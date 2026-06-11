# from .world import HenryStickminWorld


# # class HenryDataContainer:
# #     def __init__(self):
# #         self.regions = RegionContainer()

# #     def FillDataContainer(self, world: HenryStickminWorld) -> None:
# #         self.regions.FillRegionContainers(world)
    
# #     def GetRegionContainers(self):
# #         return self.regions


# class RegionContainer:
#     def __init__(self):
#         self.btbRegions = BtBRegionContainer()
#         self.etpRegions = EtPRegionContainer()

#     def GetBtBRegions(self):
#         return self.btbRegions

#     def GetEtPRegions(self):
#         return self.etpRegions

#     def FillRegionContainers(self, world: HenryStickminWorld) -> None:
#         self.btbRegions.FillBtBRegionContainer(world)


# class BtBRegionContainer:
#     def __init__(self):
#         self.btbBank = None

#     def FillBtBRegionContainer(self, world: HenryStickminWorld):
#         self.btbBank = world.get_region("btbIntro")

# class EtPRegionContainer:
#     def __init__(self):
#         self.etpCell = None
#         self.etpCourtroom = None
#         self.etpCloset = None
#         self.etpRooftop = None
#         self.etpBathroom = None
#         self.etpLobby = None

#     def FillBtBRegionContainer(self, world: HenryStickminWorld):
#         self.etpCell = world.get_region("etpCell")
#         self.etpCourtroom = world.get_region("etpCourtroom")
#         self.etpCloset = world.get_region("etpCloset")
#         self.etpRooftop = world.get_region("etpRooftop")
#         self.etpBathroom = world.get_region("etpBathroom")
#         self.etpLobby = world.get_region("etpLobby")

# # class LocationContainer:
# #     def __init__(self):
# #         self.btbLocations = BtBLocationContainer()
# #         self.etpLocations = EtPLocationContainer()

# #     def GetBtBLocation(self):
# #         return self.btbLocation

# #     def GetEtPLocation(self):
# #         return self.etpLocation

# #     def FillLocationContainers(self, world: HenryStickminWorld) -> None:
# #         self.btbLocation.FillBtBLocationContainer(world)


# # class BtBLocationContainer:
# #     def __init__(self):
# #         self.btbBank = None

# #     def FillBtBLocationContainer(self, world: HenryStickminWorld):
# #         self.btbBank = world.get_region("btbIntro")

# # class EtPLocationContainer:
# #     def __init__(self):
# #         self.etpCell = None
# #         self.etpCourtroom = None
# #         self.etpCloset = None
# #         self.etpRooftop = None
# #         self.etpBathroom = None
# #         self.etpLobby = None

# #     def FillBtBLocationContainer(self, world: HenryStickminWorld):
# #         self.etpCell = world.get_region("etpCell")
# #         self.etpCourtroom = world.get_region("etpCourtroom")
# #         self.etpCloset = world.get_region("etpCloset")
# #         self.etpRooftop = world.get_region("etpRooftop")
# #         self.etpBathroom = world.get_region("etpBathroom")
# #         self.etpLobby = world.get_region("etpLobby")