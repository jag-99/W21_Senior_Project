from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), unique=True, index=True)
    hashed_password = Column(String(256))
    phone = Column(String(16))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")

class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64))
    desc = Column(Text)
    price = Column(Integer)
    for_rent = Column(Boolean, default=False)
    address = Column(String(256))
    city = Column(String(64))
    state = Column(String(16))
    zip = Column(Integer)
    views = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Photo(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, index=True)
    listing_id = Column(Integer, ForeignKey("listings.id"))
    src = Column(String(256))

    listing = relationship("Listing", back_populates="photos")

# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")