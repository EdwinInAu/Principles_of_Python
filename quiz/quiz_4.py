# Uses Heath Nutrition and Population statistics,
# stored in the file HNP_Data.csv.gz,
# assumed to be located in the working directory.
# Prompts the user for an Indicator Name. If it exists and is associated with
# a numerical value for some countries or categories, for some the years 1960-2015,
# then finds out the maximum value, and outputs:
# - that value;
# - the years when that value was reached, from oldest to more recents years;
# - for each such year, the countries or categories for which that value was reached,
#   listed in lexicographic order.
#
# Written by Chongshi Wang and Eric Martin for COMP9021

import sys
import os
import csv
import gzip
from collections import defaultdict
filename = 'HNP_Data.csv.gz'
if not os.path.exists(filename):
    print(f'There is no file named {filename} in the working directory, giving up...')
    sys.exit()

indicator_of_interest = input('Enter an Indicator Name: ')

first_year = 1960
number_of_years = 56
max_value = None
countries_for_max_value_per_year = {}
with gzip.open(filename) as csvfile:
    file = csv.reader(line.decode('utf8').replace('\0', '') for line in csvfile)
    countries_for_max_value_per_year = defaultdict(list)
    max = 0
    for item in file:
        if len(item) > 3:
            if item[2] == indicator_of_interest:
                for i in range(56):
                    if item[4+i] != '':
                        if float(item[4+i]) > max:
                            max = float(item[4+i])
                            countries_for_max_value_per_year.clear()
                            countries_for_max_value_per_year[1960+i].append(item[0])
                        elif float(item[4+i]) == max:
                            countries_for_max_value_per_year[1960+i].append(item[0])
                            
if  max != 0:
    if max == round(max):
            max_value = int(max)
    else :
        max_value = max
if max_value is None:
    print('Sorry, either the indicator of interest does not exist or it has no data.')
else:
    print('The maximum value is:', max_value)
    print('It was reached in these years, for these countries or categories:')
    print('\n'.join(f'    {year}: {countries_for_max_value_per_year[year]}'
                    for year in sorted(countries_for_max_value_per_year)
                    )
          )