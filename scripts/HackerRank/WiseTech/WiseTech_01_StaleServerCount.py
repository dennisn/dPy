import math
import os
import random
import re
import sys
import copy

def getStaleServerCount(n, log_data, query, X):
    servers = {x+1 for x in range(n)}
    # set up the result set
    res = []
    for q in query:
        # at first, assume all servers are stale for each query
        q_res = copy.deepcopy(servers)
        q_min = q - X
        for data in log_data:
            if data[0] not in q_res:
                continue    # this server is not stale
            
            # this server is still in question, so do the check
            if data[1] >= q_min and data[1] <= q:
                q_res.remove(data[0])
                if len(q_res) == 0:
                    break
        
        # finished checking this query --> record the result
        res.append(len(q_res))
    return res

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    n = int(input().strip())

    log_data_rows = int(input().strip())
    log_data_columns = int(input().strip())

    log_data = []

    for _ in range(log_data_rows):
        log_data.append(list(map(int, input().rstrip().split())))

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = int(input().strip())
        query.append(query_item)

    X = int(input().strip())

    result = getStaleServerCount(n, log_data, query, X)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()