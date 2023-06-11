import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps_1(arr):
    total_mismatch = 0
    mismatch_pair = 0
    for i in range(len(arr)):
        if arr[i] != i + 1:
            total_mismatch += 1
            if arr[arr[i] - 1] == i + 1:
                mismatch_pair += 1
                print("Pair: ", arr[i], i+1)
    single_mismatch = total_mismatch - mismatch_pair
    print("Total: ", total_mismatch, ", single: ", single_mismatch, ", pair: ", mismatch_pair)
    if single_mismatch > 0:
        single_swap = single_mismatch - 1
    print("Single swap:", single_swap, " + pair-swap:", mismatch_pair//2)
    return mismatch_pair//2 + single_swap

def minimumSwaps(arr):
    res = 0
    for i in range(len(arr)):
        expected_value = i + 1
        while arr[i] != expected_value:
            swap_pos = arr[i] - 1
            arr[i] = arr[swap_pos]
            arr[swap_pos] = swap_pos + 1
            res += 1
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()