import requests
from random import *
import time
for i in range(10):
    value = randint(1, 100)
    url = 'https://api.thingspeak.com/update?api_key=NRGA7VE1M9L292QP&field1=' + str(value)
    r = requests.get(url)
    time.sleep(20)
