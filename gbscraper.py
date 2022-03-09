# -*- coding: utf-8 -*-
"""
Title:      gbscraper.py
Purpose:    this .py file handles the web scraping. A 5 second delay per scrape
            is included to reduce polling load on the website to keep everyone
            happy. Please contact me at pipeeeeees@gmail.com if there are any
            issues.
    
Author:     D. Pipes
IDE:        Spyder 5
Created:    3/8/2022
"""

import requests
import time

#home QT
#https://www.gasbuddy.com/station/146644
#home raceway
#https://www.gasbuddy.com/station/71747


#work racetrac
#https://www.gasbuddy.com/station/197744
#work gym QT
#https://www.gasbuddy.com/station/137126


def getPrice(url,grade):
    """
    url: of gasbuddy gas station
    grade: choose one of the following
        'regular'
        'midgrade'
        'premium'
        'diesel'
    """
    #url = 'https://www.gasbuddy.com/station/197744'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    htmlstring = str(result.content.decode())
    parselist = htmlstring.split('<span class="text__xl___2MXGo text__bold___1C6Z_ text__left___1iOw3 FuelTypePriceDisplay-module__price___3iizb">')
    parselist.pop(0)
    time.sleep(5)
    #at this point, we should have all prices
    try:
        if len(parselist) == 4:
            if grade == 'regular':
                return str(parselist[0].split('<')[0])
            if grade == 'midgrade':
                return str(parselist[1].split('<')[0])
            if grade == 'premium':
                return str(parselist[2].split('<')[0])
            if grade == 'diesel':
                return str(parselist[3].split('<')[0])
            else:
                return 'ERROR. GRADE OF GASOLINE NOT TYPED CORRECTLY'
        elif len(parselist) == 5:
            if grade == 'regular':
                return str(parselist[0].split('<')[0])
            if grade == 'midgrade':
                return str(parselist[1].split('<')[0])
            if grade == 'premium':
                return str(parselist[2].split('<')[0])
            if grade == 'diesel':
                return str(parselist[3].split('<')[0])
            if grade == 'UNL88':
                return str(parselist[4].split('<')[0])
            else:
                return 'ERROR. GRADE OF GASOLINE NOT TYPED CORRECTLY'
    except:
        return 'ERROR OCCURED FETCHING DATA...'

    
    
    