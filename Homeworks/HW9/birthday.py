"""
Nihal Wadhwa
Homework 9: Birthdays
"""


from dataclasses import dataclass

@dataclass(frozen = True)
class Birthday:
    month: str
    day: int
    year: int

def build_dictionary(filename):
    """
    Creates a dictionary from a file with birthdays. The dictionaries will have a Birthday object as the key and the
    number of times it appears in the file as the value.
    :param filename: name of the file of birthday dates
    :return: birthdays: dictionary of Birthday objects and a counter as the value
    """
    birthdays = dict()
    with open(filename) as file:
        for line in file:
            fields = line.strip().split(' ')
            month= fields[0]
            day = int(fields[1])
            year = int(fields[2])
            temp = Birthday(month, day, year)
            if temp in birthdays:
                birthdays[temp] += 1
            else:
                birthdays[temp] = 1
    return birthdays


def birthdays_atleast(bd_counts, min_count):
    """
    Creates a list of birthday objects from dictionary, bd_counts, that occurred at least min_count times
    :param bd_counts: list of birthday objects
    :param min_count: number of times the birthday should AT LEAST occur
    :return: lst: list of birthday objects that occurred at least min_count times
    """
    lst = []
    for key in bd_counts:
        if bd_counts[key] >= min_count:
            lst.append(key)
    return lst

def to_strings(list_birthdays):
    """
    Takes a list of birthday objects as an input and creates a list of converted birthdays in the format of
    month/day/year
    :param list_birthdays: list of birthday objects
    :return: dash_dates: list of converted birthdays in format month/day/year
    """
    dash_dates = []
    months = {'JAN': '1', 'FEB': '2', 'MAR': '3', 'APR': '4', 'MAY': '5', 'JUN': '6', 'JUL': '7', 'AUG': '8', 'SEP': '9', 'OCT': '10', 'NOV': '11', 'DEC': '12'}
    for bday in list_birthdays:
        month = months[bday.month]
        birthday = month + "/" + str(bday.day) + "/" + str(bday.year)
        dash_dates.append(birthday)
    return dash_dates



def main():
    """
    Tests the program by taking a file of 20,000 birthdays and takes an input of minimum count. The program then
    prints the birthday objects that occur a minimum of min-count times and converts those objects to the format month/day/year
    :return: None
    """
    bd_counts = build_dictionary("birthday20000.txt")
    min_count = int(input("Enter a minimum count: "))
    list_birthdays = birthdays_atleast(bd_counts, min_count)
    print("Birthdays occurred at least " + str(min_count) + " times:")
    print(list_birthdays)
    print()
    list_strings = to_strings(list_birthdays)
    print(list_strings)


main()
