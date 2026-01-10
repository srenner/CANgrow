from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy import create_engine
from sqlmodel import Session, select
from shared.config import Settings
from shared.models.environment_target import EnvironmentTarget, EnvironmentTargetCreate, EnvironmentTargetPublic

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/environment-target",
    tags=["enviornment-target"]
)

@router.get("/{environmentProfileId}", response_model=List[EnvironmentTargetPublic], operation_id="getEnvironmentTargetsForProfile")
def get_environment_targets(*, session = Depends(get_session), environmentProfileId: int):
    environment_targets = session.exec(select(EnvironmentTarget)
                                       .where(EnvironmentTarget.is_active == True)
                                       .where(EnvironmentTarget.environment_profile_id == environmentProfileId)
                                       ).all()
    return environment_targets

@router.post("", response_model=EnvironmentTargetPublic, operation_id="createEnvironmentTarget")
def post_environment_target(*, session: Session = Depends(get_session), environment_target: EnvironmentTargetCreate):
    db_environment_target = EnvironmentTarget.model_validate(environment_target)
    session.add(db_environment_target)
    session.commit()
    session.refresh(db_environment_target)
    return db_environment_target