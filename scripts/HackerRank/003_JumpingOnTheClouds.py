import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    i = 0
    jump_count = 0
    while i < len(c) - 1:
        if i + 2 < len(c) and c[i+2] == 1:
            # can't jump 2 steps, so settle with 1 only
            i = i + 1
        else:
            # jump 2 steps
            i = i + 2
        jump_count += 1
    return jump_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()