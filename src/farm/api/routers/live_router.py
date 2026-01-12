from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import create_engine
from sqlmodel import Session, select
from shared.config import Settings
from shared.live_cache import LiveCache
from shared.models.environment_history import EnvironmentHistory, EnvironmentHistoryCreate, EnvironmentHistoryPublic
import json

environment_history_cache = LiveCache(EnvironmentHistory, 'environment_id', 15)


settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/live",
    tags=["live"]
)

@router.get("/envioronment-history", response_model=str)
def get_live_environment_history():
    data = [item.__dict__ for item in environment_history_cache.items]
    return json.dumps(data, default=str)

@router.post("/environment-history", response_model=int, operation_id="createLiveEnvironmentHistory")
def post_live_environment_history(*, environment_history: EnvironmentHistoryCreate):
    db_environment_history = EnvironmentHistory.model_validate(environment_history)
    environment_history_cache.add(db_environment_history)
    return len(environment_history_cache.items)


    # print(db_environment_history.model_dump_json())