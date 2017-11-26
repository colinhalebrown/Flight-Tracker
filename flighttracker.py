#import libraries
import urllib2 
import keyboard #pip install keyboard
import threading
from datetime import date
from bs4 import BeautifulSoup #pip install bs4
seconds = 0
today = date.today()
flightnum = raw_input('Enter airline code - flight number: ')
seconds = input('How often do you want to check?: ')
url = 'https://www.kayak.com/tracker/' + flightnum + '/' + str(today)

def track():
 if seconds > 0:
  clock = threading.Timer(seconds, track)
  clock.start()
 webPage = urllib2.urlopen(url)
 soup = BeautifulSoup(webPage, 'html.parser')
 status_box = soup.find('div', {'class' : 'keel-grid statusSubHeadline'})
 status = status_box.text.strip()
 print status
 if seconds > 0:
  while True:
   try:
    if keyboard.is_pressed('space'):
     clock.cancel()
     print 'key pressed!'
     break
    else:
     pass
   except:
    break
track()