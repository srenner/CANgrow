from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from sqlmodel import Session, create_engine
from shared.config import Settings
from shared import Plant, PlantCreate, PlantPublic

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

router = APIRouter(
    prefix="/plant",
    tags=["plant"]
)

@router.get("", response_model=List[PlantPublic], operation_id="listPlants")
def read_plants():
    with Session(engine) as session:
        plants = session.exec(select(Plant)
                              .where(Plant.is_active == True)).scalars().all()
        return plants
    
@router.post("", response_model=PlantPublic, operation_id="createPlant")
def create_plant(plant: PlantCreate):
    with Session(engine) as session:
        db_plant = Plant.model_validate(plant)
        session.add(db_plant)
        session.commit()
        session.refresh(db_plant)
        return db_plant
