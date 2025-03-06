from ..database.database import Base
from sqlalchemy import Boolean, Column, Integer, String


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    is_active = Column(Boolean, default=True)
