#Question Link: https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[-2:] == "PM":
        l = s.split(":")
        if int(l[0]) < 12:
            l[0] = str(int(l[0]) + 12)
        l[-1] = l[-1][:len(l[-1]) - 2]
        return ":".join(l)
    elif s[-2:] == "AM":
        l = s.split(":")
        if int(l[0]) == 12:
            l[0] = "00"
            
        l[-1] = l[-1][:len(l[-1]) - 2]
        return ":".join(l)
    else:
        return s
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
