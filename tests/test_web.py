import unittest
from unittest.mock import patch, MagicMock
from zabbix_automator.web import ZabbixWeb

class TestZabbixWeb(unittest.TestCase):
    def setUp(self):
        self.zabbix_web = ZabbixWeb('http://test.example.com', 'test_user', 'test_pass')

    def test_login(self):
        with patch('requests.Session') as mock_session:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_session.return_value.post.return_value = mock_response
            
            result = self.zabbix_web.login()
            self.assertTrue(result)

    def test_failed_login(self):
        with patch('requests.Session') as mock_session:
            mock_response = MagicMock()
            mock_response.status_code = 401
            mock_session.return_value.post.return_value = mock_response
            
            result = self.zabbix_web.login()
            self.assertFalse(result)

    def test_get_hosts(self):
        with patch.object(ZabbixWeb, 'make_request') as mock_request:
            mock_request.return_value = {'result': [{'hostid': '1', 'host': 'test_host'}]}
            hosts = self.zabbix_web.get_hosts()
            self.assertEqual(len(hosts), 1)
            self.assertEqual(hosts[0]['host'], 'test_host')

    def test_logout(self):
        with patch('requests.Session') as mock_session:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_session.return_value.get.return_value = mock_response
            
            result = self.zabbix_web.logout()
            self.assertTrue(result)

    def test_get_problems(self):
        with patch.object(ZabbixWeb, 'make_request') as mock_request:
            mock_data = {'result': [{'problemid': '1', 'name': 'High CPU usage'}]}
            mock_request.return_value = mock_data
            problems = self.zabbix_web.get_problems()
            self.assertEqual(len(problems), 1)
            self.assertEqual(problems[0]['name'], 'High CPU usage')

    def test_connection_timeout(self):
        with patch('requests.Session') as mock_session:
            mock_session.return_value.post.side_effect = TimeoutError()
            with self.assertRaises(ConnectionError):
                self.zabbix_web.login()

    def test_invalid_response(self):
        with patch.object(ZabbixWeb, 'make_request') as mock_request:
            mock_request.return_value = None
            hosts = self.zabbix_web.get_hosts()
            self.assertEqual(hosts, [])

if __name__ == '__main__':
    unittest.main()
