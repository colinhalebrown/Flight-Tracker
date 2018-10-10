# Flight Tracker
This tool will tell you how soon a flight is supposed to land. It will also tell you the status of the flight whether it is on time, delayed, or if it has landed. Just follow the promts and you will be receiving flight updates in to time. It uses Twilio to send you live updates to your phone so an account is needed at this time.

ICAO Airline Code - Flight Number
> Example:
> ASA-11,
> Alaska Airlines flight 11

Common Airlines

| Airline | ICAO Airline Codes |
| ------- | ----------- |
| Alaska | ASA |
| American | AAL |
| Delta | DAL |
| Hawaiian | HAL |
| JetBlue | JBU |
| Southwest | SWA |
| Spirit | NKS |
| United | UAL |
| Virgin America | VRD |

[Full list](https://en.wikipedia.org/wiki/List_of_airline_codes)

![Flow Chart](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/flowchart.png)

# Installation Tutorial
This tool is made for python 2.7.14, mileage may vary. 

## Install Needed Libraries
Open your virtual environment or what ever instance of python you intend on using and install three libraries BeautifulSoup4, Twilio and Keyboard.

```python
pip install bs4
pip install keyboard
pip install twilio
```

## [Download](https://github.com/colinhalebrown/Flight-Tracker/archive/master.zip) the Code & Create a Twilio account
In whatever instance of python you have installed the liberaries into [download](https://github.com/colinhalebrown/Flight-Tracker/archive/master.zip) or [clone](https://github.com/colinhalebrown/Flight-Tracker.git) and move the flighttracker.py to that destination.

![Folder example](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/folder.PNG)

While your downloading the python code jump over to [Twilio](https://www.twilio.com) and create an account, trial works fine. After you have created an account make sure to buy a Twilio phone number. Then go to your console and grab your account SID, Authentication Token, and phone number. You will need this information later.

## Run flighttracker.py
In your virtual environment run flighttracker.py.

![console](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/run.gif)

```console
python flighttracker.py
```

## Input your flight, check time & Twilio info.
First it will ask for your flight code. This code is in ICAO format, two parts the airline and the flight number separated by a hyphen. 

Here is an example using flight asa-123 (Alaska Airlines flight 123)

![example flight ASA-123](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/asa-123.gif)

| Airline | ICAO Airline Codes |
| ------- | ----------- |
| Alaska | ASA |
| American | AAL |
| Delta | DAL |
| Hawaiian | HAL |
| JetBlue | JBU |
| Southwest | SWA |
| Spirit | NKS |
| United | UAL |
| Virgin America | VRD |

[Full list](https://en.wikipedia.org/wiki/List_of_airline_codes)

After You have put in your airline code input how often you want it to check the status of the flight in minutes. If you want it to only check once input 0. If you input a number greater than 0 press escape to end the program. Follow the next promts to have it send you text notifications. It will start by asking for your Account SID and Account authentication token I recommend copy and pasting these values (they tend to be long AF). To complete the setup of the program just input the Twilio number and the number you wish to send notifications to. When inputting these numbers _don't_ add hyphens, spaces or parentheses however a +1 in front of the number is fine.

![examaple flight ASA-123 comleted](https://github.com/colinhalebrown/Flight-Tracker/blob/master/images/asa-123(2).PNG)

# Common Errors
* If the flight ICAO code or flight number is not associated with an actual flight it will check and give a large error code every few invterval. 
* invalid or incorrect Twilio information is given.
* The Twilio or cell number given are given with other characters, spaces, hyphens, parentheses ect. 


# Sources
* I used a free code camp tutorial to learn BeautifulSoup it can be found [HERE](https://medium.freecodecamp.org/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe)
* I used the guide from Twilio for the Twilio code that can be found [HERE](https://www.twilio.com/docs/libraries/python)
