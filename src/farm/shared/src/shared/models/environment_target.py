from sqlmodel import Field, SQLModel
from shared.models.base_table import BaseTable

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

class EnvironmentTargetCreate(SQLModel):
    """Schema for POST requests"""

    environment_profile_id: int
    timestamp: int
    light_status: bool
    target_temperature: float
    target_humidity: float

class EnvironmentTargetPublic(SQLModel):
    """Schema for GET response"""

    id: int
    created_at: int
    updated_at: int
    is_active: bool
    environment_profile_id: int
    timestamp: int
    light_status: bool
    target_temperature: float
    target_humidity: float
    # possibly add target_gas if it makes sense
