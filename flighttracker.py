#import libraries
import urllib2 
import keyboard #pip install keyboard
import threading
from bs4 import BeautifulSoup #pip install bs4
def main():
# clock = threading.Timer(2.0, main)
# clock.start()
 #url
 flightnum = raw_input("Enter airline code and light numbe: ")
 url = 'https://flightaware.com/live/flight/' + flightnum
 print url
 webPage = urllib2.urlopen(url)
 #is it a good adress, does it read?
 print "result code: " + str(webPage.getcode())
 soup = BeautifulSoup(webPage, 'html.parser')
 remaining_box = soup.find('div', attrs={'class': 'flightPageSummaryStatusExt'})
 timeremaining = remaining_box.text.strip()
 print airtemp
# while True:
#  try:
#   if keyboard.is_pressed('enter'):
#    clock.cancel()
#    print 'key pressed!'
#    break
#   else:
#    pass
#  except:
#   break
if __name__ == "__main__":
 main()