from classes.room import Room
from nps_list import *

corridor = Room("Corridor of living pictures", painting)
library = Room("Library")
pantry = Room("Ingredients pantry")
passage = Room("Ktiny passage")
office = Room("Professor Snake's office", snape)
dungeon = Room("Dungeon/Potion Brewing")


dungeon.add_room(pantry)
pantry.add_room(dungeon, corridor)
corridor.add_room(library, office, passage)
office.add_room(corridor)
library.add_room(corridor)
