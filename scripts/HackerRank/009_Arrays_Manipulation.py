import math
import os
import random
import re
import sys
from dataclasses import dataclass

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation_1(n, queries):
    max_val = 0
    
    values = [0] * n
    
    for r in range(len(queries)):
        query = queries[r]
        for idx in range(query[0] - 1, query[1]):
            values[idx] += query[2]
    
    for i in range(n):
        if values[i] > max_val:
            max_val = values[i]
    return max_val

@dataclass
class Segment:
    value: int
    start: int
    end: int

def arrayManipulation(n, queries):
    segment_lst = [] # list of non-overlapped segments and their values
    for q in queries:
        new_s = Segment(q[2], q[0], q[1])
        #print("Processing ", q)
        #for s in segment_lst:
        #    print(s)
        #print("------------------")
        idx = 0
        insert_idx = -1
        while new_s is not None and idx < len(segment_lst):
            # check for overlapped of segment with this queries
            s = segment_lst[idx]
            #print("idx:", idx, " ==> ", s)
            if new_s.start < s.start:
                if new_s.end <= s.start:
                    # do nothing as it's not overlapped, but update the insert index
                    insert_idx = idx
                elif new_s.end <= s.end:
                    existing_start = s.start
                    if new_s.end < s.end:
                        # need to split current segment into overlapped and non-overlapped
                        overlapped_s = Segment(s.value + new_s.value, s.start, new_s.end)
                        segment_lst.insert(idx, overlapped_s)
                        # non overlapped part of current segment
                        s.start = new_s.end + 1
                    elif new_s.end == s.end:
                        # update value of the overlapped
                        s.value = s.value + new_s.value
                    # the new query remained front will be inserted infront of the current position
                    new_s.end = existing_start - 1
                    segment_lst.insert(idx, new_s)
                    new_s = None    # processing done
                elif new_s.end > s.end:
                    # update value of the overlapped
                    s.value = s.value + new_s.value
                    # insert the front-portion
                    front_s = Segment(new_s.value, new_s.start, s.start - 1)
                    segment_lst.insert(idx, front_s)
                    # the back portion is processed further
                    new_s.start = s.end + 1
            elif new_s.start == s.start:
                if new_s.end < s.end:
                    # the back portion of existing segment remained the same
                    s.start = new_s.end + 1
                    # the overlapped is updated to new value
                    new_s.value = new_s.value + s.value
                    segment_lst.insert(idx, new_s)
                    new_s = None    # processing done
                elif new_s.end == s.end:
                    # totally overlapped --> update value
                    s.value += new_s.value
                    new_s = None    # processing done
                elif new_s.end > s.end:
                    # update overlapped value
                    s.value = s.value + new_s.value
                    # new_s now only the non-overlapped part
                    new_s.start = s.end + 1
            elif new_s.start <= s.end:
                if new_s.end <= s.end:
                    if new_s.end == s.end:
                        # add a non-overlap segment
                        non_overlap_s = Segment(s.value, s.start, new_s.start - 1)
                        segment_lst.insert(idx, non_overlap_s)
                        # udpate value of the overlapped segment
                        s.value = s.value + new_s.value
                        s.start = new_s.start
                    else:
                        # add the overlapped segment
                        overlap_s = Segment(s.value + new_s.value, new_s.start, new_s.end)
                        segment_lst.insert(idx, overlap_s)
                        # add a non-overlap segment
                        non_overlap_s = Segment(s.value, s.start, new_s.start - 1)
                        segment_lst.insert(idx, non_overlap_s)
                        # udpate value of the back non-overlap segment
                        s.start = new_s.end + 1
                    new_s = None    # processing done
                elif new_s.end > s.end:
                    # add the non-overlap segment
                    non_overlap_s = Segment(s.value, s.start, new_s.start - 1)
                    segment_lst.insert(idx, non_overlap_s)
                    # update value of the overlapped part
                    s.start = new_s.start
                    s.value = s.value + new_s.value
                    # continue processing with the non-overlapped
                    new_s.start = s.end + 1
            else:
                # do nothing as it's totally not overlapped
                None
            
            # move to next segment
            idx += 1
            #for s in segment_lst:
            #    print(s)
            #print("+++++++++++++++++++++")
            #print("New segment: ", new_s)
        
        # not overlap, then create a new segment to represent this query
        # insert this new segment to the index above
        if new_s is not None:
            segment_lst.insert(insert_idx, new_s)
            
        #for s in segment_lst:
        #    print(s)
        #print("============================")
    
    max_value = 0
    for s in segment_lst:
        if s.value > max_value:
            max_value = s.value
    return max_value
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()