from typing import List
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlmodel import Session
from shared.config import Settings
from shared.live_cache import LiveCache
from shared.models.environment_history import EnvironmentHistory, EnvironmentHistoryCreate

environment_history_cache = LiveCache[EnvironmentHistory](
    timestamp_attr=EnvironmentHistory.datetime.key, 
    group_id_attr=EnvironmentHistory.environment_id.key, 
    time_window_minutes=2)

settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def get_session():
    with Session(engine) as session:
        yield session

router = APIRouter(
    prefix="/live",
    tags=["live"]
)

@router.get("/environment-history", response_model=List[dict])
def get_live_environment_history():
    return jsonable_encoder(environment_history_cache.items)

@router.post("/environment-history", response_model=int, operation_id="createLiveEnvironmentHistory")
def post_live_environment_history(*, environment_history: EnvironmentHistoryCreate):
    db_environment_history = EnvironmentHistory.model_validate(environment_history)
    environment_history_cache.add(db_environment_history)
    return len(environment_history_cache.items)