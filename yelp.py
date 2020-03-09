import requests
import random 

number = random.randint(1, 10)
if number == 1:
    term = 'sushi'
elif number == 2:
    term = 'burger'
elif number == 3:
    term = 'pizza'
elif number == 4:
    term = 'chinese'
elif number == 5:
    term = 'tacos'
elif number == 6:
    term = 'ramen'
elif number == 7:
    term = 'korean'
elif number == 8:
    term = 'thai'
elif number == 9:
    term = 'poke'
elif number == 10:
    term = 'pho'

radius = random.randint(1, 8000)

API_KEY = 'FUNjHwPm21YiKZpwzqW40Ah3Fm3kGQ75DTm9i2nG6naK9F4eEGh6zdYQd67iHiPv-gBgEQSK5kpC1aRPQr27LJw82rdq5m85zDfUOvzfVwHlMKNUQsSM5QRSip5aXnYx'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

PARAMETERS = {'term': term,
              'limit': 1,
              'radius': radius,
              'location': 'San Diego'}

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

business_data = response.json()

for biz in business_data['businesses']:
    print(biz['name'])