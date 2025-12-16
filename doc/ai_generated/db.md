# Plant Monitoring System - Database Schema

## Entity Relationship Diagram

```mermaid
erDiagram
    Environment ||--o{ EnvironmentHistory : has
    Environment ||--o{ Plant : contains
    Environment ||--o{ CameraLink : monitors
    EnvironmentProfile ||--o{ EnvironmentTarget : defines
    Plant ||--o{ PlantHistory : records
    Plant ||--o{ PlantObservation : observes
    Plant ||--o{ CameraLink : monitors

    Environment {
        int id PK
        string can_id
        string name
        int sort_order
        int created_at
        bool is_active
    }

    EnvironmentProfile {
        int id PK
        string name
        string descr
        int created_at
        bool is_active
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
        bool is_active
    }

    Plant {
        int id PK
        string species
        string name
        string can_id
        int environment_id FK
        bool auto_watering
        int sort_order
        int created_at
        bool is_active
    }

    PlantHistory {
        int id PK
        int plant_id FK
        float soil_moisture
        float soil_temperature
        int datetime
    }

    PlantObservation {
        int id PK
        int plant_id FK
        float height_cm
        string subjective_notes
        int subjective_score
        int created_at
    }

    CameraLink {
        int id PK
        int plant_id FK
        int environment_id FK
        string photo_url
        string video_url
        string descr
        int sort_order
        int created_at
        bool is_active
    }
```

## Table Descriptions

### Base Fields
All tables with `created_at` and `is_active` inherit from `BaseTable`:
- **created_at**: Timestamp when the record was created
- **is_active**: Boolean flag for soft deletion/deactivation

### Environment Models

- **Environment**: Represents the physical growing space (room, tent, etc.)
  - Inherits: `created_at`, `is_active`
  
- **EnvironmentProfile**: Reusable configuration templates for environment settings (e.g., "Seedling", "Growth Stage")
  - Inherits: `created_at`, `is_active`
  
- **EnvironmentHistory**: Time-series records of actual environmental conditions
  - No inheritance - uses `datetime` field for timestamps
  
- **EnvironmentTarget**: Scheduled target conditions linked to profiles
  - Inherits: `created_at`, `is_active`

### Plant Models

- **Plant**: Individual plant monitoring nodes with sensors
  - Inherits: `created_at`, `is_active`
  
- **PlantHistory**: Time-series sensor data for soil conditions
  - No inheritance - uses `datetime` field for timestamps
  
- **PlantObservation**: Manual observations and subjective assessments
  - Uses `created_at` but doesn't inherit from BaseTable

### Miscellaneous

- **CameraLink**: IP camera references for environments or specific plants
  - Inherits: `created_at`, `is_active`
  - Supports both photo and video URLs