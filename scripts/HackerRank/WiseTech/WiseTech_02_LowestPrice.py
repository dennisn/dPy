import math
import os
import random
import re
import sys

# constants, should be defined outside
EMPTY_ST = "EMPTY"
    
def calc_discounted_price(org_price, discount):
    if discount[0] == 0:
        return discount[1]
    elif discount[0] == 1:
        return org_price * (100 - discount[1])/100
    elif discount[0] == 2:
        return org_price - discount[1]
    else:
        raise Exception("Unknown discount code: " + discount[0])
    
def findLowestPrice(products, discounts):
    discounts_dict = {d[0]:(int(d[1]), float(d[2])) for d in discounts}
    
    total_price = 0
    for item in products:
        org_price = None
        min_price = None
        print("Item: ", item)
        # calc. all the prices
        for x in item:
            if org_price is None:
                print("Org:", org_price)
                org_price = float(x)
                min_price = org_price
            elif x == EMPTY_ST:
                continue    # empty discount
            else:
                new_price = round(calc_discounted_price(org_price, discounts_dict[x]))
                print("New price:", new_price)
                if new_price < min_price:
                    min_price = new_price
        
        # add the min price into the total price
        total_price += min_price
    # result
    return int(total_price)
                
        
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    products_rows = int(input().strip())
    products_columns = int(input().strip())

    products = []

    for _ in range(products_rows):
        products.append(input().rstrip().split())

    discounts_rows = int(input().strip())
    discounts_columns = int(input().strip())

    discounts = []

    for _ in range(discounts_rows):
        discounts.append(input().rstrip().split())

    result = findLowestPrice(products, discounts)

    fptr.write(str(result) + '\n')

    fptr.close()