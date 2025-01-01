import unittest
import pytest
from zabbix_automation.web import ZabbixWeb
from zabbix_automation.api import ZabbixAPI

@pytest.mark.integration
class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Skip these tests unless specifically running integration tests
        if not pytest.config.getoption("--run-integration"):
            pytest.skip("Integration tests not requested")

    def setUp(self):
        self.credentials = {
            'url': 'http://localhost/zabbix',
            'username': 'Admin',
            'password': 'zabbix'
        }
        self.web = ZabbixWeb(**self.credentials)
        self.api = ZabbixAPI(f"{self.credentials['url']}/api_jsonrpc.php", 
                            self.credentials['username'],
                            self.credentials['password'])

    def test_web_api_consistency(self):
        web_hosts = self.web.get_hosts()
        api_hosts = self.api.get_hosts()
        self.assertEqual(len(web_hosts), len(api_hosts))

    def test_problem_detection(self):
        problems = self.web.get_problems()
        triggers = self.api.get_triggers(only_true=True)
        self.assertGreaterEqual(len(problems), len(triggers))

if __name__ == '__main__':
    unittest.main()
