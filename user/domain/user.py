"""User domain model."""
from typing import Optional
from pydantic import BaseModel, Field, ValidationError, field_validator
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
    accepted_terms: bool = Field(..., description="Accepted terms")

    @field_validator('accepted_terms')
    def check_accepted_terms(cls, value):
        """Check if accepted_terms is true."""
        if not value:
            raise ValidationError.from_exception_data(
                title='accepted_terms must be True',
                line_errors=['accepted_terms must be True']
            )
        return value
