# CANgrow
Modular, automated gardening using a CAN Bus communication network.

## Farm
The Farm is the main application server, hosted by a Raspberri Pi with a MCP2515 based CAN Bus board, such as the PiCAN3.

## Environment
The Farm can have 1 or more Environments. Each Environment has its own temperature, humidity, and light schedule.

## Plant
Each Plant in the Environment will be monitored and watered.