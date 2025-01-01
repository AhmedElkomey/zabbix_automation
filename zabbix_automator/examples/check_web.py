# Description: This script fetches monitoring data for a web scenario.

from zabbix_automator.modules import items

host_id = input('Enter the host ID: ')
web_scenario_name = input('Enter the web scenario name: ')
# Check web scenario data
try:
   web_data = items.get_item(f"web.test[{web_scenario_name}]",host_id)
   print(f"Monitoring data for web scenario '{web_scenario_name}':")
   for item in web_data:
     print(
        f"Item: {item['name']}, Key: {item['key_']}, Last Value: {item['lastvalue']}"
    )
except Exception as e:
    print(f"Failed to fetch web scenario data: {e}")