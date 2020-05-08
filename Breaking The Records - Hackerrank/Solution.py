#https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def breakingRecords(scores):
    chi, clo = scores[0], scores[0]
    res = [0, 0]
    for x in scores:
        if x > chi:
            res[0] += 1
            chi = x
        if x < clo:
            res[1] += 1
            clo = x
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
