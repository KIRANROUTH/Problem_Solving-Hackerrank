#Question Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

import math
import os
import random
import re
import sys
import calendar

def dayOfProgrammer(year):
    feb = 0
    if year >= 1700 and year <= 1917:
        if year%4 == 0:
            feb = 29
        else:
            feb = 28
    elif year >= 1919:
        if (year%4 == 0 and year%100 != 0) or year%400 == 0:
            feb = 29
        else:
            feb = 28
    elif year == 1918:
        if year%4 == 0:
            feb = 28 - 14
        else:
            feb = 29 - 14
    else:
        if calendar.isleap(year):
            feb = 28
        else:
            feb = 29
            
    su = 5*31 + 2*30 + feb
    val = 256 - su
    return "{}.09.{}".format(val, year)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
