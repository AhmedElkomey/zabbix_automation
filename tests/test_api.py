import unittest
from unittest.mock import patch, MagicMock
from zabbix_automator.api import ZabbixAPI

class TestZabbixAPI(unittest.TestCase):
    def setUp(self):
        self.zabbix_api = ZabbixAPI('http://test.example.com/api_jsonrpc.php', 'test_user', 'test_pass')

    def test_api_login(self):
        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = {'result': 'auth_token'}
            self.zabbix_api.login()
            self.assertEqual(self.zabbix_api.auth, 'auth_token')

    def test_failed_api_login(self):
        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = {'error': {'code': -32602, 'message': 'Invalid credentials'}}
            with self.assertRaises(AuthenticationError):
                self.zabbix_api.login()

    def test_api_call(self):
        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = {'result': ['data']}
            result = self.zabbix_api.api_call('test.method', {'param': 'value'})
            self.assertEqual(result, ['data'])

    def test_api_error_handling(self):
        with patch('requests.post') as mock_post:
            mock_post.return_value.json.return_value = {'error': {'code': 123, 'message': 'Test error'}}
            with self.assertRaises(APIError):
                self.zabbix_api.api_call('test.method', {})

    def test_get_host_groups(self):
        with patch.object(ZabbixAPI, 'api_call') as mock_call:
            mock_call.return_value = [{'groupid': '1', 'name': 'test_group'}]
            groups = self.zabbix_api.get_host_groups()
            self.assertEqual(len(groups), 1)
            self.assertEqual(groups[0]['name'], 'test_group')

    def test_get_triggers(self):
        with patch.object(ZabbixAPI, 'api_call') as mock_call:
            mock_data = [{'triggerid': '1', 'description': 'Test trigger'}]
            mock_call.return_value = mock_data
            triggers = self.zabbix_api.get_triggers()
            self.assertEqual(triggers[0]['description'], 'Test trigger')

    def test_update_host(self):
        with patch.object(ZabbixAPI, 'api_call') as mock_call:
            mock_call.return_value = {'hostids': ['123']}
            result = self.zabbix_api.update_host('123', {'status': '0'})
            self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
