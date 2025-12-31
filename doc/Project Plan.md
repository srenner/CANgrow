# Node Responsibilities

## Farm Node

### Logic

- Receive and log all CAN messages in SQLite
- Archive CAN messages and replace with summary records
- Maintain lighting schedules
- Maintain heating range preferences
- Maintain humdity range preferences
- Host API
- Host web frontend

## Environment Nodes

### Logic

- Read environment temperature
- Read environment humidity
- Read and analyze environment gas
- Trigger relay for environment lighting
- Trigger relay for environment heating

### CAN

- Rx ping from Farm node
- Rx desired temperature range
- Rx desired humidity range
- Rx desired light status
- Tx temperature
- Tx humdity
- Tx gas
- Tx light status
- Tx humdifier status

## Plant Nodes

### Logic

- Read soil moisture
- Read soil temperature
- Activate water valve on
- Read water flow
- Activate water valve off
- Cache data locally if Environment node goes offline

### CAN

- Tx soil moisture
- Tx soil temperature
- Tx water valve status
- Tx water flow data (?)
- Rx ping from Environment node

### Pseudocode

```
while(true)
{
    var soilMoisture = readSoilMoisture()
    var soilTemperature = readSoilTemperature()

    CAN.send(soilMoisture)
    CAN.send(soilTemperature)
    
    var waterValveStatus = readWaterValve()

    if(plantNeedsWater())
    {
        waterValve.set(true)
    }
    else
    {
        waterValve.set(false)
    }
}

function calculateFlowRate()
{
    // measure pulses with timestamps
    // total water volume over period calculated by pulse count
    // flow rate calculated with pulses per length of time, possibly 1s
}
```

Data strategy

Environment sends msgs: temp, humid, gas, light status, heat status
only send to db if any value changed
save key frame record at least every 60s

finalize naming conventions