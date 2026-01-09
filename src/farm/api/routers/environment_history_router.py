from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlmodel import Session, select
from shared.config import Settings
from shared.models.environment_history import EnvironmentHistory, EnvironmentHistoryCreate, EnvironmentHistoryPublic

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/environment-history",
    tags=["environment-history"]
)

@router.get("/latest/{environmentId}", response_model=EnvironmentHistoryPublic, operation_id="getLatestEnvironmentHistory")
def get_latest_environment_history(environmentId: int, session = Depends(get_session)):
    environment_history = session.exec(select(EnvironmentHistory)
                                       .where(EnvironmentHistory.environment_id == environmentId)
                                       .order_by(EnvironmentHistory.datetime.desc())
                                       .limit(1)).one_or_none()
    
    print(f"Result type: {type(environment_history)}")
    print(f"Result value: {environment_history}")
    print(f"Is tuple: {isinstance(environment_history, tuple)}")


    if not environment_history:
        raise HTTPException(status_code=404)
    return environment_history

@router.post("", response_model=EnvironmentHistoryPublic, operation_id="createEnvironmentHistory")
def post_environment_history(*, session: Session = Depends(get_session), environment_history: EnvironmentHistoryCreate):
    db_environment_history = EnvironmentHistory.model_validate(environment_history)
    session.add(db_environment_history)
    session.commit()
    session.refresh(db_environment_history)
    return db_environment_history