#Question Link: https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
'''
def migratoryBirds(arr):
    co = 0
    no = 0
    for x in arr:
        val = arr.count(x)
        if val > no:
            no = val
            co = x
        if val == no:
            if co > x:
                co = x
    return co'''
def migratoryBirds(arr):
    dicti = dict()
    for x in arr:
        if str(x) not in list(dicti.keys()):
            dicti[str(x)] = 1
        else:
            dicti[str(x)] += 1
    val = max(list(dicti.values()))
    result = []
    for key, value in dicti.items():
        if value == val:
            result.append(int(key))
    return min(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
