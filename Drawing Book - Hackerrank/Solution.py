#Question Link: https://www.hackerrank.com/challenges/drawing-book/problem
#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    lis = []
    for x in range(1, n + 2, 2):
        if x > n and n % 2 == 0:
            lis.append((x - 1, 0))
            break
        lis.append((x - 1, x))
    ind = 0
    for x, y in lis:
        if x == p or y == p:
            ind = lis.index((x, y))
    val1 = ind
    val2 = len(lis) - ind - 1
    if val1 > val2:
        return val2
    else:
        return val1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
