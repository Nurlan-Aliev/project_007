from classes.room import Room
from config import config
from nps_list import *
from item_list import *

corridor = Room("Corridor of living pictures", config.description.corridor, painting)
library = Room("Library", config.description.library)
ingredients_pantry = Room("Ingredients ingredients_pantry", config.description.ingredients_pantry)
bathroom = Room("Ladies’ bathroom", config.description.bathroom)
office = Room("Professor Snake's office", config.description.office, snape)
dungeon = Room("Dungeon/Potion Brewing", config.description.dungeon)


dungeon.add_room(ingredients_pantry)
ingredients_pantry.add_room(dungeon, corridor)
corridor.add_room(library, office, bathroom, ingredients_pantry)
bathroom.add_room(corridor)
office.add_room(corridor)
library.add_room(corridor)


office.items.add(bottle, bottle, bottle, note)
library.items.add(book1, book2, book3)
ingredients_pantry.items.add(
    pearl_powder, troll_whisker, dragon_blood, fairy_wings, rougarou_fur
)
