"""
CSCI-141 Week 9: Dictionaries & Dataclasses
Lab: 07-BabyNames
Author: RIT CS
Author: Nihal Wadhwa

This utility module is used by the main programs to perform the work on the
data and return the desired results.
"""

from dataclasses import dataclass
from operator import attrgetter, itemgetter
from typing import List

# the range of valid years of data
START_YEAR = 1880
END_YEAR = 2018

# indices into the name data when splitting by commas
NAME_INDEX = 0
GENDER_INDEX = 1
COUNT_INDEX = 2

# gender strings
FEMALE = 'F'
MALE = 'M'


def get_filename(year):
    """
    Returns a formatted string for the filename that is associated with a
    given year.
    :param year: the desired year
    :return: a string, e.g. 'yob1990.txt' if year is 1990
    """
    return f'yob{year}.txt'


"""
PROBLEM 1: tops_in_year
"""

@dataclass
class NameInfo:
    """
    A NameInfo structure is used to represent three pieces of data that are
    required by the tops_in_year main program.  For each name we want
    to record the gender and the total count of babies that were born
    in a particular year.
    """
    name: str     # baby's first name
    gender: str   # gender of baby, ('F' = female, 'M' = male)
    count: int    # total babies with the same name and gender born in a year


def get_tops_in_year(year, num=10):
    """
    For a particular year, find and return the top 'num' babies that were
    born in that year, sorted in descending order by counts.  By default
    'num' is 10.
    :param year: the year
    :param num: the top number of babies
    :return: tops: a list of NameInfo objects containing the top babies for that
        year in descending order by count.
    """
    bebes = []
    tops = []
    with open(get_filename(year)) as file:
        for line in file:
            fields = line.strip().split(',')
            name = fields[0]
            gender = fields[1]
            count = int(fields[2])
            bebes.append(NameInfo(name, gender, count))
    file.close()
    bebes.sort(key=attrgetter('count'), reverse=True)
    for i in range(num):
        tops.append(bebes[i])
    return tops



"""
PROBLEM 2: top_name_year
"""


@dataclass
class NameCount:
    """
    A NameCount structure is used to store the information required by
    the top_name_year main program.  In the year given, the top baby
    name of the year by total count, combining both genders, is to be
    found and returned.
    """
    name: str           # baby's first name
    count: int          # total babies with the same name (combining genders) in a year
    percentage: float   # how popular was the name in relation to all babies born that year


def get_top_name_year(year):
    """
    For a given year, find and return the top name, combining both genders if
    a name appears as both female and male.
    :param year: year to use when returning the top name
    :return:top_nameobj: the NameCount object of the top name of the given year
    """
    names = dict()
    all_count = 0
    percentage = 0
    with open(get_filename(year)) as file:
        for line in file:
            fields = line.strip().split(',')
            name = fields[0]
            count = int(fields[2])
            if name in names:
                names[name] += count
                all_count += count
            else:
                names[name] = count
                all_count += count
    file.close()
    top_name = max(names, key=names.get)
    percentage = (names[top_name]/all_count) * 100
    top_nameobj = NameCount(top_name, names[top_name], percentage)
    return top_nameobj









"""
PROBLEM 3: top_10_years
"""


@dataclass
class TopNamesYear:
    """
    A TopNamesYear structure is used by the top_10_years main program in order to find
    the top 'num' names over a range of years by total count.  It stores the
    female and male list of top names (strings).
    """
    females: List[str]     # list of top female names in descending order
    males: List[str]       # list of top male names in descending order


def get_top_years(start_year, end_year, num=10):
    """
    For a range of years, find and return the top 'num' female and male babies
    born over that range, in descending order.  By default 'num' is 10.
    :param start_year: the starting year (assumed to be valid)
    :param end_year: the ending year (assumed to be valid)
    :param num: the number of top names for each gender to generate
    :return: a TopNamesYear that holds the top female and male names in
    separate lists of strings.
    """
    m = dict()
    f = dict()
    m_final = list()
    f_final = list()
    for year in range(start_year, end_year+1):
        with open(get_filename(year)) as file:
            for line in file:
                fields = line.strip().split(',')
                name = fields[0]
                gender = fields[1]
                count = int(fields[2])
                if gender == MALE:
                    if name in m:
                        tempcount = m[name]
                        m[name] = count + tempcount
                    else:
                        m[name] = count
                elif gender == FEMALE:
                    if name in f:
                        tempcount = f[name]
                        f[name] = count + tempcount
                    else:
                        f[name] = count
        file.close()
    for i in range(num+1):
        temp_male = max(m, key=m.get)
        m_final.append(temp_male)
        m.pop(temp_male)
        temp_female = max(f, key=f.get)
        f_final.append(temp_female)
        f.pop(temp_female)
    return TopNamesYear(f_final, m_final)





