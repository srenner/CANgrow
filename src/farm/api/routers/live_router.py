from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlmodel import Session
from shared.config import Settings
from shared.live_cache import LiveCache
from shared.models.environment_history import EnvironmentHistory, EnvironmentHistoryCreate, EnvironmentHistoryPublic

environment_history_cache = LiveCache[EnvironmentHistory](
    timestamp_attr=EnvironmentHistory.datetime.key, 
    group_id_attr=EnvironmentHistory.environment_id.key, 
    time_window_minutes=15)

ws_connections: dict[int, WebSocket] = {}

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

@router.get("/environment-history/{environmentId}", response_model=List[EnvironmentHistoryPublic])
def get_live_environment_history_by_group(environmentId: int):
        return jsonable_encoder(environment_history_cache.get_group(environmentId))

@router.websocket("/ws/environment-history/{environmentId}")
async def environment_history_ws(websocket: WebSocket, environmentId: int):
    await websocket.accept()
    ws_connections[environmentId] = websocket
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        ws_connections.pop(environmentId, None)

@router.post("/environment-history", response_model=int, operation_id="createLiveEnvironmentHistory")
async def post_live_environment_history(*, environment_history: EnvironmentHistoryCreate):
    validated_environment_history = EnvironmentHistory.model_validate(environment_history)
    environment_history_cache.add(validated_environment_history)

    disconnected = []
    for connection in ws_connections:
        try:
              print("sending~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
              #await connection.send_json({id: 1})
              await connection.send_text("hello ws")
              # await connection.send_json(validated_environment_history.model_dump())
        except:
            disconnected.append(connection)
    for connection in disconnected:
         # ws_connections.remove(connection)
         # ws_connections.pop()
         pass

    return len(environment_history_cache.items)