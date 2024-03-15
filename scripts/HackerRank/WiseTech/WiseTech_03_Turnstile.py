import math
import os
import random
import re
import sys

import queue
from collections import namedtuple
PersonRecord = namedtuple("PersonRecord", "idx time dir")

def get_next_person(enter_per, exit_per, last_used_time, last_used_dir):
    next_per = None
    
    min_time = min(exit_per.time, enter_per.time)
    max_time = max(exit_per.time, enter_per.time)
    if min_time > last_used_time + 1:
        # if there is gap in usage
        if enter_per.time == exit_per.time or exit_per.time < enter_per.time:
            # two persons arrived at the same time after a gap, or when exit arrived first
            next_per = exit_per
        else:
            # enter arrived first
            next_per = enter_per
    elif min_time == last_used_time + 1:
        # turnstile is in used
        if enter_per.time == exit_per.time:
            if last_used_dir == 0:
                next_per = enter_per
            else:
                next_per = exit_per
        elif enter_per.time < exit_per.time:
            next_per = enter_per
        else:
            next_per = exit_per
    elif max_time > last_used_time + 1:
        # one person in queue used the turnstile before another arrived
        if enter_per.time < exit_per.time:
            next_per = enter_per
        else:
            next_per = exit_per
    elif max_time <= last_used_time + 1:
        # one person in queue, another arrived then the turnstile is available
        # or when both persons are in queue
        if last_used_dir == 0:
            next_per = enter_per
        else:
            next_per = exit_per
    return next_per

def get_usage_time(p_record, last_used_time):
    if last_used_time < p_record.time:
        return p_record.time
    else:
        return last_used_time + 1

def getTimes(time, direction):
    res = [None for t in time]
    
    # arrange usage into 2 queue
    enter_q = queue.Queue()
    exit_q = queue.Queue()
    for idx in range(len(time)):
        rec = PersonRecord(idx, time[idx], direction[idx])
        #print(rec)
        if rec.dir > 0:
            exit_q.put(rec)
        else:
            enter_q.put(rec)
    
    last_used_time = -1
    last_used_dir = None
    enter_per = None if enter_q.empty() else enter_q.get()
    exit_per = None if exit_q.empty() else exit_q.get()
    while enter_per is not None or exit_per is not None:
        # one of the two queues is empty --> finishing the remaining queue
        if enter_per is None:
            next_per = exit_per
        elif exit_per is None:
            next_per = enter_per
        else:
            # main processing
            next_per = get_next_person(enter_per, exit_per, last_used_time, last_used_dir)
        usage_time = get_usage_time(next_per, last_used_time)
        res[next_per.idx] = usage_time
        last_used_time = usage_time
        last_used_dir = next_per.dir
            
        # update the queue
        if next_per.dir == 0:
            enter_per = None if enter_q.empty() else enter_q.get()
        else:
            exit_per = None if exit_q.empty() else exit_q.get()
        
    return res
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    time_count = int(input().strip())

    time = []

    for _ in range(time_count):
        time_item = int(input().strip())
        time.append(time_item)

    direction_count = int(input().strip())

    direction = []

    for _ in range(direction_count):
        direction_item = int(input().strip())
        direction.append(direction_item)

    result = getTimes(time, direction)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()