# -*- coding: utf-8 -*-
"""
Title:      main.py
Purpose:    sends an email to myself and my father once a day via windows 10 
            scheduler to tell us where the cheapest gas is out of our usual gas 
            stations
    
Author:     D. Pipes
IDE:        Spyder 5
Created:    3/8/2022
"""

import emailer
import gbscraper

homeQT = 'https://www.gasbuddy.com/station/146644'
homeRaceway = 'https://www.gasbuddy.com/station/71747'
workRaceTrac = 'https://www.gasbuddy.com/station/197744'
workGymQT = 'https://www.gasbuddy.com/station/137126'

def dpipesUpdate():
    """
    Handles my personal gas update
    """
    subject = 'Gas Update!'
    message = """Time for a gas update. For a gallon of MidGrade:
    Work:
        Work RaceTrac: {0}
        Gym QuikTrip: {1}
    Home:
        Home QT: {2}
        Home Raceway: {3}
    
    
    Links:
    Home QT: https://www.gasbuddy.com/station/146644
    Home Raceway: https://www.gasbuddy.com/station/71747
    Work RaceTrac: https://www.gasbuddy.com/station/197744
    Gym QT: https://www.gasbuddy.com/station/137126""".format(gbscraper.getPrice(workRaceTrac,'midgrade'),gbscraper.getPrice(workGymQT,'midgrade'),gbscraper.getPrice(homeQT,'midgrade'),gbscraper.getPrice(homeRaceway,'midgrade'))
    emailer.sendEmail('pipeeeeees@gmail.com',subject,message)

def dadUpdate():
    """
    Handles my father's gas update
    """
    subject = 'Gas Update!'
    message = """Time for a gas update. For a gallon of MidGrade:
        Home QT: {0}
        Home Raceway: {1}
    
    
    Links:
    Home QT: https://www.gasbuddy.com/station/146644
    Home Raceway: https://www.gasbuddy.com/station/71747""".format(gbscraper.getPrice(homeQT,'midgrade'),gbscraper.getPrice(homeRaceway,'midgrade'))
    emailer.sendEmail('pipesda@gmail.com',subject,message)

def main():
    dpipesUpdate()
    dadUpdate()

if __name__ == '__main__':
    main()