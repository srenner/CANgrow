import can
import time
import os
import queue
from threading import Thread
import requests

# setup gpio pins, etc

test_mode: bool = True

def can_rx_task():
    while True:
        #print("Rx:" + str(time.time()) + "\n")

        if test_mode:
            """
                /live/environment-history

                {
                    "environment_id": 1,
                    "environment_profile_id": 1,
                    "light_status": true,
                    "heat_status": false,
                    "temperature": 22.5,
                    "humidity": 44.2,
                    "gas": 0
                }

            """
            payload: dict[str, str | int | float | bool] = {
                    "environment_id": 1,
                    "environment_profile_id": 1,
                    "light_status": True,
                    "heat_status": False,
                    "temperature": 22.5,
                    "humidity": 44.2,
                    "gas": 0
            }
            response = requests.post('http://localhost:8000/live/environment-history', json=payload)
            print(response)
            time.sleep(1)

def can_tx_task():
    while True:
        #print("Tx:" + str(time.time()) + "\n")
        time.sleep(1)

q = queue.Queue()
rx = Thread(target = can_rx_task)  
rx.start()
tx = Thread(target = can_tx_task)
tx.start()

while True:
    time.sleep(1)
