from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from sqlmodel import Session, create_engine
from models import Plant
from config import Settings

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

router = APIRouter(
    prefix="/plant",
    tags=["plant"]
)

@router.get("", response_model=List[Plant], operation_id="listPlants")
def read_plants():
    with Session(engine) as session:
        plants = session.exec(select(Plant)
                              .where(Plant.is_active == True)).scalars().all()
        return plants
    
@router.post("", response_model=Plant, operation_id="createPlant")
def create_plant(plant: Plant):
    with Session(engine) as session:
        session.add(plant)
        session.commit()
        session.refresh(plant)
        return plant
