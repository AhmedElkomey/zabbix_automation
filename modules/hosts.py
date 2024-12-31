from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automation.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)


def create_host(name, group_ids, ip):
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
            groups=[{"groupid": group_id} for group_id in group_ids]
        )
        return result
    except Exception as e:
         raise Exception(f"Failed to create host: {e}")

def get_host(name):
    try:
        host = zabbix.host.get(filter={"host": name})
        return host
    except Exception as e:
          raise Exception(f"Failed to get host: {e}")

def update_host(hostid, **kwargs):
     try:
        result = zabbix.host.update(hostid=hostid,**kwargs)
        return result
     except Exception as e:
         raise Exception(f"Failed to update host: {e}")

def delete_host(hostid):
   try:
        result = zabbix.host.delete(hostids=hostid)
        return result
   except Exception as e:
        raise Exception(f"Failed to delete host: {e}")
def list_hosts(filters=None):
    try:
        if filters:
            hosts = zabbix.host.get(filter=filters,output=["hostid", "host"])
        else:
             hosts = zabbix.host.get(output=["hostid", "host"])
        return hosts
    except Exception as e:
        raise Exception(f"Failed to list hosts: {e}")
if __name__ == '__main__':
    # Example usage
    try:
        # Create a new host
        new_host = create_host(name="test-host-cli-1",group_ids=["2"], ip="127.0.0.1")
        print(f"Host created: {new_host}")

        # Fetch the host
        host = get_host("test-host-cli-1")
        print(f"Host: {host}")
        host_id = host[0]['hostid']
        # update the host
        update_host_result=update_host(hostid=host_id,status=1)
        print(f"Host updated: {update_host_result}")
        # fetch all hosts
        hosts=list_hosts()
        print("All hosts:",hosts)
        # filter hosts
        hosts=list_hosts(filters={'host':'test-host-cli-1'})
        print("Filtered hosts:",hosts)

         # Delete the host
        delete_host(host_id)
        print(f"Host deleted")
    except Exception as e:
        print(f"Error: {e}")