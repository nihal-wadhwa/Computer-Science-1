"""
Lab 6: Laser Towers
Author: Nihal Wadhwa
Program determines optimal laser tower placements from list of numbers
"""

import sys


def lis_file(file):
    """
    Creates a list from a text file
    :param file: name of file including file type
    :return: list of values found in file
    """
    f = file.open()
    lst = []
    for line in f:
        lst = list.split(" ")
    return lst


def find_max(lst):
    """
    Finds the maximum number and returns the index of said number in the list
    :param lst: list of values
    :return: index of maximum value
    """
    bignum = 0
    bigindex = 0
    for index in range(len(lst) - 1):
        if lst[index] > bignum:
            bignum = lst[index]
            bigindex = index
        index += 1
    return bigindex


def tower(listfile, numtowers):
    """
    Prints optimal laser tower placements
    :param listfile: list of numbers
    :param numtowers: number of towers required to print
    :return: None
    """
    sums = []
    tri_list = []
    up_down_list = []
    for i in range(len(listfile) - 3):
        tow_sum = 0
        temptower = []
        for num in range(i, i + 4):
            if num - i == 1:
                if listfile[num] < listfile[num + 1]:
                    tri_list.append(num)
                    tow_sum -= listfile[num]
                    up_down_list.append("upward")
                elif listfile[num + 1] < listfile[num]:
                    tri_list.append(num + 1)
                    tow_sum -= listfile[num + 1]
                    up_down_list.append("downward")
                elif listfile[num + 1] == listfile[num]:
                    tri_list.append(num + 1)
                    tow_sum -= listfile[num + 1]
                    up_down_list.append("downward")
            temptower.append(listfile[num])
            tow_sum += listfile[num]
        sums.append(tow_sum)
    tri_index = []
    while numtowers > 0:
        comb = 0
        sum = 0
        used = False
        comb = find_max(sums)
        sum = sums[comb]
        for idx1 in range (0, len(tri_index)):
            if tri_list[comb] == tri_index[idx1]:
                used = True
                sums[comb] = -1
        if used == False:
            print("Centered at location", tri_list[comb], "facing", up_down_list[comb], "scoring", sum)
            sums[comb] = -1
            tri_index.append(tri_list[comb])
            numtowers -= 1


def main():
    """
    Takes user input for file name and number of laser towers. Prints the optimal laser tower placements
    :return: None
    """
    if len(sys.argv) != 3:
        print("Usage: lasers.py laser-file num-towers")
    else:
        numFile = sys.argv[1]
        lst = lis_file(open(numFile))
        tower(lst, int(sys.argv[2]))

main()
