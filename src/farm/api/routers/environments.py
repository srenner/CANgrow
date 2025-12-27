from typing import List
from fastapi import APIRouter
from sqlalchemy import select
from sqlmodel import Session, create_engine
from models import Environment
from config import Settings

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

router = APIRouter(
    prefix="/environment",
    tags=["environment"]
)

@router.get("", response_model=List[Environment], operation_id="listEnvironments")
def read_environments():
    with Session(engine) as session:
        environments = session.exec(select(Environment)).scalars().all()
        return environments
    
@router.post("", response_model=Environment, operation_id="createEnvironment")
def create_environment(environment: Environment):
    with Session(engine) as session:
        session.add(environment)
        session.commit()
        session.refresh(environment)
        return environment