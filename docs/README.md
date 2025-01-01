# Zabbix Automator Documentation

## Overview

Zabbix Automator streamlines Zabbix management through a Python package that offers both CLI and programmatic interfaces. Built on top of the `zabbix-utils` library, it simplifies common Zabbix operations.

## Getting Started

### Installation

```bash
# PyPI installation
pip install zabbix-automator

# Source installation
git clone https://github.com/AhmedElkomey/zabbix_automation.git
cd zabbix_automation
pip install .
```

### Configuration

1. Create a `config.yaml` file:
```yaml
zabbix_url: "https://zabbix.your-domain.com"
api_token: "your_api_token_here"
```

2. Load configuration in your Python code:
```python
from zabbix_automator.config import load_config

# Use default config location
config = load_config()

# Or specify custom path
config = load_config("/path/to/custom_config.yaml")
```

## Usage Guide

### Command Line Interface

The `zabbix-cli` command provides access to all functionality:

```bash
# Host Management
zabbix-cli host create --name "web-01" --group-ids 2 --ip "192.168.1.100"
zabbix-cli host list
zabbix-cli host get --name "web-01"
zabbix-cli host update --hostid 10084 --status enabled

# Web Monitoring
zabbix-cli web create \
    --hostid 10084 \
    --name "HTTP Check" \
    --url "https://example.com" \
    --status-codes "200" \
    --required "Welcome"
zabbix-cli web list --hostid 10084

# Get CLI help
zabbix-cli --help
zabbix-cli <command> --help
```

### Python API

Example automation scripts:

```python
from zabbix_automator.modules import hosts, items, web

# Create a host
host = hosts.create_host(
    name="app-server-01",
    group_ids=["2"],
    ip="192.168.1.102"
)

# Check host items
items_list = items.list_items(
    hostid=host["hostids"][0],
    filters={"type": "0"}  # Zabbix agent items
)

# Add web monitoring
scenario = web.create_web_scenario(
    hostid=host["hostids"][0],
    name="API Health Check",
    url="http://localhost:8080/api/health",
    status_codes="200",
    required="status: UP",
    delay=30
)
```

## Best Practices

1. **Error Handling**: Always wrap API calls in try-except blocks
2. **Configuration Management**: Use environment variables or secure vaults for sensitive data
3. **Automation Scripts**: Create reusable functions for common operations
4. **Testing**: Verify operations in a test environment first

## Troubleshooting

Common issues and solutions:

1. **Authentication Failures**
   - Verify API token validity
   - Check Zabbix URL accessibility
   - Ensure proper permissions for the API user

2. **Operation Failures**
   - Confirm host/group IDs exist
   - Check for required permissions
   - Verify input parameter formats

## Additional Resources

- [API Reference](api.md)
- [Example Scripts](../examples/)
- [Zabbix API Documentation](https://www.zabbix.com/documentation/current/manual/api)