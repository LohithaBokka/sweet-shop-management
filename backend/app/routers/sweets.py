from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.database.database import SessionLocal
from app.models.sweet import Sweet
from app.schemas.sweet import SweetCreate, SweetOut, SweetUpdate
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from app.schemas.user import Token
from fastapi import Query
router = APIRouter(
    prefix="/api/sweets",
    tags=["sweets"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("", response_model=SweetOut, status_code=status.HTTP_201_CREATED)
def create_sweet(sweet: SweetCreate, db: Session = Depends(get_db)):
    db_sweet = db.query(Sweet).filter(Sweet.name == sweet.name).first()
    if db_sweet:
        raise HTTPException(status_code=400, detail="Sweet already exists")
    
    new_sweet = Sweet(**sweet.dict())
    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)
    return new_sweet

@router.get("", response_model=List[SweetOut])
def get_all_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()

@router.get("/search", response_model=List[SweetOut])
def search_sweets(
    name: str = Query(None),
    category: str = Query(None),
    min_price: float = Query(None),
    max_price: float = Query(None),
    db: Session = Depends(get_db)
):
    query = db.query(Sweet)
    
    if name:
        query = query.filter(Sweet.name.ilike(f"%{name}%"))
    if category:
        query = query.filter(Sweet.category.ilike(f"%{category}%"))
    if min_price is not None:
        query = query.filter(Sweet.price >= min_price)
    if max_price is not None:
        query = query.filter(Sweet.price <= max_price)
    
    return query.all()

@router.put("/{sweet_id}", response_model=SweetOut)
def update_sweet(sweet_id: int, sweet: SweetUpdate, db: Session = Depends(get_db)):
    db_sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    for key, value in sweet.dict(exclude_unset=True).items():
        setattr(db_sweet, key, value)
    
    db.commit()
    db.refresh(db_sweet)
    return db_sweet


@router.delete("/{sweet_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sweet(sweet_id: int, db: Session = Depends(get_db)):
    db_sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    db.delete(db_sweet)
    db.commit()
    return

@router.post("/{sweet_id}/purchase", response_model=SweetOut)
def purchase_sweet(sweet_id: int, db: Session = Depends(get_db)):
    db_sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not db_sweet or db_sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Sweet not available")
    
    db_sweet.quantity -= 1
    db.commit()
    db.refresh(db_sweet)
    return db_sweet

@router.post("/{sweet_id}/restock", response_model=SweetOut)
def restock_sweet(sweet_id: int, quantity: int = 1, db: Session = Depends(get_db)):
    db_sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not db_sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")
    
    db_sweet.quantity += quantity
    db.commit()
    db.refresh(db_sweet)
    return db_sweet
