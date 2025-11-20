from classes.room import Room
from config import config
from nps_list import *
import item_list

corridor = Room(
    **config.description.corridor,
    creature=painting,
)
library = Room(**config.description.library, creature=madam)
ingredients_pantry = Room(**config.description.ingredients_pantry, blocked=True)
bathroom = Room(**config.description.bathroom, creature=mirtle)
office = Room(**config.description.office, creature=snape)
dungeon = Room(**config.description.dungeon)


dungeon.add_room(ingredients_pantry)
ingredients_pantry.add_room(dungeon, corridor)
corridor.add_room(library, office, bathroom, ingredients_pantry)
bathroom.add_room(corridor)
office.add_room(corridor)
library.add_room(corridor)


office.items.add(
    item_list.asphodel_leaves,
    item_list.moonstone,
    item_list.empty_vial,
    item_list.note,
)

library.items.add(item_list.book1, item_list.book2, item_list.book3)
ingredients_pantry.items.add(
    item_list.pearl_dust,
    item_list.troll_whisker,
    item_list.dragon_blood,
    item_list.fairy_wings,
    item_list.rougarou_fur,
)
