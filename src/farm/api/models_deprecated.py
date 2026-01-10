from sqlmodel import SQLModel, Field
from models_deprecated.base_table import BaseTable
import time

### PLANT MODELS ##############################################################

# unsure if batches are necessary
# class PlantBatch(SQLModel, table=True)



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
    