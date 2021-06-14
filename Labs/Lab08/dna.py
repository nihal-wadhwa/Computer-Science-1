"""
Nihal Wadhwa
Lab 08: DNA Toolkit
"""
import linked_code as lnk


def rev_rec(dna_seq):
    """
    Supporting function for the is_Palindrome function. Returns a linked list of the reverse order of elements of dna_seq
    :param dna_seq: linked list representing a dna sequence
    :return: linked list with

    """
    if dna_seq is None:
        return None
    else:
        return lnk.concatenate(rev_rec(dna_seq.rest), lnk.LinkNode(dna_seq.value, None))


def convert_to_nodes(dna_string):
    """
    Takes in a string of DNA and converts it into a linked list.
    :param dna_string: a string of characters corresponding to DNA bases
    :return: linked list of DNA bases
    """
    if dna_string == "":
        return None
    else:
        return lnk.LinkNode(dna_string[0], convert_to_nodes(dna_string[1:]))


def convert_to_string(dna_seq):
    """
    Takes in a linked list of DNA bases and coverts it into a string of DNA bases
    :param dna_seq: linked list of DNA bases
    :return: str: string of DNA bases
    """
    str = ""
    while dna_seq is not None:
        str += dna_seq.value
        dna_seq = dna_seq.rest
    return str


def is_match(dna_seq1, dna_seq2):
    """
    Takes in two linked lists of dna and check to see if they match
    :param dna_seq1: first linked list of DNA bases
    :param dna_seq2: second linked list of DNA bases
    :return: True if the two sequences match or False if they don't
    """
    if (dna_seq1 is None) and (dna_seq2 is None):
        return True
    elif (dna_seq1 is None) or (dna_seq2 is None):
        return False
    elif dna_seq1.value != dna_seq2.value:
        return False
    else:
        return is_match(dna_seq1.rest, dna_seq2.rest)


def is_pairing(dna_seq1, dna_seq2):
    """
    Takes in two dna sequences and checks to see if the corresponding pairs at each index are a valid DNA base pair
    :param dna_seq1: first linked list of DNA bases
    :param dna_seq2: second linked list of DNA bases
    :return: True if all pairs are valid and False if not all pairs are valid
    """
    result = False
    if (dna_seq1 is None) and (dna_seq2 is None):
        return True
    while (dna_seq1 is not None) and (dna_seq2 is not None):
        if ((dna_seq1.value == "A") and (dna_seq2.value == "T")) or (
                (dna_seq1.value == "T") and (dna_seq2.value == "A")):
            result = True
            dna_seq1 = dna_seq1.rest
            dna_seq2 = dna_seq2.rest
        elif ((dna_seq1.value == "G") and (dna_seq2.value == "C")) or (
                (dna_seq1.value == "C") and (dna_seq2.value == "G")):
            result = True
            dna_seq1 = dna_seq1.rest
            dna_seq2 = dna_seq2.rest
        else:
            return False
    if (dna_seq1 is not None) and (dna_seq2 is None):
        return False
    return result


def insertion(dna_seq1, dna_seq2, idx):
    """
    Takes in two sequences and inserts the second sequence at the index idx of the first sequence
    :param dna_seq1: the first sequence of bases
    :param dna_seq2: the second sequence of bases
    :param idx: index in the first sequence at which the second sequence is being inserted
    :return: new linked list with the inserted dna_seq2
    """

    if idx == 0:
        return lnk.concatenate(dna_seq2, dna_seq1)
    elif dna_seq1 is None:
        raise IndexError("invalid insertion index")
    else:
        return lnk.LinkNode(dna_seq1.value, insertion(dna_seq1.rest, dna_seq2, idx - 1))


def is_palindrome(dna_seq):
    """
    Takes in a sequence of bases and sees if it is a palindrome
    :param dna_seq: linked list of bases
    :return: True if it is a palindrome and False if it isn't
    """
    dna_seq2 = rev_rec(dna_seq)
    if dna_seq2 == dna_seq:
        return True
    else:
        return False


def substitution(dna_seq1, idx, base):
    """
    Takes in a sequence of bases and replaces a base at the index idx and replaces it with a base base
    :param dna_seq1: sequence of bases
    :param idx: index at which substitution occurs
    :param base: base being substituted
    :return: temp2: new linked list with the substitution
    """

    if idx > lnk.length_iter(dna_seq1):
        raise IndexError("Index out of Range in substitution")
    else:
        temp1 = lnk.insert_at(idx, base, dna_seq1)
        temp2 = lnk.remove_at(idx+1, temp1)
    return temp2


def deletion(dna_seq, idx, segment_size):
    """
    Takes a sequence of bases and deletes a segment with size segment_size, starting at the index idx
    :param dna_seq: sequence of bases
    :param idx: index where the deletion begins
    :param segment_size: length of segment being deleted
    :return: temp: new linked list with the segment removed
    """
    if (segment_size == 0):
        return dna_seq
    if (idx + segment_size > lnk.length_iter(dna_seq)) or (idx > lnk.length_iter(dna_seq)):
        raise IndexError("Index out of Range in deletion")
    else:
        tempidx = 0
        temp = dna_seq
        while dna_seq is not None:
            if idx == tempidx:
                while segment_size > 0:
                    temp = lnk.remove_at(tempidx, temp)
                    segment_size -= 1
            dna_seq = dna_seq.rest
            tempidx += 1
    return temp


def duplication( dna_seq, idx, segment_size ):
    """
    Takes in a sequence of bases duplicates a segment with size segment_size and inserts at right after the same segment
    , starting at index idx.
    :param dna_seq: sequence of bases
    :param idx: index where the duplicated sequence begins
    :param segment_size: the size of the duplicated segment
    :return: temp: new linked list with the duplicated segment
    """
    if (segment_size == 0):
        return dna_seq
    if (idx + segment_size > lnk.length_iter(dna_seq)) or (idx > lnk.length_iter(dna_seq)):
        raise IndexError("Index out of Range in deletion")
    else:
        temp = dna_seq
        segment = deletion(temp, 0, idx)
        segment = deletion(segment, segment_size, lnk.length_iter(dna_seq) - (segment_size+idx))
        temp = insertion(temp, segment, idx)
        return temp
