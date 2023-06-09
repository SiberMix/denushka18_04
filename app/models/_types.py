from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Type(Base):
    """
    Содержит описание общих для всего проекта типов данных
    """

    __tablename__ = "types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    coin_collections = relationship("CoinCollection", back_populates="type")
