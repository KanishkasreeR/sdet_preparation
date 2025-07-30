import pytest

@pytest.fixture
def sample_user():
    return {
        "name": "kanishka",
        "email": "kanishka@gmail.com",
        "password": "Pass@123"
    }
