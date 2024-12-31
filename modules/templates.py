from zabbix_utils import ZabbixAPI

# Load configuration from config file
from zabbix_automation.config import load_config

config = load_config()
zabbix = ZabbixAPI(
    url=config.get("zabbix_url"),
    token=config.get("api_token"),
)


def get_template(name):
    try:
        template=zabbix.template.get(filter={"name": name},output=['templateid','name'])
        return template
    except Exception as e:
         raise Exception(f"Failed to get template: {e}")

def list_templates():
    try:
        templates = zabbix.template.get(output=['templateid','name'])
        return templates
    except Exception as e:
        raise Exception(f"Failed to list templates: {e}")
if __name__ == '__main__':
    try:
          template_name=input('Enter the name of the template: ')
          template=get_template(template_name)
          print("Template:",template)
          # fetch all templates
          templates=list_templates()
          print("All templates:",templates)
    except Exception as e:
       print(f"Error: {e}")