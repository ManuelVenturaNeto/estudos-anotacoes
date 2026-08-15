import uvicorn
from fastapi import FastAPI

from src.infra.database import Base, engine
from src.routers import router

app = FastAPI()
app.include_router(router)

Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
