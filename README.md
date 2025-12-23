# CANgrow

Modular, automated indoor gardening using a CAN Bus communication network.

CANgrow consists of three main parts: A Farm, Environments, and Plants.

The Farm is the brain of the system. It runs on a Raspberry Pi with a PiCAN hat and collects data, runs schedules, and hosts a website.

The Environment is the room or tent your plants grow in. You can have more than one. It runs on a RP2040 microcontroller with a MCP2515 CAN controller and monitors temperature, humdity, and air quality. It can control relays to activate lights, heaters, and more.

And a Plant is a plant. It runs on the same RP2040 microcontroller with MCP2515 CAN controller, and monitors soil moisture, and temperature. It can activate relays that control water flow, and measure the water usage.

All of these nodes are daisy-chained on a low voltage, reliable wired CAN bus network.

## Partial hardware list

- Raspberry Pi - [Raspberry Pi 5 - 2 GB RAM](https://www.adafruit.com/product/6007)
- CAN Bus board - [PiCAN3 CAN Bus Board for Raspberry Pi 4 with 3A SMPS And RTC](https://copperhilltech.com/pican3-can-bus-board-for-raspberry-pi-4-with-3a-smps-and-rtc/)

- Microcontroller - [Adafruit RP2040 CAN Bus Feather with MCP2515 CAN Controller - STEMMA QT](https://www.adafruit.com/product/5724)
- Environment sensor - [Adafruit BME688 - Temperature, Humidity, Pressure and Gas Sensor - STEMMA QT](https://www.adafruit.com/product/5046)
- Soil sensor - [Adafruit STEMMA Soil Sensor - I2C Capacitive Moisture Sensor - JST PH 2mm](https://www.adafruit.com/product/4026)
- Water valve - [Brass Liquid Solenoid Valve - 12V - 1/2 Inch G / BSP Thread](https://www.adafruit.com/product/996)
- Water flow sensor - [Liquid Flow Meter - Plastic 1/2" NPS Threaded](https://www.adafruit.com/product/828)

## Raspberry Pi / PiCAN Pinout

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
- AI generated 3D print designs located in the [3dprint/ai_generated](3dprint/ai_generated/) folder
- Additional use of AI will be listed here
