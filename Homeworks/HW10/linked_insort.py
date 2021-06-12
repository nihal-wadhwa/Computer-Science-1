"""
file: linked_insort.py
author: Nihal Wadhwa
description: homework
"""

import linked_code as link


def insert( value, lnk ):
    """
    Put the value in the proper spot in the linked list to keep it sorted.
    New nodes are created.
    :param value: the value to add to the sequence of values in the list
    :param lnk: the node at the head of the list
    :return: a (partially) new linked list with the value inserted
    :pre: the list headed by lnk is sorted.
    :post: the link returned refers to a list that is sorted.
    """

    if lnk is None:
        return link.LinkNode(value, None)
    elif value > lnk.value:
        return link.LinkNode(lnk.value, insert(value, lnk.rest))
    elif value <= lnk.value:
        return link.LinkNode(value, lnk)


def insort( lnk ):
    """
    Return a copy of a linked list where all the values are sorted,
    with the lowest value at the head.
    :param lnk: the node at the head of the provided list
    :return: the head node of the sorted linked list
    """

    lnk_sort = None
    while lnk is not None:
        lnk_sort = insert(lnk.value, lnk_sort)
        lnk = lnk.rest
    return lnk_sort


def pretty_print( lnk ):
    """
    Print the contents of a linked list in standard Python format.
    [value, value, value] (Note the spaces.)
    :param lnk: the node at the head of the provided list
    :return: lst: list of the values in the linked list lnk
    """
    lst = []
    while lnk is not None:
        lst.append(lnk.value)
        lnk = lnk.rest
    print(lst)