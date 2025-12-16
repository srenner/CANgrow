# Plant Monitoring System - Database Schema

## Entity Relationship Diagram

```mermaid
erDiagram
    Environment ||--o{ EnvironmentHistory : has
    Environment ||--o{ Plant : contains
    Environment ||--o{ PhotoLink : monitors
    EnvironmentProfile ||--o{ EnvironmentTarget : defines
    Plant ||--o{ PlantHistory : records
    Plant ||--o{ PlantObservation : observes
    Plant ||--o{ PhotoLink : monitors

    Environment {
        int id PK
        string can_id
        string name
        int created_at
        int sort_order
        bool is_active
    }

    EnvironmentProfile {
        int id PK
        string name
        string descr
        bool is_active
        int created_at
    }

    EnvironmentHistory {
        int id PK
        int environment_id FK
        bool light_status
        bool heat_status
        float temperature
        float humidity
        float gas
        int datetime
    }

    EnvironmentTarget {
        int id PK
        int environment_profile_id FK
        int timestamp
        bool light_status
        float target_temperature
        float target_humidity
        int created_at
    }

    Plant {
        int id PK
        string species
        string name
        string can_id
        int environment_id FK
        int created_at
        int sort_order
        bool auto_watering
        bool is_active
    }

    PlantHistory {
        int id PK
        int plant_id FK
        float soil_moisture
        float soil_temperature
    }

    PlantObservation {
        int id PK
        int plant_id FK
        float height_cm
        string subjective_notes
        int subjective_score
        int created_at
    }

    PhotoLink {
        int id PK
        int plant_id FK
        int environment_id FK
        string photo_url
        string descr
        int created_at
        bool is_active
    }
```

## Table Descriptions

### Environment Models

- **Environment**: Represents the physical growing space (room, tent, etc.)
- **EnvironmentProfile**: Reusable configuration templates for environment settings
- **EnvironmentHistory**: Time-series records of actual environmental conditions
- **EnvironmentTarget**: Scheduled target conditions linked to profiles

### Plant Models

- **Plant**: Individual plant monitoring nodes with sensors
- **PlantHistory**: Time-series sensor data for soil conditions
- **PlantObservation**: Manual observations and subjective assessments
- **PhotoLink**: IP camera references for environments or specific plants