"""
Homework 11: Droid Factory
Author: Nihal Wadhwa
This program is designed to simulate a droid factory using queues.
"""

import cs_queue as q
import node as n
from dataclasses import dataclass


@dataclass()
class Droid:
    serialnum: int
    head: bool
    body: bool
    arms: bool
    legs: bool


def unload(parts):
    """
    Takes a file of droid parts and converts it into a queue of parts representative of a conveyer belt
    :param parts: file with droid parts
    :return: convbelt: queue of droid parts
    """
    convbelt = q.make_empty_queue()
    with open(parts) as file:
        for line in file:
            part = line.strip().split('\n')
            q.enqueue(convbelt, part)
    return convbelt


def make_droid(serial, belt):
    """
    Makes a single droid from a conveyer belt (queue) of droid with its own serial number serial
    :param serial: serial number of droid
    :param belt: queue of conveyer belt of droids
    :return: size of conveyer belt
    """
    print("Building a new droid with serial number:", serial)
    droid = Droid(serial, False, False, False, False)
    part = q.dequeue(belt)
    while (
            (droid.head is False) or (droid.arms is False) or (droid.body is False) or (droid.legs is False)
    ):
        if part == ['arms'] and (droid.arms is False):
            droid.arms = True
            if belt.size != 0:
                part = q.dequeue(belt)
            print("attaching arms...")
        elif part == ['head'] and (droid.head is False):
            droid.head = True
            if belt.size != 0:
                part = q.dequeue(belt)
            print("attaching head...")
        elif part == ['legs'] and (droid.legs is False):
            droid.legs = True
            if belt.size != 0:
                part = q.dequeue(belt)
            print("attaching legs...")
        elif part == ['body'] and (droid.body is False):
            droid.body = True
            if belt.size != 0:
                part = q.dequeue(belt)
            print("attaching body...")
        else:
            q.enqueue(belt, part)
            print("placing unneeded part back on belt:", part[0])
            part = q.dequeue(belt)
    if (droid.head is True) and (droid.arms is True) and (droid.body is True) and (droid.legs is True):
        print("Droid", str(serial), "has been assembled!")
    if (belt.size > 1):
        q.enqueue(belt, part)
    return belt.size


def buildarmy(belt):
    """
    Takes a coveyer belt of parts and makes all the droids possible with the parts provided
    :param belt: queue of parts
    :return: none
    """
    serial = 10000
    print("Starting a shift at the droid factory!")
    while belt.size > 0:
        make_droid(serial, belt)
        serial += 1
    if belt.size == 0:
        print("All Droids have been assembled! Time to clock out and play Sabacc...")
    return serial


def main():
    """
    Takes user input of the file name of parts and uses it to create all droids possible
    :return: none
    """
    filename = input("Enter filename: ")
    belt = unload(filename)
    buildarmy(belt)


def testallfunc():
    """
    Tests all the functions
    :return: none
    """

    print("Testing Task 1:")
    droid = Droid(12345, True, False, False, True)
    print(droid.head is True, end=" ")
    print(droid.body is False, end=" ")
    print(droid.arms is False, end=" ")
    print(droid.legs is True, end=" ")
    print(droid.serialnum == 12345, end="\n")

    print("Testing Task 2 using test files droid_parts_1, droid_parts_3, droid_parts_5: ")
    belt = unload("droid_parts_1.txt")
    print(belt.front.value == ['head'] and belt.back.value == ['legs'] and belt.size == 4, end=" ")
    belt = unload("droid_parts_3.txt")
    print(belt.front.value == ['arms'] and belt.back.value == ['arms'] and belt.size == 12, end=" ")
    belt = unload("droid_parts_5.txt")
    print(belt.front.value == ['arms'] and belt.back.value == ['body'] and belt.size == 20, end="\n")

    print("Testing Task 3 using test files droid_parts_1:")
    print(make_droid(10000, unload("droid_parts_1.txt")) == 0, end="\n")

    print("Testing Task 4 using test files droid_parts_1, droid_parts_3, droid_parts_5:")
    print(buildarmy(unload("droid_parts_1.txt")) == 10001, end="\n")
    print(buildarmy(unload("droid_parts_3.txt")) == 10003, end="\n")
    print(buildarmy(unload("droid_parts_5.txt")) == 10005, end="\n")


main()