# src/api_clientes/schemas.py
from pydantic import BaseModel, Field
from pydantic import ConfigDict

class ClienteBase(BaseModel):
    full_name: str
    email: str
    dni: str = Field(..., min_length=8, max_length=8)
    phone: str

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ClienteIdResponse(BaseModel):
    id: int
    model_config = ConfigDict(from_attributes=True)