from sqlmodel import Field, SQLModel
from shared.models.base_table import BaseTable


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