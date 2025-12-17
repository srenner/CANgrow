# CANgrow

Modular, automated indoor gardening using a CAN Bus communication network.

## Farm

The Farm is the main application server, hosted by a Raspberri Pi with a MCP2515 based CAN Bus board, such as the PiCAN2 or PiCAN3.

- Rasperri Pi - [Raspberry Pi 5 - 2 GB RAM](https://www.adafruit.com/product/6007)
- CAN Bus board - [PiCAN3 CAN Bus Board for Raspberry Pi 4 with 3A SMPS And RTC](https://copperhilltech.com/pican3-can-bus-board-for-raspberry-pi-4-with-3a-smps-and-rtc/)

For development, start the server with `fastapi dev src/farm/api/main.py`

## Environment

The Farm can have 1 or more Environments. Each Environment has its own temperature, humidity, and light schedule. If you have multiple rooms or multiple tents, each one is a separate Environment. Each Environment runs on a Raspberry Pi RP2040 microcontroller with a MCP25625 CAN Controller chip.

- Microcontroller - [Adafruit RP2040 CAN Bus Feather with MCP2515 CAN Controller - STEMMA QT](https://www.adafruit.com/product/5724)
- Environment sensor - [Adafruit BME688 - Temperature, Humidity, Pressure and Gas Sensor - STEMMA QT](https://www.adafruit.com/product/5046)

### Power

- Microcontroller can be powered from USB-C port
- Environment sensor takes 3-5VDC from the microcontroller

### Pinout

TBD

## Plant

Each Plant in the Environment will be monitored and watered. Like the Environment nodes, a Plant is powered by a Raspberry Pi RP2040 microcontroller with a MCP25625 CAN Controller chip.

- Microcontroller - [Adafruit RP2040 CAN Bus Feather with MCP2515 CAN Controller - STEMMA QT](https://www.adafruit.com/product/5724)
- Soil sensor - [Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor - JST PH 2mm](https://www.adafruit.com/product/4026)
- Water valve - [Brass Liquid Solenoid Valve - 12V - 1/2 Inch G / BSP Thread](https://www.adafruit.com/product/996)
- Water flow sensor - [Liquid Flow Meter - Plastic 1/2" NPS Threaded](https://www.adafruit.com/product/828)

### Power

- Microcontroller can be powered from USB-C port
- Soil sensor takes 3-5VDC from the microcontroller
- Water valve requires 12VDC
- Water flow sensor requires 5-18VDC

### Pinout

| Function      | Communication | GPIO Pin | Pin on board | Hookup                  |
| ------------- | ------------- | -------- | ------------ | ----------------------- |
| Digital pulse | CAN           | GPIO13   | D13          | Water meter yellow wire |
| CAN_STANDBY   | CAN           | GPIO16   |              |                         |
| CAN_TX0_RTS   | CAN           | GPIO17   |              |                         |
| CAN_RESET     | CAN           | GPIO18   |              |                         |
| CAN_CS        | CAN           | GPIO19   |              |                         |
| CAN_INTERRUPT | CAN           | GPIO22   |              |                         |
| CAN_RX0_BF    | CAN           | GPIO23   |              |                         |
| SDA0          | I2C           | GPIO24   | D24          | Soil sensor white wire  |
| SCL0          | I2C           | GPIO25   | D25          | Soil sensor green wire  |

## AI Usage

- AI generated documentation is located in the [doc/ai_generated](doc/ai_generated) folder
- Additional use of AI will be listed here
