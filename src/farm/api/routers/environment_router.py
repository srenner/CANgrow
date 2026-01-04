from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlmodel import Session, create_engine
from config import Settings
from models.environment import Environment, EnvironmentCreate, EnvironmentPatch, EnvironmentPublic


settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/environment",
    tags=["environment"]
)

@router.get("", response_model=List[EnvironmentPublic], operation_id="listEnvironments")
def get_environments(*, session = Depends(get_session)):
    environments = session.exec(select(Environment)
                                .where(Environment.is_active == True)).scalars().all()
    return environments

@router.get("/{id}", response_model=EnvironmentPublic, operation_id="getEnvironment")
def get_environment(*, session: Session = Depends(get_session), id: int, include_inactive: bool = False):
    query = select(Environment).where(Environment.id == id)
    if not include_inactive:
        query = query.where(Environment.is_active == True)
    environment = session.exec(query).scalar_one_or_none()
    if environment is None:
        raise HTTPException(status_code=404)
    return environment

@router.post("", response_model=EnvironmentPublic, operation_id="createEnvironment")
def post_environment(*, session: Session = Depends(get_session), environment: EnvironmentCreate):
    db_environment = Environment.model_validate(environment)
    session.add(db_environment)
    session.commit()
    session.refresh(db_environment)
    return db_environment
    
@router.patch("/{id}", response_model=EnvironmentPublic, operation_id="updateEnvironment")
def patch_environment(*, session: Session = Depends(get_session), id: int, environment: EnvironmentPatch):
    db_environment = session.get(Environment, id)
    if not db_environment:
        raise HTTPException(status_code=404, detail="Environment Not Found")
    update_data = environment.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_environment, field, value)
    session.add(db_environment)
    session.commit()
    session.refresh(db_environment)
    return db_environment
