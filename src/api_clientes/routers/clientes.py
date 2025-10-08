# src/api_clientes/routers/clientes.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter(prefix="/clientes", tags=["clientes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/lookup", response_model=schemas.ClienteIdResponse)
def lookup_client_id(
    dni: str = Query(..., min_length=8, max_length=8, pattern=r"^\d{8}$"),
    db: Session = Depends(get_db),
):
    cliente = db.query(models.Cliente).filter(models.Cliente.dni == dni).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"id": cliente.id}
