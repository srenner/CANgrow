# CANgrow
Modular, automated gardening using a CAN Bus communication network.

## Farm
The Farm is the main application server, hosted by a Raspberri Pi with a MCP2515 based CAN Bus board, such as the PiCAN2 or PiCAN3.

For development, start the server with `fastapi dev src/farm/main.py`

## Environment
The Farm can have 1 or more Environments. Each Environment has its own temperature, humidity, and light schedule. Each environment runs on a Raspberry Pi RP2040 with a MCP25625 CAN Controller chip.

## Plant
Each Plant in the Environment will be monitored and watered. Like the Environment nodes, a Plant is powered by a Raspberry Pi RP2040 with a MCP25625 CAN Controller chip.