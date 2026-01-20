from sqlalchemy import Column, Integer, String, ForeignKey 
from sqlalchemy.orm import relationship
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)

    refresh_tokens = relationship("RefreshToken", back_populates="user")
    customers = relationship("Customer", back_populates="user")
    tasks = relationship("Task", back_populates="user")


class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    token = Column(String, primary_key=True, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    user = relationship("User", back_populates="refresh_tokens")
