# Zabbix Automation Package

This Python package provides a command-line interface (CLI) and a set of modules for automating tasks in Zabbix. It leverages the `zabbix-utils` library for API communication.

## Installation

```bash
pip install -e .
```

or

```bash
pip install zabbix-automation
```
## Configuration
create a config.yaml in your root project directory and add your configuration like that:
```yaml
zabbix_url: 'your_zabbix_url'
api_token: 'your_api_token'
```

## Usage

### CLI

```bash
zabbix-cli <command> [options]
```

**Example:**

```bash
zabbix-cli host create --name test-host --group-ids 2 --ip 127.0.0.1
zabbix-cli host get --name test-host
zabbix-cli item get --hostid 10277 --item-name "agent.ping"
zabbix-cli item list --hostid 10277
zabbix-cli web create --hostid 10277 --name "Test Web Scenario" --url "http://example.com" --status-codes "200" --required "Welcome"
zabbix-cli web list --hostid 10277
zabbix-cli trigger get --hostid 10277 --description "CPU utilization is too high"
zabbix-cli trigger list --hostid 10277
zabbix-cli group get --name "Zabbix servers"
zabbix-cli group list
zabbix-cli template get --name "Template App HTTP Service"
zabbix-cli template list
```
You can use `--help` with each command to get a list of the options
 ```bash
 zabbix-cli host --help
 ```
### Modules

You can also use the modules directly in your python scripts to automate zabbix.

**Example:**

```python
from zabbix_automation.modules import hosts, items

try:
  # Create a host
   new_host = hosts.create_host(name="test-host-module", group_ids=["2"], ip="127.0.0.1")
   print(f"Host created: {new_host}")
   # fetch the item data for host
   item_data = items.get_item(item_name="agent.ping", hostid="10277")
   print(f"Item data: {item_data}")
except Exception as e:
    print(f"Error: {e}")


```

## Features

*   Host Management (create, get, update, delete, list)
*   Item Management (get, list)
*   Web Scenario Management (create, get, list)
*   Trigger Management (get, list)
*    Host Group Management (get, list)
*    Template Management (get, list)
*   CLI for easy automation.
*   Unit tests
*   Examples

## Future Enhancements

*   Advanced Zabbix object management
*   Rate limiting for API calls
*   More output formats
*   Configuration from ENV
*   Support for more Zabbix objects
*   Integration with other tools

