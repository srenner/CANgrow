import time
from sqlmodel import Field, SQLModel

class EnvironmentHistory(SQLModel, table=True):
    """
    Represents the true condition for an Environment at the specified [datetime].
    """

    id: int | None = Field(default=None, primary_key=True)
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    environment_profile_id: int | None = Field(default=None, foreign_key="environmentprofile.id")
    light_status: bool | None
    heat_status: bool | None
    temperature: float | None
    humidity: float | None
    gas: float | None
    datetime: int = Field(default_factory=lambda: int(time.time()))

class EnvironmentHistoryCreate(SQLModel):
    """Schema for POST requests"""
    
    environment_id: int | None
    environment_profile_id: int | None
    light_status: bool | None
    heat_status: bool | None
    temperature: float | None
    humidity: float | None
    gas: float | None

class EnvironmentHistoryPublic(SQLModel):
    """Schema for GET response"""

    id: int
    environment_id: int | None
    environment_profile_id: int | None
    light_status: bool | None
    heat_status: bool | None
    temperature: float | None
    humidity: float | None
    gas: float | None
    datetime: int
