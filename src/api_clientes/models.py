# src/api_clientes/models.py
from sqlalchemy import Column, Integer, String, Sequence
from .database import Base

# Create a custom sequence starting at 100001
cliente_id_seq = Sequence("cliente_id_seq", start=100001)

class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, cliente_id_seq, primary_key=True, server_default=cliente_id_seq.next_value())
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    dni = Column(String(8), nullable=False, unique=True, index=True)
    phone = Column(String, nullable=True)
