"""
Basic script to extract data from Investment Property website
(i.e. a set of URL, defined by a template.)
"""
from __future__ import print_function

import datetime
import os
import pprint
import requests
from bs4 import BeautifulSoup

import vicPostcodes

IS_DEBUG = 0

# Import encoding engine
if IS_DEBUG:
    import codecs
    try:
        from feedparser import _getCharacterEncoding as enc
    except ImportError:
        enc = lambda x, y: ('utf-8', 1)


PARSING_CLASS_TEMPLATE = 'align_r {0} {1}'
PARSING_GROUP = ["House", "Unit"]
PARSING_CLASSNAME = ["Median", "QuarterlyGrowth", "1yr", "MedianGrowthThisYr",
                    "WeeklyMedianAdvertisedRent", "NumberSold", 
                    "GrossRentalYield", "DaysOnMarket"]
def processPage(soupObj, suburb):
    '''
    Process the BeautifulSoup object
    '''
    try:
        if IS_DEBUG:
            with codecs.open(outputDir + "/" + suburb + ".txt", "w", encoding="utf-8") as outF:
                outF.write(soup.prettify())
                outF.close()
        res = {}
        for group in PARSING_GROUP:
            for name in PARSING_CLASSNAME:
                className = PARSING_CLASS_TEMPLATE.format(group, name)
                tag = soupObj.find("td", class_ = className)
                # TODO: collect the data for long term storage
                # maybe output to a csv file
                #print(className, " = ", tag.string)
                res[group + "_" + name] = tag.string.strip()
        return res
    except Exception as e:
        print('Exception', e);
    
    
def getSuburbURL(urlTemplate, suburb, postcode):
    '''
    Construct URL for each suburb based on a template
    '''
    suburbTemp = suburb.lower().replace(" ", "-")
    return urlTemplate.format(suburbTemp, postcode)
    
    
"""
Main entry
"""
if __name__ == "__main__":
    # setup params
    #baseurl = 'http://www.yourinvestmentpropertymag.com.au/top-suburbs/vic-3130-blackburn.aspx'
    urlTemplate = 'http://www.yourinvestmentpropertymag.com.au/top-suburbs/vic-{1}-{0}.aspx'
    postcodes = vicPostcodes.loadPostcodes()
    today = datetime.date.today().isoformat()
    outputDir = "output_" + today
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    suburbs = postcodes.keys()
    suburbs.sort()
    count = 0
    for suburb in suburbs:
        if (count > 5): break
        count += 1
        print("Processing suburb: " + suburb)
        baseurl = getSuburbURL(urlTemplate, suburb, postcodes[suburb])
        # read the web site
        page_response = requests.get(baseurl, timeout=5)
        if page_response.status_code == 200:
            soup = BeautifulSoup(page_response.content, 'html.parser')
            record = processPage(soup, suburb)
            if record != None:
                pprint.pprint(record)
        else:
            print("Page response code", page_response.status_code)

    print("Completed: ")
