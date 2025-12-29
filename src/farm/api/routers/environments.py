from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from sqlmodel import Session, create_engine
from models import Environment, EnvironmentCreate, EnvironmentPublic
from config import Settings

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

router = APIRouter(
    prefix="/environment",
    tags=["environment"]
)

@router.get("", response_model=List[EnvironmentPublic], operation_id="listEnvironments")
def read_environments():
    with Session(engine) as session:
        environments = session.exec(select(Environment)
                                    .where(Environment.is_active == True)).scalars().all()
        return environments
    
@router.post("", response_model=EnvironmentPublic, operation_id="createEnvironment")
def create_environment(environment: EnvironmentCreate):
    with Session(engine) as session:
        db_environment = Environment.model_validate(environment)
        session.add(db_environment)
        session.commit()
        session.refresh(db_environment)
        return db_environment