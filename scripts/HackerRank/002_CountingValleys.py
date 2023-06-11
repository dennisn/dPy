import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    res = 0
    cur_alt = 0
    for i in range(steps):
        if path[i] == 'U':
            cur_alt += 1
        else:
            cur_alt -= 1
            # check if we're entering valley first time
            if cur_alt == -1:
                res += 1
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()