"""
file: test_link_sort.py
author: Nihal Wadhwa
description: tester for functions in linked_insort.py
"""

import linked_insort
import linked_code as link


def read_file( fname ):
    """
       Open a file of containing one integer per line,
       prepend each integer to a linked sequence,
       and return the reverse of the sequence.
       :param fname: A string containing the name of the file
       :return: lnk: A linked list of the numbers in the file, ordered
                identically to how they are ordered in the file
    """
    lst = []
    with open(fname) as file:
        for line in file:
            num = int(line.strip())
            lst.append(num)
    result = link.mk_linked_list_rec(lst)
    return link.reverse_rec(result)


def main():
    """
       Read file, build sequence, print it, sort it, print result, and
       pretty-print both lists.
    """

    name = input( "Enter file name: " )
    if name == "":
        return

    original_s = read_file( name )
    print( "unsorted:", original_s )

    sorted_s = linked_insort.insort( original_s )

    print( "sorted:", sorted_s )

    print( "pretty printed original: ", end="")
    linked_insort.pretty_print( original_s )
    print( "pretty printed sorted: ", end="")
    linked_insort.pretty_print( sorted_s )


if __name__ == "__main__":
    main()
