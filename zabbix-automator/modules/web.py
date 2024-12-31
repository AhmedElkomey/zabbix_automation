from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automator.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)


def create_web_scenario(hostid, name, url, status_codes, required, delay=60):
    try:
         scenario= zabbix.httptest.create(
            name=name,
            hostid=hostid,
            steps=[
                {
                    "name": "Check URL",
                    "no": 1,
                    "url": url,
                    "status_codes": status_codes,
                    "required": required,
                    "timeout": 5,
                }
            ],
            retries=1,
            delay=delay,
        )
         return scenario
    except Exception as e:
         raise Exception(f"Failed to create web scenario: {e}")


def get_web_scenario(hostid,name):
    try:
        scenario = zabbix.httptest.get(filter={"name": name, "hostid": hostid})
        return scenario
    except Exception as e:
        raise Exception(f"Failed to get web scenario: {e}")

def list_web_scenarios(hostid):
     try:
        scenarios = zabbix.httptest.get(filter={"hostid": hostid},output=['httptestid','name'])
        return scenarios
     except Exception as e:
          raise Exception(f"Failed to list web scenarios: {e}")

if __name__ == '__main__':
      try:
          # Example usage
          host_id = input('Enter the host ID: ')
          new_web_scenario=create_web_scenario(
             hostid=host_id,
             name="Test Web Scenario",
             url="http://example.com",
             status_codes="200",
             required="Welcome",
             delay=60
         )
          print(f"Web scenario created: {new_web_scenario}")
           # fetch a web scenario
          web_scenario=get_web_scenario(hostid=host_id,name="Test Web Scenario")
          print(f"Web Scenario {web_scenario}")
          # fetch all web scenarios
          scenarios=list_web_scenarios(hostid=host_id)
          print("All web scenarios:", scenarios)
      except Exception as e:
          print(f"Error: {e}")