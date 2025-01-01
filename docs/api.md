# Zabbix Automator API Reference

## Core Modules

### Host Management (`hosts`)

```python
from zabbix_automator.modules import hosts

# Available Functions
def create_host(name: str, group_ids: List[str], ip: str) -> Dict:
    """
    Create a new host in Zabbix.
    
    Args:
        name: Host name
        group_ids: List of group IDs to assign
        ip: Host IP address
    
    Returns:
        Dict containing created host details including hostid
    """

def get_host(name: str) -> List[Dict]:
    """
    Retrieve host information by name.
    
    Args:
        name: Host name to search for
    
    Returns:
        List of matching host objects
    """

def update_host(hostid: str, **kwargs) -> Dict:
    """
    Update host properties.
    
    Args:
        hostid: Host ID to update
        **kwargs: Properties to update (status, name, etc.)
    
    Returns:
        Dict containing update result
    """

def delete_host(hostid: str) -> Dict:
    """
    Delete a host.
    
    Args:
        hostid: Host ID to delete
    
    Returns:
        Dict containing deletion result
    """

def list_hosts(filters: Optional[Dict] = None) -> List[Dict]:
    """
    List hosts with optional filtering.
    
    Args:
        filters: Optional dict of filter criteria
    
    Returns:
        List of host objects
    """
```

### Item Management (`items`)

```python
from zabbix_automator.modules import items

def get_item(item_name: str, hostid: str) -> List[Dict]:
    """
    Get item details by name and host.
    
    Args:
        item_name: Item key name
        hostid: Host ID
    
    Returns:
        List of matching item objects
    """

def list_items(hostid: str, filters: Optional[Dict] = None) -> List[Dict]:
    """
    List items for a host with optional filtering.
    
    Args:
        hostid: Host ID
        filters: Optional dict of filter criteria
    
    Returns:
        List of item objects
    """
```

### Web Scenario Management (`web`)

```python
from zabbix_automator.modules import web

def create_web_scenario(
    hostid: str,
    name: str,
    url: str,
    status_codes: str,
    required: str,
    delay: int = 60
) -> Dict:
    """
    Create a web monitoring scenario.
    
    Args:
        hostid: Host ID
        name: Scenario name
        url: URL to monitor
        status_codes: Expected HTTP status codes
        required: Required response content
        delay: Check interval in seconds
    
    Returns:
        Dict containing created scenario details
    """

def get_web_scenario(hostid: str, name: str) -> List[Dict]:
    """
    Get web scenario details.
    
    Args:
        hostid: Host ID
        name: Scenario name
    
    Returns:
        List of matching scenario objects
    """

def list_web_scenarios(hostid: str) -> List[Dict]:
    """
    List all web scenarios for a host.
    
    Args:
        hostid: Host ID
    
    Returns:
        List of scenario objects
    """
```

### Additional Modules

#### Triggers (`triggers`)
```python
from zabbix_automator.modules import triggers

def get_trigger(hostid: str, description: str) -> List[Dict]
def list_triggers(hostid: str) -> List[Dict]
```

#### Host Groups (`groups`)
```python
from zabbix_automator.modules import groups

def get_group(name: str) -> List[Dict]
def list_groups() -> List[Dict]
```

#### Templates (`templates`)
```python
from zabbix_automator.modules import templates

def get_template(name: str) -> List[Dict]
def list_templates() -> List[Dict]
```

## Error Handling

All functions may raise:
- `ZabbixAPIException`: For API-related errors
- `ConfigurationError`: For configuration issues
- `ValidationError`: For invalid input parameters

Example error handling:
```python
from zabbix_automator.exceptions import ZabbixAPIException

try:
    host = hosts.create_host(name="test", group_ids=["2"], ip="192.168.1.1")
except ZabbixAPIException as e:
    print(f"API Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```