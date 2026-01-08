
from sqlmodel import Field, SQLModel
from shared.models.base_table import BaseTable

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

class EnvironmentProfileCreate(SQLModel):
    """Schema for POST requests"""

    name: str
    descr: str = Field(default="")

class EnvironmentProfilePatch(SQLModel):
    """Schema for PATCH requests"""

    name: str
    descr: str = Field(default="")

class EnvironmentProfilePublic(SQLModel):
    """Schema for GET response"""

    id: int
    created_at: int
    updated_at: int
    is_active: bool
    name: str
    descr: str | None = Field(default="")