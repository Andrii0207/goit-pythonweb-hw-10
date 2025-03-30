from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr, condecimal, constr


class ContactBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr = Field(..., max_length=100)
    phone: str = Field(..., max_length=15)
    birth_date: datetime
    additional_data: Optional[str] = None

    class Config:
        orm_mode = True

class ContactCreate(ContactBase):
    pass

class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr] = Field(None, max_length=100)
    phone: Optional[str] = Field(None, max_length=15)
    birth_date: Optional[datetime] = None
    additional_data: Optional[str] = None

    class Config:
        orm_mode = True

class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True