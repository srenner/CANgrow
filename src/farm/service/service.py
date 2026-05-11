import can
import time
import os
import queue
from threading import Thread
import requests
import datetime
import random

# setup gpio pins, etc

test_mode: bool = True

def can_rx_task():
    previous_temp = 22.5
    previous_humidity = 50.0
    while True:
        if test_mode:
            current_temp = previous_temp + random.uniform(-0.01, 0.01)
            current_humidity = previous_humidity + random.uniform(-0.01, 0.01)
            payload: dict[str, str | int | float | bool] = {
                    "environment_id": 1,
                    "environment_profile_id": 1,
                    "light_status": True,
                    "heat_status": False,
                    "temperature": current_temp,
                    "humidity": current_humidity,
                    "gas": 0
            }
            response = requests.post('http://localhost:8000/live/environment-history', json=payload)
            print(response.text + ' ' + str(datetime.datetime.now()))
            previous_temp = current_temp
            previous_humidity = current_humidity
            time.sleep(.2)

def can_tx_task():
    while True:
        # check for 
        time.sleep(1)

q = queue.Queue()
rx = Thread(target = can_rx_task)  
rx.start()
tx = Thread(target = can_tx_task)
tx.start()

while True:
    time.sleep(1)
