from classes.room import Room
from config import config
from nps_list import *
import item_list

north = "север"
south = "юг"
east = "восток"
west = "запад"

corridor = Room(
    **config.description.corridor,
    creature=painting,
)
library = Room(**config.description.library, creature=madam)
ingredients_pantry = Room(**config.description.ingredients_pantry, blocked=True)
bathroom = Room(**config.description.bathroom, creature=mirtle)
office = Room(**config.description.office, creature=snape)
dungeon = Room(**config.description.dungeon)


dungeon.add_room({north: bathroom})
ingredients_pantry.add_room({east: corridor})
corridor.add_room(
    {north: library}, {east: office}, {south: bathroom}, {west: ingredients_pantry}
)
bathroom.add_room({north: corridor}, {south: dungeon})
office.add_room({west: corridor})
library.add_room({south: corridor})


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
