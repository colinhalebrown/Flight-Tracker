#import libraries
from bs4 import BeautifulSoup #pip install bs4
import keyboard #pip install keyboard
import urllib2 
import threading
from datetime import date

def track():
 if seconds > 0:
  clock = threading.Timer(seconds, track)
  clock.start()
 webPage = urllib2.urlopen(url)
# print str(webPage.getcode())
 soup = BeautifulSoup(webPage, 'html.parser')
 status_box = soup.find('div', {'class' : 'keel-grid statusSubHeadline'})
 status = status_box.text.strip()
 flight_box = soup.find('div', {'class' : 'col col-6-12'})
 flight = flight_box.text.strip()
 print flight + ' ' + status
 if seconds > 0:
  while True:
   try:
    if keyboard.is_pressed('escape'):
     clock.cancel()
     break
    else:
     pass
   except:
    break

def var():
 today = date.today()
 flightnum = raw_input('Enter airline ICAO code - flight number: ')
 global seconds 
 seconds = input('How often do you want to check? (seconds): ')
 global url 
 url = 'https://www.kayak.com/tracker/' + flightnum + '/' + str(today)
 print 'Checking for flight ' + flightnum + ' every ' + str(seconds) + ' seconds'
# print url
# print today
# print flightnum
# print seconds
 track()

var()
