# API Documentation

This document provides the API documentation for the `zabbix_automation` package modules.

## Modules

### `hosts`

*   **`create_host(name, group_ids, ip)`**: Creates a new host.
    *   `name`: Host name (string)
    *   `group_ids`: List of group IDs (list of strings)
    *   `ip`: Host IP address (string)
    *   Returns: Dictionary containing the created host object

*   **`get_host(name)`**: Retrieves a host.
    *   `name`: Host name (string)
    *   Returns: Dictionary containing the host object

*    **`update_host(hostid, **kwargs)`**: Update the host.
    *   `hostid`: Host ID (string)
    *   `**kwargs`:  dictionary of update properties like 'status',...
    *   Returns: Dictionary containing the updated host object

*  **`delete_host(hostid)`**: Delete the host.
    *  `hostid`: Host ID (string)
    *   Returns: Dictionary containing the deleted host object

*   **`list_hosts(filters=None)`**: List hosts.
    *   `filters`: dictionary for filtering hosts  (optional)
    *   Returns: List of dictionaries containing host objects

### `items`

*   **`get_item(item_name,hostid)`**: Retrieves an item.
    *   `item_name`: Item key  (string)
    *  `hostid` : host ID (string)
    *   Returns: Dictionary containing the item object

*   **`list_items(hostid,filters=None)`**: List items.
    *    `hostid`: Host ID (string)
    *   `filters`: dictionary for filtering items  (optional)
    *   Returns: List of dictionaries containing items

### `web`

*   **`create_web_scenario(hostid, name, url, status_codes, required, delay=60)`**: Creates a web scenario.
    *   `hostid`: Host ID (string)
    *   `name`: Web scenario name (string)
    *   `url`: URL to check (string)
    *   `status_codes`: Expected status codes (string)
    *   `required`: Required content in response (string)
     *   `delay`: Delay between checks (integer)
    *   Returns: Dictionary containing the created web scenario object

*    **`get_web_scenario(hostid,name)`**: Retrieves a web scenario.
     *    `hostid`: Host ID (string)
     *  `name` : Web scenario name (string)
     *  Returns: Dictionary containing the web scenario object

*   **`list_web_scenarios(hostid)`**: List web scenarios for a given host.
    *    `hostid`: Host ID (string)
    *   Returns: List of dictionaries containing web scenarios

### `triggers`
*   **`get_trigger(hostid, description)`**: Retrieves a trigger.
      *  `hostid`: Host ID (string)
      *   `description` :  Trigger description (string)
      * Returns: Dictionary containing the trigger object

*   **`list_triggers(hostid)`**: List triggers for a given host.
       * `hostid`: Host ID (string)
       *  Returns: List of dictionaries containing triggers

### `groups`
*   **`get_group(name)`**: Retrieves a group.
      *   `name` : Group name (string)
      * Returns: Dictionary containing the group object

*    **`list_groups()`**: List groups.
    *   Returns: List of dictionaries containing groups

### `templates`
*   **`get_template(name)`**: Retrieves a template.
    *  `name` : template name (string)
    *   Returns: Dictionary containing the template object

*  **`list_templates()`**: List templates
    *   Returns: List of dictionaries containing templates
