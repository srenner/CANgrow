from fastapi import FastAPI
from sqlmodel import SQLModel, create_engine
from contextlib import asynccontextmanager
from routers.environment_router import router as environment_router
from routers.plant_router import router as plant_router
from routers.environment_profile_router import router as environment_profile_router
from shared.config import Settings
from fastapi.middleware.cors import CORSMiddleware


settings = Settings()
engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=settings.CONNECT_ARGS)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
    print("Shutdown at " )

app = FastAPI(lifespan=lifespan)
app.include_router(environment_router)
app.include_router(environment_profile_router)
app.include_router(plant_router)

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# ### ENVIRONMENT ENDPOINTS #####################################################

# @app.get("/environment/profile")
# def read_environment_profiles():
#     with Session(engine) as session:
#         environment_profiles = session.exec(select(EnvironmentProfile)).all()
#         return environment_profiles

# @app.post("/environment/profile")
# def create_environment_profile(environment_profile: EnvironmentProfile):
#     with Session(engine) as session:
#         session.add(environment_profile)
#         session.commit()
#         session.refresh(environment_profile)
#         return environment_profile
