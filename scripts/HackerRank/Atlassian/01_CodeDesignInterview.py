
import time

cust_requests = {}
CONFIG_REQ_LIMIT = 2
CONFIG_TIME_LIMIT = 4

def rateLimit(cust_requests, cust_id, ts):
    res = True
    # ts = int(time.time())
    print("DEBUG: ", ts)
    if cust_id not in cust_requests:
        # brand new customer id
        cust_requests[cust_id] = [ts]
    else:
        # check if customer already make X requests for last Y seconds
        prev_requests = cust_requests[cust_id]
        count = 1
        i = 0
        for i in range(len(prev_requests) - 1, -1, -1):
            if ts - prev_requests[i] < CONFIG_TIME_LIMIT:
                # within time limit
                if count == CONFIG_REQ_LIMIT:
                    # more requests than allowed
                    res = False
                    break
                else:
                    count += 1
            else:
                # outside of time limit
                res = True
                break
        
        # just update the prev_requests list so we don't overgrown
        if i > 0:
            prev_requests = prev_requests[i:]
        if res:
            prev_requests.append(ts)
        cust_requests[cust_id] = prev_requests
        
    # return the result
    return res, cust_requests            
        
        
res, cust_requests = rateLimit(cust_requests, 1, 0)
print(res, " == ", cust_requests)
# time.sleep(1)
res, cust_requests = rateLimit(cust_requests, 1, 1)
print(res, " == ", cust_requests)

# time.sleep(3.5)
res, cust_requests = rateLimit(cust_requests, 1, 4.5)
print(res, " == ", cust_requests)

# time.sleep(1)
res, cust_requests = rateLimit(cust_requests, 1, 5.5)
print(res, " == ", cust_requests)
