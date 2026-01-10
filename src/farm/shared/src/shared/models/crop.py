from sqlmodel import Field, SQLModel
from shared.models.base_table import BaseTable

class Crop(BaseTable, table=True):
    """
    A Crop is a batch of plants grown together at the same time
    """

    id: int | None = Field(default=None, primary_key=True)
    name: str | None
    descr: str | None
    batch_number: str | None
    start_date: int | None
    end_date: int | None
    