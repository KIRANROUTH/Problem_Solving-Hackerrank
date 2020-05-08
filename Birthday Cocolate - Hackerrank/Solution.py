#Question Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    le = 0
    for x in range(len(s) - m + 1):
        su = sum(s[x : x + m])
        if su == d:
            le += 1
    return le

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
