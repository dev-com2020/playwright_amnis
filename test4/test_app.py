import unittest
from unittest.mock import patch
from app import get_user_data


class TestApp(unittest.TestCase):

    @patch("app.requests.get")
    def test_get_user_data_success(self, mock_get):
        # Mock odpowiedzi z API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com"
        }

        result = get_user_data(1)

        # Sprawdzanie oczekiwanych rezultatów
        self.assertEqual(result["name"], "John Doe")
        self.assertEqual(result["email"], "john@example.com")

    @patch("app.requests.get")
    def test_get_user_data_failure(self, mock_get):
        # Symulacja błędu serwera
        mock_get.return_value.status_code = 404

        result = get_user_data(999)
        self.assertIsNone(result)

    def test_example(self):
        with patch("app.requests.get") as mock_get:
            mock_get.return_value.status_code = 200
            # Testowanie...


if __name__ == "__main__":
    unittest.main()