from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from .infra.database import get_session
from .infra.entity import Pets

router = APIRouter()


# Create a Pets
@router.post("/pets/", response_model=Pets)
def create_pet(pet: Pets, session: Session = Depends(get_session)):
    session.add(pet)
    session.commit()
    session.refresh(pet)
    return pet


# Read all pets
@router.get("/pets/", response_model=list[Pets])
def read_pets(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    pets = session.exec(select(Pets).offset(skip).limit(limit)).all()
    return pets


# Read a pet by ID
@router.get("/pets/{pet_id}", response_model=Pets)
def read_pet(pet_id: int, session: Session = Depends(get_session)):
    pet = session.get(Pets, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pets not found")
    return pet


# Update a Pets
@router.put("/pets/{pet_id}", response_model=Pets)
def update_pet(
    pet_id: int, pet_data: Pets, session: Session = Depends(get_session)
):
    pet = session.get(Pets, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pets not found")

    for field, value in pet_data.model_dump(exclude_unset=True).items():
        setattr(pet, field, value)

    session.commit()
    session.refresh(pet)
    return pet


# Delete a Pets
@router.delete("/pets/{pet_id}", response_model=Pets)
def delete_pet(pet_id: int, session: Session = Depends(get_session)):
    pet = session.get(Pets, pet_id)
    if not pet:
        raise HTTPException(status_code=404, detail="Pets not found")

    session.delete(pet)
    session.commit()
    return pet
