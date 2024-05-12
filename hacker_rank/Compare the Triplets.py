#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    # Write your code here
    # final = []
    count1 = 0
    count2 = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            count1 += 1
        elif a[i] < b[i]:
            count2 += 1
    return [count1, count2]


if __name__ == '__main__':
    fptr = sys.stdout

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
