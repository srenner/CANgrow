from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlmodel import Session, create_engine
from shared.config import Settings
from shared import EnvironmentProfile, EnvironmentProfileCreate, EnvironmentProfilePatch, EnvironmentProfilePublic

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/environment-profile",
    tags=["environment-profile"]
)

@router.get("", response_model=List[EnvironmentProfilePublic], operation_id="listEnvironmentProfiles")
def get_environment_profiles(*, session = Depends(get_session)):
    environment_profiles = session.exec(select(EnvironmentProfile)
                                        .where(EnvironmentProfile.is_active == True)).scalars().all()
    return environment_profiles

@router.get("/{id}", response_model=EnvironmentProfilePublic, operation_id="getEnvironmentProfile")
def get_environment_profile(*, session: Session = Depends(get_session), id: int, include_inactive: bool = False):
    query = select(EnvironmentProfile).where(EnvironmentProfile.id == id)
    if not include_inactive:
        query = query.where(EnvironmentProfile.is_active == True)
    environment_profile = session.exec(query).scalar_one_or_none()
    if environment_profile is None:
        raise HTTPException(status_code=404)
    return environment_profile

@router.post("", response_model=EnvironmentProfilePublic, operation_id="createEnvironmentProfile")
def post_environment_profile(*, session: Session = Depends(get_session), environment_profile: EnvironmentProfileCreate):
    db_environment_profile = EnvironmentProfile.model_validate(environment_profile)
    session.add(db_environment_profile)
    session.commit()
    session.refresh(db_environment_profile)
    return db_environment_profile