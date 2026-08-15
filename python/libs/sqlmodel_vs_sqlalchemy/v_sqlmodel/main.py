import uvicorn
from fastapi import FastAPI
from src.infra.database import engine
from src.routers import router
from sqlmodel import SQLModel

app = FastAPI()
app.include_router(router)

SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
