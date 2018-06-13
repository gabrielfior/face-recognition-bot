import pytest
from src.DbService import DbService

@pytest.fixture(scope="module")
def dbService() -> DbService:
    testDatafile = "data_test.json"

    return DbService(testDatafile)