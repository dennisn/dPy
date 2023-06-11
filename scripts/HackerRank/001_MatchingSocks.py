import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    ar.sort()
    res = 0
    prev = None
    for i in ar:
        if prev is None:
            # new pair check
            prev = i
        elif prev == i:
            # found a pair --> count but discard this item
            res += 1
            prev = None
        else:
            # not a pair -> use 
            prev = i
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()