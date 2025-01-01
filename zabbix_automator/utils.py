import datetime

def format_time(timestamp):
    """
    Convert a UNIX timestamp to an ISO-8601 formatted string.
    """
    return datetime.datetime.utcfromtimestamp(timestamp).isoformat()

def validate_response(response):
    """
    Check if a Zabbix-like response contains an 'error' key;
    raise ValueError if so.
    """
    if 'error' in response:
        message = response['error'].get('message', 'Unknown error')
        raise ValueError(message)
    return True

def parse_severity(severity_str):
    """
    Convert a severity string to an integer.
    """
    mapping = {
        'not classified': 0,
        'information': 1,
        'warning': 2,
        'average': 3,
        'high': 4,
        'disaster': 5,
    }
    if severity_str not in mapping:
        raise ValueError(f"Invalid severity: {severity_str}")
    return mapping[severity_str]
