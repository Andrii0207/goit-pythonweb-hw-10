from typing import List, Optional

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.database.models import User
from src.schemas import ContactResponse, ContactCreate, ContactUpdate
from src.services.auth import get_current_user
from src.services.contacts import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])

@router.get("/", response_model=List[ContactResponse])
async def read_contacts(
        skip: int = 0,
        limit: int = 100,
        query: Optional[str]=None,
        db: AsyncSession = Depends(get_db),
        user: User = Depends(get_current_user)):
    contact_service = ContactService(db)
    contacts = await contact_service.get_contacts(skip, limit, user, query)
    return contacts

@router.get("/birthdays", response_model=List[ContactResponse])
async def get_birthdays(db: AsyncSession = Depends(get_db), user: User = Depends(get_current_user)):
    contact_service = ContactService(db)
    contacts = await contact_service.get_birthdays(user)
    return contacts

@router.get("/{contact_id}", response_model=ContactResponse)
async def read_contact(
        contact_id: int,
        db: AsyncSession = Depends(get_db),
        user: User = Depends(get_current_user)):
    contact_service = ContactService(db)
    contact = await contact_service.get_contact(contact_id, user)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact

@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(
        body: ContactCreate,
        db: AsyncSession = Depends(get_db),
        user: User = Depends(get_current_user)):
    contact_service = ContactService(db)
    return await contact_service.create_contact(body, user)

@router.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(
        body: ContactUpdate,
        contact_id: int, db:
        AsyncSession = Depends(get_db),
        user: User = Depends(get_current_user)):
    contact_service = ContactService(db)
    contact = await contact_service.update_contact(contact_id, body, user)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact

@router.delete("/{contact_id}", response_model=ContactResponse)
async def remove_contact(
        contact_id: int,
        db: AsyncSession = Depends(get_db),
        user: User = Depends(get_current_user)):
    contact_service = ContactService(db)
    contact = await contact_service.remove_contact(contact_id, user)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact