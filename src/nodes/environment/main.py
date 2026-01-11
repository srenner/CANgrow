# import board
# import digitalio
import time

NODE_TYPE: str = "environment"
FARM_CAN_ID: str = "can01"

while True:
    time.sleep(0.5)
    pass


#initialization:
#ping FARM_CAN_ID with NODE_TYPE payload
#receive ack - blink if not in db
#receive msg again when db ready
#stop blink
#loop/listen for commands
#respond when tasked with light switch, heat switch, humidity switch