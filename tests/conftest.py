import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_session():
    session = MagicMock()
    session.post.return_value.status_code = 200
    session.post.return_value.json.return_value = {'result': 'success'}
    return session

@pytest.fixture
def mock_api_response():
    return {
        'result': {
            'hostid': '10084',
            'host': 'test_host',
            'status': '0'
        }
    }

@pytest.fixture
def test_credentials():
    return {
        'url': 'http://test.example.com',
        'username': 'test_user',
        'password': 'test_pass'
    }
