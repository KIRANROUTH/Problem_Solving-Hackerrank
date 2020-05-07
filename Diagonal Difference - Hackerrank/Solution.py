#Question Link: https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    sum1, sum2 = 0, 0
    right = len(arr[0]) - 1
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if x == y:
                sum1 += arr[x][y]
        sum2 += arr[x][right]
        right -= 1
    result = abs(sum1 - sum2)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
