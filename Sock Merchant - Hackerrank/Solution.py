#https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    pair = 0
    dicti = dict()
    for x in ar:
        if str(x) not in list(dicti.keys()):
            dicti[str(x)] = 0
        if str(x) in list(dicti.keys()):
            dicti[str(x)] += 1

    for value in list(dicti.values()):
        if value > 1:
            if value % 2 == 0:
                pair += value / 2
            else:
                a = value
                a -= 1
                pair += a / 2
            
    return int(pair)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
