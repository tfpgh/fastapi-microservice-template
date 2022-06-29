from tests import client, test_user_store


def test_get_non_existent_user() -> None:
    test_user_store.reset_store()

    request = client.get("/users/NOT_REAL")
    assert request.status_code == 404
    assert request.json() == {"detail": "User with the given ID could not be found"}


def test_get_user() -> None:
    user_data = {
        "id": "123",
        "name": "Claude Shannon",
        "email": "claude.shannon@aol.com",
    }
    test_user_store.db_dict["123"] = user_data

    request = client.get("/users/123")
    assert request.status_code == 200
    assert request.json() == user_data


def test_add_user() -> None:
    test_user_store.reset_store()

    request = client.post(
        "/users/",
        json={
            "name": "Mike Massimino",
            "email": "MikeMassimino1@aol.com",
        },
    )
    assert request.status_code == 201

    json = request.json()
    assert json["name"] == "Mike Massimino"
    assert json["email"] == "MikeMassimino1@aol.com"
    assert json.get("id") is not None
