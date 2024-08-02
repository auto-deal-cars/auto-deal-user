"""User domain model."""
from typing import Optional
from pydantic import BaseModel, Field
from user.domain.address import Address

class User(BaseModel):
    """User domain model."""
    id: Optional[str] = Field(default=None)
    email: str = Field(..., email=True)
    password: str = Field(..., min_length=8)
    first_name: str = Field(..., description='First name')
    last_name: str = Field(..., description='Last name')
    address: Address = Field(..., description='Address')
    cpf: str = Field(..., description="CPF", min_length=11, max_length=11)
