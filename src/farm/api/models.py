from sqlmodel import SQLModel, Field
import time

class Environment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    can_id: str = Field(index=True)
    name: str
    created_at: int = Field(default=int(time.time()))
    sort_order: int
    is_active: bool = Field(default=True)

class EnvironmentProfile(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    descr: str
    is_active: bool = Field(default=True)
    created_at: int = Field(default=int(time.time()))

class EnvironmentHistory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    environment_id: int | None = Field(default=None, foreign_key="environment.id")
    light_status: bool
    heat_status: bool
    temperature: float
    humidity: float
    gas: float
    datetime: int



class EnvironmentTarget(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    environment_profile_id: int = Field(default=None, foreign_key="environmentprofile.id")
    timestamp: int
    light_status: bool
    target_temperature: float
    target_humidity: float
    # possibly add target_gas if it makes sense
    created_at: int = Field(default=int(time.time()))