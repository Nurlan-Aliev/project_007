from classes.room import Room
from nps_list import *
from item_list import *

corridor = Room(
    "Corridor of living pictures", "a long corridor with living pictures", painting
)
library = Room("Library", None)
pantry = Room("Ingredients pantry", None)
passage = Room("Ktiny passage", None)
office = Room(
    "Professor Snake's office",
    "In a dim room you see a table with a candle on it,"
    " a pile of papers, an open cabinet next to it, several bottles in the cabinet,"
    " and parchment with some kind of recipe",
    snape,
)
dungeon = Room("Dungeon/Potion Brewing", None)


dungeon.add_room(pantry)
pantry.add_room(dungeon, corridor)
corridor.add_room(library, office, passage, pantry)
passage.add_room(corridor)
office.add_room(corridor)
library.add_room(corridor)


office.items.add(bottle, bottle, bottle, note)
library.items.add(books1, books2, books3, books4, books5)
