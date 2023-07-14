import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    m_words = {}
    for w in magazine:
        if w not in m_words:
            m_words[w] = 0
        m_words[w] += 1
    
    for w in note:
        if (w not in m_words) or (m_words[w] <= 0):
            print("No")
            return
        else:
            m_words[w] -= 1
    print("Yes")

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)