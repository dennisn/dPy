"""
Basic script to extract data from Investment Property website
(i.e. a set of URL, defined by a template.)
"""
from __future__ import print_function

import csv
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


PARSING_CLASS_TEMPLATE = 'align_r {0}'
PARSING_GROUP = ["House", "Unit"]
PARSING_CLASSNAME = ["Median", "QuarterlyGrowth", "1yr", "MedianGrowthThisYr",
                    "WeeklyMedianAdvertisedRent", "NumberSold", 
                    "GrossRentalYield", "DaysOnMarket"]
PARSING_TYPE = []
                    
def processPage(soupObj, suburb):
    '''
    Process the BeautifulSoup object
    '''
    res = {}
    res['suburb'] = suburb
    try:
        if IS_DEBUG:
            with codecs.open(outputDir + "/" + suburb + ".txt", "w", encoding="utf-8") as outF:
                outF.write(soup.prettify())
                outF.close()
        if len(PARSING_TYPE) == 0:
            for group in PARSING_GROUP:
                for name in PARSING_CLASSNAME:
                    PARSING_TYPE.append(group + " " + name)
        for type in PARSING_TYPE:
            className = PARSING_CLASS_TEMPLATE.format(type)
            tag = soupObj.find("td", class_ = className)
            # TODO: collect the data for long term storage
            # maybe output to a csv file
            #print(className, " = ", tag.string)
            res[type] = tag.string.strip()
    except Exception as e:
        print('Exception', e);
    return res
        
def processPageResponse(pageResponse, suburb):
    '''
    '''
    if page_response.status_code == 200:
        soup = BeautifulSoup(page_response.content, 'html.parser')
        record = processPage(soup, suburb)
        return record
    else:
        print("Page response code", page_response.status_code)
        return None
    
def getSuburbURL(urlTemplate, suburb, postcode):
    '''
    Construct URL for each suburb based on a template
    '''
    suburbTemp = suburb.lower().replace(" ", "-")
    return urlTemplate.format(suburbTemp, postcode)
    
def writeResults(data, outputDir):
    '''
    Write the result into a result CSV file
    '''
    suburbList = data.keys()
    suburbList.sort()
    fields = ['suburb']
    fields.extend(PARSING_TYPE)
    with open(outputDir + '/results.csv', 'wb') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields, restval='N/A', extrasaction='ignore')
        writer.writeheader()
        for suburb in suburbList:
            #if data[suburb] != None:
            writer.writerow(data[suburb])
                
    
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
    data = {}
    for suburb in suburbs:
        #if len(data) > 10: break
        print("Processing suburb: " + suburb)
        baseurl = getSuburbURL(urlTemplate, suburb, postcodes[suburb])
        # read the web site
        page_response = requests.get(baseurl, timeout=5)
        extractedData = processPageResponse(page_response, suburb)
        data[suburb] = extractedData
    writeResults(data, outputDir)
    print("Completed: ")
    #pprint.pprint(data)