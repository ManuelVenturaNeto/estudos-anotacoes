from sqlalchemy import Column, Integer, String

from .database import Base


class Pets(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    type = Column(String)
    age = Column(Integer, nullable=True)
