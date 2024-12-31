from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automation.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)

# Test the connection and fetch the API version
try:
    api_version = zabbix.apiinfo.version()
    print(f"Connected to Zabbix API. Version: {api_version}")
except Exception as e:
    print(f"Failed to connect to Zabbix API: {e}")
    exit(1)

# Example: Fetch all hosts
try:
    hosts = zabbix.host.get(output=["hostid", "host"])
    print("Hosts:")
    for host in hosts:
        print(f"Host ID: {host['hostid']}, Hostname: {host['host']}")
except Exception as e:
    print(f"Failed to fetch hosts: {e}")