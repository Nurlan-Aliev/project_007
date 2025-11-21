from classes.bag import Bag
from config import config
from nps_list import painting
from item_list import *


def corridor(hero):
    room = {
        "name": "Corridor of living pictures",
        "description": config.description.corridor,
        "creature": painting,
        "items": Bag(),
    }


def library(hero):
    room = {
        "name": "library",
        "description": config.description.library,
        "creature": None,
        "items": Bag(book1, book2, book3),
    }


def ingredients_pantry(hero):
    pass


def bathroom(hero):
    pass


def office(hero):
    pass
