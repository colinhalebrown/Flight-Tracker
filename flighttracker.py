#import libraries
import urllib2 
import keyboard #pip install keyboard
import threading
from bs4 import BeautifulSoup #pip install bs4
flightnum = raw_input("Enter airline code - flight number: ")
def main():
 clock = threading.Timer(2.0, main)
 clock.start()
 url = 'https://www.kayak.com/tracker/' + flightnum + '/2017-11-25'
 print url
 webPage = urllib2.urlopen(url)
 #is it a good adress, does it read?
 print "result code: " + str(webPage.getcode())
 soup = BeautifulSoup(webPage, 'html.parser')
 status_box = soup.find('div', {'class' : 'keel-grid statusSubHeadline'})
 status = status_box.text.strip()
 print status
 while True:
  try:
   if keyboard.is_pressed('enter'):
    clock.cancel()
    print 'key pressed!'
    break
   else:
    pass
  except:
   break
if __name__ == "__main__":
 main()