from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automator.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)


def get_group(name):
    try:
        group=zabbix.hostgroup.get(filter={"name": name},output=['groupid','name'])
        return group
    except Exception as e:
        raise Exception(f"Failed to get group: {e}")


def list_groups():
     try:
        groups = zabbix.hostgroup.get(output=['groupid','name'])
        return groups
     except Exception as e:
        raise Exception(f"Failed to list groups: {e}")
if __name__ == '__main__':
    try:
          group_name=input('Enter the name of the group: ')
          group=get_group(group_name)
          print("Group:",group)
          # fetch all groups
          groups=list_groups()
          print("All Groups:",groups)
    except Exception as e:
       print(f"Error: {e}")