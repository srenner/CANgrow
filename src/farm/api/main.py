from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager
import time


class Environment(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    can_id: str = Field(index=True)
    name: str
    created_at: int = Field(default=int(time.time()))
    sort_order: int
    is_active: int


sqlite_file_name = "cangrow.db"
sqlite_url = f"sqlite:///src/farm/database/{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("Shutdown at " )

app = FastAPI(lifespan=lifespan)

@app.post("/environment/")
def create_environment(environment: Environment):
    with Session(engine) as session:
        session.add(environment)
        session.commit()
        session.refresh(environment)
        return environment


@app.get("/environment/")
def read_environments():
    with Session(engine) as session:
        environments = session.exec(select(Environment)).all()
        return environments