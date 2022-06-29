from tests import client


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == '"Hello, Root!"'
