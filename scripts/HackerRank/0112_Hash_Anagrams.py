import math
import os
import random
import re
import sys

import copy

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def sherlockAndAnagrams(s):
    res = 0
    src = list(s)
    s_len = len(src)
    sub_s = {}
    for i in range(s_len - 1):
        for j in range(i, s_len):
            w = src[j]
            if w not in sub_s:
                sub_s[w] = 0
            sub_s[w] += 1
            
            # do the checking
            sub_len = j - i + 1
            for x in range(i + 1, s_len + 1 - sub_len):
                matched = True
                target_s = copy.deepcopy(sub_s)
                for w in src[x: x+sub_len]:
                    if (w not in target_s) or (target_s[w] <= 0):
                        # not an anagrams
                        matched = False
                        break
                    else:
                        target_s[w] -= 1
                
                if matched:
                    res += 1
        sub_s.clear()
        
    return res
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    #fptr.close()