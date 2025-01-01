import logging
from typing import Any, Dict, List
from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automator.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)

def create_host(name: str, group_ids: List[str], ip: str) -> Dict[str, Any]:
    """
    Create a new Zabbix host.
    :param name: Host name
    :param group_ids: List of group IDs
    :param ip: IP address for the host
    :return: API response dict
    """
    try:
        result = zabbix.host.create(
            host=name,
            interfaces=[
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": ip,
                    "dns": "",
                    "port": "10050",
                }
            ],
            groups=[{"groupid": gid} for gid in group_ids]
        )
        return result
    except Exception as e:
        logging.error(f"Failed to create host: {e}")
        raise

def get_host(name: str) -> List[Dict[str, Any]]:
    """
    Retrieve a host by name.
    :param name: Host name
    :return: List of host dict objects
    """
    try:
        host = zabbix.host.get(filter={"host": name})
        return host
    except Exception as e:
        logging.error(f"Failed to get host: {e}")
        raise

def update_host(hostid: str, **kwargs) -> Dict[str, Any]:
    """
    Update a host.
    :param hostid: Host ID
    :param kwargs: Additional parameters to pass to the API
    :return: API response dict
    """
    try:
        result = zabbix.host.update(hostid=hostid, **kwargs)
        return result
    except Exception as e:
        logging.error(f"Failed to update host: {e}")
        raise

def delete_host(hostid: str) -> Dict[str, Any]:
    """
    Delete a host.
    :param hostid: Host ID
    :return: API response dict
    """
    try:
        result = zabbix.host.delete(hostids=hostid)
        return result
    except Exception as e:
        logging.error(f"Failed to delete host: {e}")
        raise

def list_hosts(filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    List all hosts with optional filters.
    :param filters: Dict of Zabbix filter options
    :return: List of host dict objects
    """
    try:
        if filters:
            hosts = zabbix.host.get(filter=filters, output=["hostid", "host"])
        else:
            hosts = zabbix.host.get(output=["hostid", "host"])
        return hosts
    except Exception as e:
        logging.error(f"Failed to list hosts: {e}")
        raise
