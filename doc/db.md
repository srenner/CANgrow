# Plant Monitoring Database Schema

## Database Diagram

```mermaid
erDiagram
    Environment ||--o{ EnvironmentHistory : "has"
    Environment ||--o{ Plant : "contains"
    EnvironmentProfile ||--o{ EnvironmentTarget : "defines"
    Plant ||--o{ PlantHistory : "tracks"
    Plant ||--o{ PlantObservation : "documents"

    Environment {
        int id
        string can_id
        string name
        int created_at
        int sort_order
        bool is_active
    }

    EnvironmentProfile {
        int id
        string name
        string descr
        bool is_active
        int created_at
    }

    EnvironmentHistory {
        int id
        int environment_id
        bool light_status
        bool heat_status
        float temperature
        float humidity
        float gas
        int datetime
    }

    EnvironmentTarget {
        int id
        int environment_profile_id
        int timestamp
        bool light_status
        float target_temperature
        float target_humidity
        int created_at
    }

    Plant {
        int id
        string species
        string name
        string can_id
        int environment_id
        int created_at
        int sort_order
        bool auto_watering
        bool is_active
    }

    PlantHistory {
        int id
        int plant_id
        float soil_moisture
    }

    PlantObservation {
        int id
        int plant_id
        float height_cm
        string subjective_notes
        int subjective_score
        int created_at
    }
```

## Table Details

### Environment
- **id**: Primary key
- **can_id**: Indexed, hardware integration identifier
- **environment_id** in EnvironmentHistory: Foreign key reference

### EnvironmentProfile
- **id**: Primary key
- **environment_profile_id** in EnvironmentTarget: Foreign key reference

### Plant
- **id**: Primary key
- **can_id**: Indexed, hardware integration identifier
- **environment_id**: Foreign key to Environment
- **plant_id** in PlantHistory and PlantObservation: Foreign key reference