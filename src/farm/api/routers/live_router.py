from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlmodel import Session, select
from shared.config import Settings
from shared.models.environment_history import EnvironmentHistory, EnvironmentHistoryCreate, EnvironmentHistoryPublic
import json

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/live",
    tags=["live"]
)

@router.post("/environment-history", response_model=None, operation_id="createLiveEnvironmentHistory")
def post_live_environment_history(*, environment_history: EnvironmentHistoryCreate):
    db_environment_history = EnvironmentHistory.model_validate(environment_history)
    print(db_environment_history.model_dump_json())