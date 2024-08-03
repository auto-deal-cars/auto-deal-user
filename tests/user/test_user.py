"""Test user domain model"""
import pytest
from user.domain.address import Address
from user.domain.user import User

@pytest.fixture
def user() -> User:
    """User fixture"""
    address = Address(
        city='São Paulo',
        federal_unit='SP',
        neighborhood='Jardim Paulista',
        street_name='Av. Paulista',
        street_number='123',
        zip_code='13000-000'
    )
    return User(
        id='123',
        email='john.doe@example.com',
        first_name='John',
        last_name='Doe',
        password='password',
        cpf='12345678909',
        address=address,
    )

def test_user_model(user: User):
    """Test user model"""
    assert user.id == '123'
    assert user.email == 'john.doe@example.com'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.password == 'password'
    assert user.cpf == '12345678909'
    assert user.address == Address(
        city='São Paulo',
        federal_unit='SP',
        neighborhood='Jardim Paulista',
        street_name='Av. Paulista',
        street_number='123',
        zip_code='13000-000'
    )
