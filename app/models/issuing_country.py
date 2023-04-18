from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class IssuingCountry(Base):
    """
    Хранит информацию об стране, выпустившей монеты коллекции.
    """

    __tablename__ = "issuing_countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    coin_collections = relationship("CoinCollection", back_populates="issuing_country")
