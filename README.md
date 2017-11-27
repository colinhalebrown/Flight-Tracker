# Flight Tracker
This tool will tell you how soon a flight is supposed to land. It will also tell you the status of the flight whether it is on time, delayed, or if it has landed. When the propt appears to input a ICAO Airline code then the flight number seperated by a hiphen. 

ICAO Airline Code - Flight Number
> example
> ASA-11
> Alaska Airlines flight 11

Common Airlines

| Airline | ICAO Airline Codes |
| ------- | ----------- |
| Alaska Airline | ASA |
| American Airline | AAL |
| Delta Airlines | DAL |
| Hawaiian Airlines | HAL |
| JetBlue Airway | JBU |
| Southwest Airlines | SWA |
| Spirit Airlines | NKS |
| United Airlines | UAL |
| Virgin America | VRD |

[Full list](https://en.wikipedia.org/wiki/List_of_airline_codes)

# Installation Tutorial
This tool is made for python 2.7, mileage may vary. 

## Install Needed Liberaries
Open your virtual enviroment or what ever instance of python you intend on using and install the two liberaries BeautifulSoup4 and Keyboard.  
```python
pip install bs4
pip install keyboard
```
## [Download](https://github.com/colinhalebrown/Flight-Tracker/archive/master.zip) the Code
In whatever instane of python you have installed the liberaries in [download](https://github.com/colinhalebrown/Flight-Tracker/archive/master.zip) or [clone](https://github.com/colinhalebrown/Flight-Tracker.git) and move the flighttracker.py to that destination.
![Folder example](/images/foler.png)
## Run flighttracker.py
In your virtual enviroment run flighttracker.py.
![console](/images/run.png)
## Input your flight & check time
First it will ask for your flight code. This code is in ICAO format, two parts the airlines and the flight number seperated by a hyphen. 
![example flight](/images/asa-123.png)
| Airline | ICAO Airline Codes |
| ------- | ----------- |
| Alaska Airline | ASA |
| American Airline | AAL |
| Delta Airlines | DAL |
| Hawaiian Airlines | HAL |
| JetBlue Airway | JBU |
| Southwest Airlines | SWA |
| Spirit Airlines | NKS |
| United Airlines | UAL |
| Virgin America | VRD |

[Full list](https://en.wikipedia.org/wiki/List_of_airline_codes)

After You have put in your airline code input how often you want it to check the status of the flight in seconds. If you want it to only check once input 0. If you input a number greater than 0 to stop it hit enter and it will end the program. 
![examaple flight 2](/images/asa-123(2).png)
