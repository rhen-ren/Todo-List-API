from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from model.note import Note
from db import Base

class User(Base):
    __tablename__ = "User"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    email: Mapped[str] = mapped_column(String(200), nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)

    notes: Mapped["Note"] = relationship("Note", back_populates="user")