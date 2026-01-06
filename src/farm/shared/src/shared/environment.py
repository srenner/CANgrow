from sqlmodel import SQLModel, Field
import time
from shared.base_table import BaseTable

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