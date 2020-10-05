#Modules imported for the script
import requests
import json
from datetime import datetime
import os

#Reading from the API and converting the json into python dicts
try:
    response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
    #response = requests.get('https://api.exchangeratesapi.io/history?start_at=2018-08-25&end_at=2018-09-01')
    response.raise_for_status()
except requests.exceptions.RequestException as err:
    raise SystemExit(err)

print(str(datetime.now()) + " : Connection to API succesful")

rates_current = json.loads(response.text)

#Tokenizing from the dict
try:
    rates = rates_current["rates"]
except KeyError as err:
    print(str(datetime.now()) + " : Key error in rates nest")
    raise SystemExit(err)

try:
    base = rates_current["base"]
except KeyError as err:
    print(str(datetime.now()) + " : Key error in base currency")
    raise SystemExit(err)

try:
    Curr_date = rates_current["date"]
except KeyError as err:
    print(str(datetime.now()) + " : Key error in date")
    raise SystemExit(err)

print(str(datetime.now()) + " : Tokenizing succesful")

#Declaring an empty list to hold the records
conversion = []

#Converting the dict into lists of records
for Curr,Amt in rates.items():
    conversion_elem = Curr + '|' + str(Amt) + '|' + base + '|' + Curr_date + '|' + str(datetime.now())
    conversion.append(conversion_elem)

#Create file if it doesn't exist:
if not os.path.exists('/edw/Currency_Conversion/data/Conversion.csv'):
    try:
        open('/edw/Currency_Conversion/data/Conversion.csv','w').close()
        print(str(datetime.now()) + " : Placed a new data file")
    except IOERROR as err:
        raise SystemExit(err)


#Place file header if it is empty
if os.path.getsize('/edw/Currency_Conversion/data/Conversion.csv') == 0:
    try:
        with open('/edw/Currency_Conversion/data/Conversion.csv','w') as f:
            f.write("Currency Code|Conversion Rate|Base Currency|Conversion Date|Load Timestamp")
            f.write("\n")
        f.close()
        print(str(datetime.now()) + " : File was empty. Placed a header.")
    except IOERROR as err:
        raise SystemExit(err)
                                                
#Write to CSV    
try:
    with open('/edw/Currency_Conversion/data/Conversion.csv','a') as f:
        f.write("\n".join(conversion))
        f.write("\n")
    f.close()
    print(str(datetime.now()) + " : File write is succesful")
except IOERROR as err:
    raise SystemExit(err)
