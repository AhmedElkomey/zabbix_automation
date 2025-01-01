import pytest
from unittest.mock import MagicMock
from zabbix_automator.modules import web
from zabbix_automator.modules import hosts
from zabbix_utils import ZabbixAPI

def test_create_host(monkeypatch):
  mock_zabbix = MagicMock(spec=ZabbixAPI)
  monkeypatch.setattr(hosts,'zabbix', mock_zabbix)
  mock_zabbix.host.create.return_value = {"hostids": ["123"]}
  result = hosts.create_host(name="test-host", group_ids=["2"], ip="127.0.0.1")
  assert result == {"hostids": ["123"]}
  mock_zabbix.host.create.assert_called_once()

def test_create_host_failed(monkeypatch):
  mock_zabbix = MagicMock(spec=ZabbixAPI)
  monkeypatch.setattr(hosts, 'zabbix', mock_zabbix)
  mock_zabbix.host.create.side_effect = Exception("API error")
  with pytest.raises(Exception, match="Failed to create host: API error"):
        hosts.create_host(name="test-host", group_ids=["2"], ip="127.0.0.1")
  mock_zabbix.host.create.assert_called_once()


def test_get_host(monkeypatch):
  mock_zabbix = MagicMock(spec=ZabbixAPI)
  monkeypatch.setattr(hosts, 'zabbix', mock_zabbix)
  mock_zabbix.host.get.return_value = [{"hostid": "123", "host": "test-host"}]
  result = hosts.get_host("test-host")
  assert result == [{"hostid": "123", "host": "test-host"}]
  mock_zabbix.host.get.assert_called_once()
  mock_zabbix.host.get.assert_called_with(filter={"host": "test-host"})


def test_get_host_not_found(monkeypatch):
      mock_zabbix = MagicMock(spec=ZabbixAPI)
      monkeypatch.setattr(hosts, 'zabbix', mock_zabbix)
      mock_zabbix.host.get.return_value = []
      result=hosts.get_host(name="non-existent-host")
      assert result == []
      mock_zabbix.host.get.assert_called_once()

def test_get_host_failed(monkeypatch):
      mock_zabbix = MagicMock(spec=ZabbixAPI)
      monkeypatch.setattr(hosts, 'zabbix', mock_zabbix)
      mock_zabbix.host.get.side_effect = Exception("API error")
      with pytest.raises(Exception, match="Failed to get host: API"):
        hosts.get_host(name="test-host")
        mock_zabbix.host.get.assert_called_once()

def test_create_web_scenario(monkeypatch):
    mock_zabbix = MagicMock(spec=ZabbixAPI)
    monkeypatch.setattr(web, 'zabbix', mock_zabbix)
    mock_zabbix.httptest.create.return_value = {"httptestids": ["456"]}

    result = web.create_web_scenario(
        hostid="123",
        name="test-scenario",
        url="http://example.com",
        status_codes="200",
        required="Welcome",
    )
    assert result == {"httptestids": ["456"]}
    mock_zabbix.httptest.create.assert_called_once()

def test_create_web_scenario_failed(monkeypatch):
     mock_zabbix = MagicMock(spec=ZabbixAPI)
     monkeypatch.setattr(web, 'zabbix', mock_zabbix)
     mock_zabbix.httptest.create.side_effect = Exception("API error")
     with pytest.raises(Exception, match="Failed to create web scenario: API error"):
       web.create_web_scenario(
            hostid="123",
            name="test-scenario",
            url="http://example.com",
            status_codes="200",
            required="Welcome",
       )
     mock_zabbix.httptest.create.assert_called_once()


def test_get_web_scenario(monkeypatch):
    mock_zabbix = MagicMock(spec=ZabbixAPI)
    monkeypatch.setattr(web, 'zabbix', mock_zabbix)
    mock_zabbix.httptest.get.return_value = [{"httptestid": "456", "name": "test-scenario"}]

    result = web.get_web_scenario(hostid="123", name="test-scenario")
    assert result == [{"httptestid": "456", "name": "test-scenario"}]
    mock_zabbix.httptest.get.assert_called_once()
    mock_zabbix.httptest.get.assert_called_with(filter={"name": "test-scenario", "hostid": "123"})


def test_get_web_scenario_not_found(monkeypatch):
      mock_zabbix = MagicMock(spec=ZabbixAPI)
      monkeypatch.setattr(web, 'zabbix', mock_zabbix)
      mock_zabbix.httptest.get.return_value = []
      result=web.get_web_scenario(hostid="123", name="non-existent-scenario")
      assert result == []
      mock_zabbix.httptest.get.assert_called_once()
      mock_zabbix.httptest.get.assert_called_with(filter={"name": "non-existent-scenario", "hostid": "123"})

def test_get_web_scenario_failed(monkeypatch):
      mock_zabbix = MagicMock(spec=ZabbixAPI)
      monkeypatch.setattr(web, 'zabbix', mock_zabbix)
      mock_zabbix.httptest.get.side_effect = Exception("API error")
      with pytest.raises(Exception, match="Failed to get web scenario: API error"):
        web.get_web_scenario(hostid="123", name="test-scenario")
      mock_zabbix.httptest.get.assert_called_once()

def test_list_web_scenarios(monkeypatch):
      mock_zabbix = MagicMock(spec=ZabbixAPI)
      monkeypatch.setattr(web, 'zabbix', mock_zabbix)
      mock_zabbix.httptest.get.return_value = [
        {"httptestid": "456", "name": "test-scenario-1"},
        {"httptestid": "789", "name": "test-scenario-2"},
      ]
      result= web.list_web_scenarios(hostid="123")
      assert result == [
        {"httptestid": "456", "name": "test-scenario-1"},
        {"httptestid": "789", "name": "test-scenario-2"},
       ]
      mock_zabbix.httptest.get.assert_called_once()
      mock_zabbix.httptest.get.assert_called_with(filter={"hostid": "123"},output=['httptestid','name'])


def test_list_web_scenarios_failed(monkeypatch):
    mock_zabbix = MagicMock(spec=ZabbixAPI)
    monkeypatch.setattr(web, 'zabbix', mock_zabbix)
    mock_zabbix.httptest.get.side_effect = Exception("API error")
    with pytest.raises(Exception, match="Failed to list web scenarios: API error"):
         web.list_web_scenarios(hostid="123")
    mock_zabbix.httptest.get.assert_called_once()
