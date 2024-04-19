import redshift_connector
from unittest.mock import patch, MagicMock

import redshift_connector.error

from PromptEngineering.connect_db import connect_to_redshift
import pytest


@pytest.fixture
def mock_connect():
    with patch("redshift_connector.connect") as mock_conn:
        yield mock_conn


def test_successful_connection(mock_connect):
    # Mock the return value of connect to simulate successful connection
    mock_connect.return_value = MagicMock()

    # Call the function with any credentials (not used for testing)
    conn = connect_to_redshift("host", 5439, "user", "password", "dbname")

    # Assert that the connect function was called with expected arguments
    mock_connect.assert_called_once_with(
        host="host", port=5439, user="user", password="password", database="dbname"
    )

    # Assert that a connection object is returned
    assert isinstance(conn, MagicMock)


def test_connection_error(mock_connect):
    # Mock the connect function to raise an exception
    mock_connect.side_effect = redshift_connector.Error("Connection failed")

    # Call the function and expect an exception
    with pytest.raises(redshift_connector.Error):
        connect_to_redshift("host", 5439, "user", "password", "dbname")

    # Assert that the connect function was called
    mock_connect.assert_called_once()


def test_invalid_arguments(mock_connect):
    # Test with missing argument
    with pytest.raises(TypeError):
        connect_to_redshift("host", 5439, "user", "password")

    # Test with unexpected argument type
    # with pytest.raises(redshift_connector.error.ProgrammingError):
    #     connect_to_redshift("host", 5439, "user", "password", 123)

# Optional test: Mocked connection can be used for methods
def test_mocked_connection_methods(mock_connect):
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn

    conn = connect_to_redshift("host", 5439, "user", "password", "dbname")

    # You can test methods on the mocked connection object here
    mock_conn.cursor.assert_not_called()
    conn.cursor()  # This will call the mocked cursor method
    mock_conn.cursor.assert_called_once()
