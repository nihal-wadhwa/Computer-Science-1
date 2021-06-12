"""
Nihal Wadhwa
Homework 08: Linear Sort
A visual of the complexities of the quick, merge, bumper, and linear sort compared to each other
"""

import random
import time
from merge_sort import merge_sort
from quick_sort import quick_sort

MAX_NUM = 300



def bumper_sort(data,k):
    """
    Takes histogram of the original list and converts it back into a sorted order in a different list
    """
    hist = [0] * (k+1)
    for v in data:
        hist[v] = hist[v]+1
        result = []
    for i in range(0,len(hist)):
        j = hist[i]
        while j >0:
            result.append(i)
            j = j-1
    return result


def warmup_test():
    """
    Tests the bumper_sort function
    """
    test = [2,5,3,0,2,3,0,3]
    print("Small List, unsorted:", test)
    print("Small List, bump-sorted:",bumper_sort(test,5))
    test_2=[]
    for n in range(0,1000):
        test_2.append(random.randint(0,MAX_NUM))
    print("Large List, unsorted:",test_2)
    print("Large List, bump-sorted:", bumper_sort(test_2,MAX_NUM),"\n")


def perfcompare_test():
    """
    Compares the time it takes sorting two different lists (one small, one large) using four different sorts for each list.
    """
    small = []
    for n in range(0,1000):
        small.append(random.randint(0,MAX_NUM))
        
    big = []
    for n in range(0,1000000):
        big.append(random.randint(0,MAX_NUM))
        
    print("Sorting a randomized list of 1000 elements.")
    merge_small_1 = time.time()
    merge_sort(small)
    merge_small_2 = time.time()
    print("merge_sort time:",merge_small_2 - merge_small_1, "seconds")
    
    quick_small_1 = time.time()
    quick_sort(small)
    quick_small_2 = time.time()
    print("quick_sort time:", quick_small_2 - quick_small_1, "seconds")
    
    bumper_small_1 = time.time()
    bumper_sort(small,MAX_NUM)
    bumper_small_2 = time.time()
    print("bumper_sort time:", bumper_small_2 - bumper_small_1, "seconds")
    
    sort_small_1 = time.time()
    small.sort()
    sort_small_2 = time.time()
    print("sorted time:", sort_small_2 - sort_small_1, "seconds", "\n")

    print("Sorting a randomized list of 1000000")
    merge_big_1 = time.time()
    merge_sort(big)
    merge_big_2 = time.time()
    print("merge_sort time:", merge_big_2 - merge_big_1, "seconds")
    
    quick_big_1 = time.time()
    quick_sort(big)
    quick_big_2 = time.time()
    print("quick_sort time:", quick_big_2 - quick_big_1, "seconds")
    
    bump_big_1 = time.time()
    bumper_sort(big,MAX_NUM)
    bump_big_2 = time.time()
    print("bumper_sort time:", bump_big_2 - bump_big_1, "seconds")
    
    sort_big_1 = time.time()
    big.sort()
    sort_big_2 = time.time()
    print("sorted time:", sort_big_2 - sort_big_1, "seconds")



def main():
    bumper_sort([2,5,3,0,2,3,0,3],5)
    warmup_test()
    perfcompare_test()
    
if __name__ == '__main__':
    main()
    
