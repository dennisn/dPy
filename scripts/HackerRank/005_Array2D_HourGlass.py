import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def sum_row_3(row_data):
    res = []
    cum_sum = row_data[0]
    for i in range(5):
        cum_sum += row_data[i + 1]
        if i < 1:
            res.append(0)
        else:
            res.append(cum_sum)
            cum_sum -= row_data[i - 1]
    res.append(0)
    return res

def hourglassSum(arr):
    # Write your code here
    sum_3 = []
    for i in range(6):
        sum_3_row = sum_row_3(arr[i])
        sum_3.append(sum_3_row)

    # calc. the hour-glass value, and compare to current max
    cur_max = None
    for r in range(1,5):
        for c in range(1, 5):
            val = arr[r][c] + sum_3[r-1][c] + sum_3[r+1][c]
            if cur_max is None or cur_max < val:
                cur_max = val
    return cur_max


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()