from sqlmodel import SQLModel, Field
import time

### ENVIRONMENT MODELS ########################################################

class Environment(SQLModel, table=True):
    """
    Represents the Environment that Plants grow in. This could be a room in a building or a tent.
    """

    id: int | None = Field(default=None, primary_key=True)
    can_id: str = Field(index=True)
    name: str
    created_at: int = Field(default=int(time.time()))
    sort_order: int
    is_active: bool = Field(default=True)

class EnvironmentProfile(SQLModel, table=True):
    """
    Represents a grouping of EnvironmentTarget settings
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str
    descr: str
    is_active: bool = Field(default=True)
    created_at: int = Field(default=int(time.time()))

class EnvironmentHistory(SQLModel, table=True):
    """
    Represents the true condition for an Environment at the specified [datetime]
    """
    id: int | None = Field(default=None, primary_key=True)
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    light_status: bool
    heat_status: bool
    temperature: float
    humidity: float
    gas: float
    datetime: int

class EnvironmentTarget(SQLModel, table=True):
    """
    Represents the ideal condition for an Environment at the specified [timestamp] time of day
    """

    id: int | None = Field(default=None, primary_key=True)
    environment_profile_id: int = Field(default=None, foreign_key="environmentprofile.id")
    timestamp: int
    light_status: bool
    target_temperature: float
    target_humidity: float
    # possibly add target_gas if it makes sense
    created_at: int = Field(default=int(time.time()))

### PLANT MODELS ##############################################################

# unsure if batches are necessary
# class PlantBatch(SQLModel, table=True)

class Plant(SQLModel, table=True):
    """
    A Plant node that monitors a single 
    """

    id: int | None = Field(default=None, primary_key=True)
    species: str
    name: str
    can_id: str = Field(index=True)
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    created_at: int = Field(default=int(time.time()))
    sort_order: int
    auto_watering: bool
    is_active: bool = Field(default=True)

class PlantHistory(SQLModel, table=True):
    """
    Represents a status of a Plant at the specified [datetime]
    """

    id: int | None = Field(default=None, primary_key=True)
    plant_id: int = Field(foreign_key="plant.id")
    soil_moisture: float
    soil_temperature: float

class PlantObservation(SQLModel, table=True):
    """
    Subjective notes about a Plant at a given [created_at]
    """

    id: int | None = Field(default=None, primary_key=True)
    plant_id: int = Field(foreign_key="plant.id")
    height_cm: float | None
    subjective_notes: str
    subjective_score: int
    created_at: int = Field(default=int(time.time()))

class PhotoLink(SQLModel, table=True):
    """
    Represents an IP camera located in an Environment or pointed at a specific Plant
    """

    id: int | None = Field(default=None, primary_key=True)
    plant_id: int | None = Field(default=None, foreign_key="plant.id")
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    photo_url: str
    descr: str
    created_at: int = Field(default=int(time.time()))
    is_active: bool = Field(default=True)