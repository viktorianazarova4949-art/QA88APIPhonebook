
import pytest
import requests
from config import *


@pytest.fixture(scope="session")
def registration_url():
    return BESE_URL+API_VERSION+REGISTRATION_URL

@pytest.fixture(scope="session")
def login_url():
    return BESE_URL+API_VERSION+LOGIN_URL

@pytest.fixture(scope="session")
def session_id():
    s=requests.Session()
    yield s  # kanta testista ja kini
    s.close()


