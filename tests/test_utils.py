import unittest
from unittest.mock import patch, MagicMock
from zabbix_automator.utils import format_time, validate_response, parse_severity

class TestUtils(unittest.TestCase):
    def test_format_time(self):
        timestamp = 1634567890
        formatted = format_time(timestamp)
        self.assertIsInstance(formatted, str)
        self.assertTrue(len(formatted) > 0)

    def test_validate_response(self):
        valid_response = {'result': ['data']}
        invalid_response = {'error': {'code': 123, 'message': 'Error'}}
        
        self.assertTrue(validate_response(valid_response))
        with self.assertRaises(ValueError):
            validate_response(invalid_response)

    def test_parse_severity(self):
        self.assertEqual(parse_severity('disaster'), 5)
        self.assertEqual(parse_severity('high'), 4)
        self.assertEqual(parse_severity('warning'), 2)
        with self.assertRaises(ValueError):
            parse_severity('invalid')

if __name__ == '__main__':
    unittest.main()
