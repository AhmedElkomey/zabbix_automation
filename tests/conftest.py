import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_session():
    """
    Example fixture to mock an HTTP session.
    """
    session = MagicMock()
    session.post.return_value.status_code = 200
    session.post.return_value.json.return_value = {'result': 'success'}
    return session

@pytest.fixture
def mock_api_response():
    """
    Example fixture for a typical Zabbix API response payload.
    """
    return {
        'result': {
            'hostid': '10084',
            'host': 'test_host',
            'status': '0'
        }
    }

@pytest.fixture
def test_credentials():
    """
    Example fixture for test credentials.
    """
    return {
        'url': 'http://test.example.com',
        'username': 'test_user',
        'password': 'test_pass'
    }
