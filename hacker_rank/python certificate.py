# import os


# def avg(num):
#     sum=0
#     for i in range(len(num)):
#         sum+=num[i]
#     print(sum)
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
#     nums = list(map(int, input().split()))
#     res = avg(*nums)
    
#     fptr.write('%.2f' % res + '\n')

#     fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'missingCharacters' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

import sys

def missingCharacters(s):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyz'
    missing = sorted(set(all_chars) - set(s))
    return ''.join(missing)

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = missingCharacters(s)

    fptr.write(result + '\n')

