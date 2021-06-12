"""
Author: Nihal Wadhwa
Homework 07: Biggie Sort
"""

"""
1. The insertion sort would work better when the test case is a list that is almost sorted or completely sorted, where 
most of the elements are almost if not completely sorted from least to greatest.

2. This is because insertion sort inserts all the smallest numbers to the beginning of the list and when the list is 
already almost completely sorted, it is quite easy because all the smallest numbers are already in the beginning. Biggie
sort, however, requires that you check the max of the list and put that element to the back and then do that for the
rest of the elements, excluding that max element. So, since the numbers are almost sorted, biggie sort will still have
to go though the list repeatedly and put the max at the back. int-ran
"""


def swap(lst, idx1, idx2):
    temp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = temp


def find_max_from(lst,idx1, idx2):
    bignum = 0
    bigindex = 0
    for index in range(idx1, idx2+1):
        if lst[index] > bignum:
            bignum = lst[index]
            bigindex = index
        index += 1
    return bigindex


def biggiesort(lst):
    for mark in range(len(lst)-1, -1, -1):
        swap(lst, mark, find_max_from(lst,  0, mark))
    return lst

def main():
    inp = input("Enter filename: ")
    file = open(inp)
    lst = []
    for line in file:
        lst.append(int(line))
    print("Sorting File: " + inp)
    print("unsorted: ", lst)
    print("sorted: ", biggiesort(lst))


main()