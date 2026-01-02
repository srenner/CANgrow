from sqlmodel import SQLModel, Field
import time

class BaseTable(SQLModel, table=False):
    """
    Common metadata fields
    """

    created_at: int = Field(default_factory=lambda: int(time.time()))
    updated_at: int = Field(
        default_factory=lambda: int(time.time()),
        sa_column_kwargs={"onupdate": lambda: int(time.time())}
    )
    is_active: bool = Field(default=True)

### ENVIRONMENT MODELS ########################################################

class Environment(BaseTable, table=True):
    """
    Represents the Environment that Plants grow in. This could be a room in a building or a tent.
    """
    
    id: int | None = Field(default=None, primary_key=True)
    can_id: str = Field(index=True)
    name: str
    descr: str | None
    sort_order: int = Field(default=0)
    model_config = {"from_attributes": True}

class EnvironmentCreate(SQLModel):
    """Schema for POST requests"""
    
    can_id: str = Field(index=True)
    name: str
    descr: str = Field(default="")
    sort_order: int = Field(default=0)

class EnvironmentPatch(SQLModel):
    """Schema for PATCH requests"""

    can_id: str | None = Field(default=None)
    name: str | None = Field(default=None)
    descr: str = Field(default="")
    sort_order: int | None = Field(default=None)
    is_active: bool | None = Field(default=None)

class EnvironmentPublic(SQLModel):
    """Schema for GET response"""

    id: int
    created_at: int
    updated_at: int
    is_active: bool
    can_id: str
    name: str
    descr: str | None = Field(default="")
    sort_order: int

class EnvironmentProfile(BaseTable, table=True):
    """
    Represents a grouping of EnvironmentTarget settings.

    Examples:
        - "Seedling": Lights are on continuously.
        - "Growth Stage": Lights are on 18h per day.
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str
    descr: str | None

class EnvironmentHistory(SQLModel, table=True):
    """
    Represents the true condition for an Environment at the specified [datetime].
    """

    id: int | None = Field(default=None, primary_key=True)
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    light_status: bool | None
    heat_status: bool | None
    temperature: float | None
    humidity: float | None
    gas: float | None
    datetime: int = Field(default=int(time.time()))

class EnvironmentTarget(BaseTable, table=True):
    """
    Represents the ideal condition for an Environment at the specified [timestamp] time of day.
    """

    id: int | None = Field(default=None, primary_key=True)
    environment_profile_id: int = Field(default=None, foreign_key="environmentprofile.id")
    timestamp: int
    light_status: bool
    target_temperature: float
    target_humidity: float
    # possibly add target_gas if it makes sense

### PLANT MODELS ##############################################################

# unsure if batches are necessary
# class PlantBatch(SQLModel, table=True)

class Plant(BaseTable, table=True):
    """
    A Plant node that monitors a single real world plant.
    """

    id: int | None = Field(default=None, primary_key=True)
    species: str
    name: str
    can_id: str = Field(index=True)
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    auto_watering: bool
    sort_order: int = Field(default=0)

class PlantCreate(SQLModel):
    """Schema for POST requests"""

    species: str
    name: str
    can_id: str
    environment_id: int
    auto_watering: bool
    sort_order: int

class PlantPublic(SQLModel):
    """Schema for GET response"""

    id: int
    created_at: int
    updated_at: int
    is_active: bool
    species: str
    name: str
    can_id: str
    environment_id: int
    auto_watering: bool
    sort_order: int

class PlantHistory(SQLModel, table=True):
    """
    Represents a status of a Plant at the specified [datetime].
    """

    id: int | None = Field(default=None, primary_key=True)
    plant_id: int = Field(foreign_key="plant.id")
    soil_moisture: float | None
    soil_temperature: float | None
    datetime: int = Field(default=int(time.time()))

class PlantObservation(SQLModel, table=True):
    """
    Subjective notes about a Plant at a given [created_at].
    """

    id: int | None = Field(default=None, primary_key=True)
    plant_id: int = Field(foreign_key="plant.id")
    height_cm: float | None
    subjective_notes: str
    subjective_score: int | None
    created_at: int = Field(default_factory=lambda: int(time.time()))

### MISC ######################################################################

class CameraLink(BaseTable, table=True):
    """
    Represents an IP camera located in an Environment or pointed at a specific Plant.
    """

    id: int | None = Field(default=None, primary_key=True)
    plant_id: int | None = Field(default=None, foreign_key="plant.id")
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    photo_url: str | None
    video_url: str | None
    descr: str | None
    sort_order: int = Field(default=0)
    