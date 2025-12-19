from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager
import time
from models import Environment, EnvironmentProfile
from models import Plant

sqlite_file_name = "cangrow.db"
sqlite_url = f"sqlite:///src/farm/database/{sqlite_file_name}" # TODO verify path for prod use

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

### ENVIRONMENT ENDPOINTS #####################################################

@app.get("/environment")
def read_environments():
    with Session(engine) as session:
        environments = session.exec(select(Environment)).all()
        return environments

@app.get("/environment/profile")
def read_environment_profiles():
    with Session(engine) as session:
        environment_profiles = session.exec(select(EnvironmentProfile)).all()
        return environment_profiles

@app.post("/environment")
def create_environment(environment: Environment):
    with Session(engine) as session:
        session.add(environment)
        session.commit()
        session.refresh(environment)
        return environment
    
@app.post("/environment/profile")
def create_environment_profile(environment_profile: EnvironmentProfile):
    with Session(engine) as session:
        session.add(environment_profile)
        session.commit()
        session.refresh(environment_profile)
        return environment_profile

### PLANT ENDPOINTS ###########################################################

@app.get("/plant")
def read_plants():
    with Session(engine) as session:
        plants = session.exec(select(Plant)).all()
        return plants
    

@app.post("/plant")
def create_plant(plant: Plant):
    with Session(engine) as session:
        session.add(plant)
        session.commit()
        session.refresh(plant)
        return plant
