"""Address"""
from pydantic import Field, BaseModel

class Address(BaseModel):
    """Address"""
    zip_code: str = Field(..., description='Zip code')
    street_name: str = Field(..., description='Street name')
    street_number: str = Field(..., description='Street number')
    neighborhood: str = Field(..., description='Neighborhood')
    city: str = Field(..., description='City')
    federal_unit: str = Field(..., description='Federal unit')
