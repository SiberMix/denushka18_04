from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CoinCollection(Base):
    """
    Хранит информацию о коллекции монет, такую как название, год выпуска, номинал, и т.д.
    """
    __tablename__ = "coin_collections"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    type_id = Column(Integer, ForeignKey("types.id"))
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    nominal_value = Column(String, index=True)
    mint_id = Column(Integer, ForeignKey("mints.id"))
    issuing_country_id = Column(Integer, ForeignKey("issuing_countries.id"))
    year_of_issue = Column(String, index=True)
    serial_number = Column(String, index=True)

    type = relationship("Type", back_populates="coin_collections")
    currency = relationship("Currency", back_populates="coin_collections")
    mint = relationship("Mint", back_populates="coin_collections")
    issuing_country = relationship("IssuingCountry", back_populates="coin_collections")
    owner_id = Column(Integer, ForeignKey("users.id"))