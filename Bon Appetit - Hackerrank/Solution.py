#Question Link: https://www.hackerrank.com/challenges/bon-appetit/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def bonAppetit(bill, k, b):
    su = 0
    for x in range(len(bill)):
        if x != k:
            su += bill[x]
    su = su//2
    if su == b:
        print("Bon Appetit")
    else:
        print(b - su)
    return None

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
