from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# SQLAlchemy model
Base = declarative_base()

# Database setup
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
