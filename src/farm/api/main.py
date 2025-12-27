from typing import List
from fastapi import APIRouter, FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager
import time
from models import Environment, EnvironmentProfile
from models import Plant
from routers.environments import router as environments_router


connect_args = {"check_same_thread": False}
engine = create_engine("sqlite:///src/farm/database/cangrow.db", echo=True, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("Shutdown at " )

router = APIRouter()
app = FastAPI(lifespan=lifespan)
app.include_router(environments_router)

# ### ENVIRONMENT ENDPOINTS #####################################################

# @app.get("/environment/profile")
# def read_environment_profiles():
#     with Session(engine) as session:
#         environment_profiles = session.exec(select(EnvironmentProfile)).all()
#         return environment_profiles

# @app.post("/environment/profile")
# def create_environment_profile(environment_profile: EnvironmentProfile):
#     with Session(engine) as session:
#         session.add(environment_profile)
#         session.commit()
#         session.refresh(environment_profile)
#         return environment_profile

# ### PLANT ENDPOINTS ###########################################################

# @app.get("/plant")
# def read_plants():
#     with Session(engine) as session:
#         plants = session.exec(select(Plant)).all()
#         return plants
    

# @app.post("/plant")
# def create_plant(plant: Plant):
#     with Session(engine) as session:
#         session.add(plant)
#         session.commit()
#         session.refresh(plant)
#         return plant
