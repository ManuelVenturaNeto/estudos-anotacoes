from sqlmodel import SQLModel, Session, create_engine


# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


# Dependency
def get_session():
    with Session(engine) as session:
        yield session
