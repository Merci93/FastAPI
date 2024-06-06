def test_root(test_client) -> None:
    """
    Test case for positive root call.
    """
    response = test_client.get("/v1/root")
    assert response.status_code == 200
    assert response.json()["message"] == "Hi! root api up and running."


def test_get_user_pass(test_client) -> None:
    """
    Test case for positive get user call.
    """
    response = test_client.get("/v1/get_user?query=David")
    assert response.status_code == 200
    assert response.json()["message"] == "Hello David!!! Welcome to my API endpoint."


def test_get_user_fail(test_client) -> None:
    """
    Test case for negative get user call.
    """
    response = test_client.get("/v1/get_user")
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Field required"


def test_non_existent_endpoint(test_client) -> None:
    """
    Test case for non existent endpoint.
    """
    response = test_client.get("/v1/does_not_exist")
    assert response.status_code == 404
    assert response.json()["detail"] == "Not Found"


def test_invalid_method(test_client) -> None:
    """
    Test case for invalid method.
    """
    response = test_client.post("/v1/root", json={"field": "value"})
    assert response.status_code == 405
    assert response.json()["detail"] == "Method Not Allowed"
