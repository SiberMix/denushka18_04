from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class Currency(Base):
    __tablename__ = "currencies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    coin_collections = relationship("CoinCollection", back_populates="currency")
