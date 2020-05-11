#Question Link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def catAndMouse(x, y, z):
    val1, val2 = 0, 0
    if x < z + 1:
        for x in range(x, z + 1):
            val1 += 1
    else:
        for x in range(z, x + 1):
            val1 += 1
    if y < z + 1:
        for y in range(y, z + 1):
            val2 += 1
    else:
        for y in range(z, y + 1):
            val2 += 1
            
    if val1 == val2:
        return "Mouse C"
    if val1 > val2:
        return "Cat B"
    else:
        return "Cat A"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
