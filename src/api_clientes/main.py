# src/api_clientes/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import clientes
from .seed import create_schema, seed_data
import time
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from .config import settings

app = FastAPI()

def wait_for_db():
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    while True:
        try:
            with engine.connect() as conn:
                # SQLAlchemy 2.0 requires text() or exec_driver_sql
                conn.execute(text("SELECT 1"))
            print("Database is ready!")
            break
        except OperationalError:
            print("Database isn't ready yet, waiting...")
            time.sleep(1)

@app.on_event("startup")
def on_startup():
    wait_for_db()
    create_schema()  # <- now safe
    seed_data()      # <- then seed

origins = [
    "http://localhost:8000",  # host port
    "http://localhost:8075",  # container port (if used)
    "*"                       # dev-friendly; lock down in prod
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(clientes.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API Clientes"}
