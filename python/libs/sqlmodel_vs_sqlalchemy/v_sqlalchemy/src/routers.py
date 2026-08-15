from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .infra.database import get_session
from .infra.entity import Pets
from .infra.models import Pet, PetUpdate

router = APIRouter()


# Create a Pet
@router.post("/pets/", response_model=Pet)
def create_pet(pet: Pet, session: Session = Depends(get_session)):
    db_pet = Pets(**pet.model_dump())
    session.add(db_pet)
    session.commit()
    session.refresh(db_pet)
    return db_pet


# Read all pets
@router.get("/pets/", response_model=list[Pet])
def read_pets(
    skip: int = 0, limit: int = 10, session: Session = Depends(get_session)
):
    pets = session.query(Pets).offset(skip).limit(limit).all()
    return pets


# Read a pet by ID
@router.get("/pets/{pet_id}", response_model=Pet)
def read_pet(pet_id: int, session: Session = Depends(get_session)):
    pet = session.query(Pets).filter(Pets.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet


# Update a Pet
@router.put("/pets/{pet_id}", response_model=Pet)
def update_pet(
    pet_id: int, pet_data: PetUpdate, session: Session = Depends(get_session)
):
    pet = session.query(Pets).filter(Pets.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    for field, value in pet_data.model_dump(exclude_unset=True).items():
        setattr(pet, field, value)

    session.commit()
    session.refresh(pet)
    return pet


# Delete a Pet
@router.delete("/pets/{pet_id}", response_model=Pet)
def delete_pet(pet_id: int, session: Session = Depends(get_session)):
    pet = session.query(Pets).filter(Pets.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    session.delete(pet)
    session.commit()
    return pet
