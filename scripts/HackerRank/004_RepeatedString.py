import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    partial_idx = n % len(s)
    dup_count = n // len(s)
    total_count = 0
    partial_count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            total_count += 1
            if i < partial_idx:
                partial_count += 1
    return total_count * dup_count + partial_count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()