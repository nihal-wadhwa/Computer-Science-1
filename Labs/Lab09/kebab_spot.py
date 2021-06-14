"""
A dataclass that represents "spots" on the skewer and functions that work
with it.

author: RITCS
author: Nihal Wadhwa
"""

from dataclasses import dataclass
from typing import Union
from food import Food

@dataclass
class KebabSpot:
    """
    Class: KebabSpot
    Description: This class is used to represent an individual
        spot on the skewer.  Each spot contains a Food 'item',
        and a reference to the 'next' spot.
    """
    item: Food
    next: Union[None, 'KebabSpot']


def spot_create(item, next):
    """
    Create a new food item spot on the skewer
    :param item (Food): new food item
    :param next: next spot
    :return: new spot
    """
    return KebabSpot(item, next)


def spot_name(spot):
    """
    Return the name of the food item in this spot.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: food name
    """
    return spot.item.name

def spot_size(spot):
    """
    Return the number of elements from this KebabSpot instance to the end
    of the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :return: the number of elements (int)
    """
    size = 0
    while spot is not None:
        size += 1
        spot = spot.next
    return size

def spot_has(spot, name):
    """
    Return whether there are is a food item from this spot to the end of
    the skewer.
    :param: spot (KebabSpot): the current spot on the skewer
    :param name: the name (string) being searched for.
    :return True if any of the spots hold a Food item that equals the
    name, False otherwise.
    """
    while spot is not None:
        if spot.item.name == name:
            return True
        spot = spot.next
    return False

def spot_string_em(spot):
    """
    Return a string that contains the list of items in the skewer from
    this spot down, with a comma after each entry.
    :param: spot (KebabSpot): the current spot on the skewer
    :return A string containing the names of each of the Food items from
    this spot down.
    """
    string = str()
    while spot is not None:
        string = string + " , " + spot.item.name
        spot = spot.next
    return string


def spot_calories(spot):
    total = 0
    while spot is not None:
        total += spot.item.calories
        spot = spot.next
    return total


def spot_vegan(spot):
    while spot is not None:
        if spot.item.veggie is True:
            spot = spot.next
        else:
            return False
