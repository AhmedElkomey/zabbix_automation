from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automator.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)


def get_item(item_name,hostid):
    try:
        item = zabbix.item.get(
            filter={"hostid": hostid},
            search={"key_": item_name},
            output=["itemid", "name", "key_", "lastvalue"]
        )
        return item
    except Exception as e:
        raise Exception(f"Failed to get items for host {hostid}: {e}")

def list_items(hostid,filters=None):
    try:
        if filters:
            items = zabbix.item.get(
                filter={"hostid": hostid,**filters},
                 output=["itemid", "name", "key_", "lastvalue"]
            )
        else:
           items=zabbix.item.get(
                filter={"hostid": hostid},
                output=["itemid", "name", "key_", "lastvalue"]
           )
        return items
    except Exception as e:
        raise Exception(f"Failed to get items for host {hostid}: {e}")


if __name__ == '__main__':
        try:
        # Fetch item data
          host_id=input('Enter the host ID: ')
          item_name= input('Enter the Item Key: ')
          item_data = get_item(item_name,host_id)
          print("Item:",item_data)
          # Fetch all items
          items = list_items(hostid=host_id)
          print("All items for this host:",items)
          # Fetch filtered items
          items= list_items(hostid=host_id,filters={'name': 'CPU utilization'})
          print("Filtered Items:",items)
        except Exception as e:
              print(f"Error: {e}")