# Tables

## Environment

| Id        | guid     |
| --------- | -------- |
| canid     | string   |
| name      | string   |
|           |          |
| sortorder | int      |
| createdat | datetime |

## EnvironmentPreferences

| Id             | guid |
| -------------- | ---- |
| environmentid  | guid |
| timestamp      | int  |
| lightstatus    | bool |
| targettemp     | int  |
| targethumidity | int  |
| targetgas      | int  |

## EnvironmentHistory

| Id            | guid     |
| ------------- | -------- |
| environmentid | guid     |
| datetime      | datetime |
| lightstatus   | bool     |
| heaterstatus  | bool     |
| temp          | int      |
| humdity       | int      |
| gas           | int      |

## Plant

| Id    | guid   |
| ----- | ------ |
| type  | string |
| name  | string |
| canid | string |
