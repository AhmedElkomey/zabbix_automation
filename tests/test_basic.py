import pytest
from zabbix_automator.modules import hosts, web

def test_config_loading():
    """Test configuration loading"""
    from zabbix_automator.config import load_config
    config = load_config()
    assert 'zabbix_url' in config
    assert 'api_token' in config

@pytest.fixture
def mock_zabbix_api(mocker):
    """Mock Zabbix API calls"""
    return mocker.patch('zabbix_automator.api.ZabbixAPI')

def test_host_creation(mock_zabbix_api):
    """Test host creation functionality"""
    mock_response = {'hostids': ['10084']}
    mock_zabbix_api.host.create.return_value = mock_response
    
    result = hosts.create_host(
        name="test-host",
        group_ids=["2"],
        ip="192.168.1.100"
    )
    assert result == mock_response
