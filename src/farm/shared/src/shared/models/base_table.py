from sqlmodel import SQLModel, Field
import time

class BaseTable(SQLModel, table=False):
    """
    Common metadata fields
    """

    created_at: int = Field(default_factory=lambda: int(time.time() * 1000))
    updated_at: int = Field(
        default_factory=lambda: int(time.time()),
        sa_column_kwargs={"onupdate": lambda: int(time.time() * 1000)}
    )
    is_active: bool = Field(default=True)