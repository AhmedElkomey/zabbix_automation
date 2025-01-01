import pytest
from zabbix_automator.modules import hosts, web

def test_config_loading():
    """Test whether load_config can successfully load a config.yaml."""
    from zabbix_automator.config import load_config
    config = load_config()
    assert 'zabbix_url' in config
    assert 'api_token' in config

@pytest.fixture
def mock_zabbix_api(mocker):
    """
    Patch the 'zabbix' object (ZabbixAPI instance) inside hosts.py
    so that any call to zabbix.host won't actually reach a real server.
    """
    return mocker.patch('zabbix_automator.modules.hosts.zabbix')

def test_host_creation(mock_zabbix_api):
    """
    Tests that create_host calls the expected zabbix.host.create method
    and returns the mock response.
    """
    mock_response = {'hostids': ['10084']}
    # Because we removed spec=..., this .host.create won't cause attribute errors:
    mock_zabbix_api.host.create.return_value = mock_response

    result = hosts.create_host(
        name="test-host",
        group_ids=["2"],
        ip="192.168.1.100"
    )
    assert result == mock_response
    mock_zabbix_api.host.create.assert_called_once()
