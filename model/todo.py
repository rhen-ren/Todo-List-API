from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from db import Base


class Todo(Base):
    __tablename__ = "Todo"
    
    id: Mapped[int] = mapped_column(primary_key = True)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"))
    title: Mapped[str] = mapped_column(String(100), nullable = False)
    description: Mapped[str] = mapped_column(String(300), nullable = True)

    user: Mapped[list["User"]] = relationship("User", back_populates = "todos")
