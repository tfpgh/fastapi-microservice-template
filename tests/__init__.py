from fastapi.testclient import TestClient

from app.dependencies import CommonParameters, common_parameters
from app.main import app
from app.stores.user import TestUserStore

test_user_store = TestUserStore()


def test_parameters() -> CommonParameters:
    return CommonParameters(user_store=test_user_store)


app.dependency_overrides[common_parameters] = test_parameters

client = TestClient(app)
