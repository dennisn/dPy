import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    total_brides = 0
    total_len = len(q)
    org_q = [x+1 for x in range(total_len)]
    for i in range(total_len):
        if org_q[i] != q[i]:
            if i < total_len-1 and org_q[i+1] == q[i]:
                # one bride
                temp = org_q.pop(i+1)
                org_q.insert(i, temp)
                #print("Insert ", temp, " at pos: ", i-1, "=>", org_q)
                total_brides += 1
            elif i < total_len-2 and org_q[i+2] == q[i]:
                # two brides
                temp = org_q.pop(i+2)
                org_q.insert(i, temp)
                #print("Insert ", temp, " at pos: ", i-1, "=>", org_q)
                total_brides += 2
            else:
                print("Too chaotic")
                return
                #print(i, " - org:", org_q[i], " vs. q:", q[i])
    print(total_brides) 

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)