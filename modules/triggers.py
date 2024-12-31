from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automation.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)


def get_trigger(hostid, description):
  try:
      trigger=zabbix.trigger.get(
        filter={"hostid": hostid, "description":description},
        output=["triggerid", "description"]
        )
      return trigger
  except Exception as e:
        raise Exception(f"Failed to get trigger: {e}")

def list_triggers(hostid):
    try:
        triggers = zabbix.trigger.get(
           filter={"hostid": hostid},
           output=["triggerid", "description"]
        )
        return triggers
    except Exception as e:
        raise Exception(f"Failed to list triggers: {e}")
if __name__ == '__main__':
      try:
            host_id = input('Enter the host ID: ')
            trigger_description=input('Enter the description for the trigger: ')
            trigger = get_trigger(hostid=host_id,description=trigger_description)
            print("Trigger:", trigger)
            # fetch all triggers
            triggers=list_triggers(hostid=host_id)
            print("All Triggers:",triggers)
      except Exception as e:
         print(f"Error: {e}")