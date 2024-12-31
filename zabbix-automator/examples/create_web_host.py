from zabbix_automation.modules import hosts, web

# Step 1: Create or fetch a host for the website
try:
    # Check if the host already exists
    host_name = "example-website"
    host = hosts.get_host(host_name)

    if not host:
        # If the host does not exist, create it
        new_host = hosts.create_host(
            name=host_name,
            group_ids=["2"],
            ip="127.0.0.1",
        )
        host_id = new_host["hostids"][0]
        print(f"Host '{host_name}' created with ID: {host_id}")
    else:
        host_id = host[0]["hostid"]
        print(f"Host '{host_name}' already exists with ID: {host_id}")
except Exception as e:
    print(f"Failed to create or fetch host: {e}")
    exit(1)

# Step 2: Configure a web scenario for website availability
try:
    web_scenario_name = "Website Availability Check"
    scenario = web.get_web_scenario(host_id, web_scenario_name)

    if not scenario:
        # Create the web scenario
        new_scenario = web.create_web_scenario(
            hostid=host_id,
            name=web_scenario_name,
            url="http://example.com",
            status_codes="200",
            required="Welcome",
        )
        scenario_id = new_scenario["httptestids"][0]
        print(f"Web scenario '{web_scenario_name}' created with ID: {scenario_id}")
    else:
        scenario_id = scenario[0]["httptestid"]
        print(f"Web scenario '{web_scenario_name}' already exists with ID: {scenario_id}")
except Exception as e:
    print(f"Failed to create or fetch web scenario: {e}")
    exit(1)