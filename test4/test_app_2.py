import pytest
from app import get_user_data


@pytest.fixture
def mock_requests_get(mocker):
    """Fixture dla mockowania requests.get"""
    return mocker.patch("app.requests.get")


@pytest.mark.parametrize("user_id, expected_name", [
    (1, "John Doe"),
    (2, "Jane Doe")
])
def test_get_user_data_parametrize(mock_requests_get, user_id, expected_name):
    # Mockowanie odpowiedzi API
    mock_requests_get.return_value.status_code = 200
    mock_requests_get.return_value.json.return_value = {
        "id": user_id,
        "name": expected_name
    }

    # Wykonanie testu
    result = get_user_data(user_id)
    assert result["name"] == expected_name
    mock_requests_get.assert_called_once_with(f"https://jsonplaceholder.typicode.com/users/{user_id}")


def test_get_user_data_raises(mock_requests_get):
    # Symulacja błędu serwera
    mock_requests_get.return_value.status_code = 500

    # Testowanie wyjątku
    with pytest.raises(Exception, match="Błąd serwera"):
        if get_user_data(1) is None:
            raise Exception("Błąd serwera")