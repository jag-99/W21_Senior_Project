from typing import List, Optional
from pydantic import BaseModel

# Photo
class PhotoBase(BaseModel):
    pass

class PhotoCreate(PhotoBase):
    pass

class Photo(PhotoBase):
    id: int
    listing_id: int
    src: str

# Listing
class ListingBase(BaseModel):
    title: str
    desc: str

class ListingCreate(ListingBase):
    pass

class Listing(ListingBase):
    id: int
    price: int
    for_rent: bool
    address: str
    city: str
    state: str
    zip: int
    views: int
    owner_id: int
    photos: List[Photo] = []

    class Config:
        orm_mode = True

# User
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    # items: List[Item] = []
    listings: List[Listing] = []

    class Config:
        orm_mode = True

# class ItemBase(BaseModel):
#     title: str
#     description: Optional[str] = None

# class ItemCreate(ItemBase):
#     pass

# class Item(ItemBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True