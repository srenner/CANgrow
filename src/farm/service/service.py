import can
import time
import os
import queue
from threading import Thread

# setup gpio pins, etc

def can_rx_task():
    while True:
        print("Rx:" + str(time.time()) + "\n")
        time.sleep(1)

def can_tx_task():
    while True:
        print("Tx:" + str(time.time()) + "\n")
        time.sleep(1)

q = queue.Queue()
rx = Thread(target = can_rx_task)  
rx.start()
tx = Thread(target = can_tx_task)
tx.start()

while True:
    time.sleep(1)
