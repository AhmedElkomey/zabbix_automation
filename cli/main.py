import argparse
from cli import hosts, items, web, triggers,groups
def main():
  parser = argparse.ArgumentParser(description="Zabbix Automation CLI")
  subparsers = parser.add_subparsers(title="commands", dest="command")

  # Host commands
  host_parser = subparsers.add_parser("host", help="Manage Zabbix hosts")
  host_subparsers = host_parser.add_subparsers(title="host_commands", dest="host_command")

  # Host - Create
  host_create_parser = host_subparsers.add_parser("create", help="Create a new host")
  host_create_parser.add_argument("--name", required=True, help="Host name")
  host_create_parser.add_argument("--group-ids", required=True, nargs='+',help="Host group IDs")
  host_create_parser.add_argument("--ip", required=True, help="Host IP address")

  # Host - Get
  host_get_parser = host_subparsers.add_parser("get", help="Get a host")
  host_get_parser.add_argument("--name", required=True, help="Host name")
  # Host - update
  host_update_parser= host_subparsers.add_parser("update",help="update a host")
  host_update_parser.add_argument("--hostid", required=True, help="Host ID")
  host_update_parser.add_argument("--status", type=int, help="Host status")
  # Host - delete
  host_delete_parser = host_subparsers.add_parser("delete", help="Delete a host")
  host_delete_parser.add_argument("--hostid", required=True, help="Host ID")

  # Host - list
  host_list_parser = host_subparsers.add_parser("list", help="List all hosts")
  host_list_parser.add_argument("--filter",help="filter for hosts",default=None)

  # Item commands
  item_parser = subparsers.add_parser("item", help="Manage Zabbix items")
  item_subparsers = item_parser.add_subparsers(title="item_commands", dest="item_command")
  # Item - Get
  item_get_parser = item_subparsers.add_parser("get", help="Get an item")
  item_get_parser.add_argument("--hostid", required=True, help="Host ID")
  item_get_parser.add_argument("--item-name", required=True, help="Item key name")
  # Item - List
  item_list_parser = item_subparsers.add_parser("list",help="list all items")
  item_list_parser.add_argument("--hostid", required=True, help="Host ID")
  item_list_parser.add_argument("--filter",default=None,help="filter for items")


  # Web scenario commands
  web_parser = subparsers.add_parser("web", help="Manage Zabbix web scenarios")
  web_subparsers = web_parser.add_subparsers(title="web_commands", dest="web_command")
  # web - create
  web_create_parser=web_subparsers.add_parser("create",help="create a web scenario")
  web_create_parser.add_argument("--hostid", required=True, help="Host ID")
  web_create_parser.add_argument("--name", required=True, help="Web scenario name")
  web_create_parser.add_argument("--url", required=True, help="Web scenario URL")
  web_create_parser.add_argument("--status-codes", required=True, help="Web scenario status codes")
  web_create_parser.add_argument("--required", required=True, help="Web scenario required text")
  web_create_parser.add_argument("--delay", type=int, default=60,help="Web scenario delay")
  #web - get
  web_get_parser = web_subparsers.add_parser("get", help="Get a web scenario")
  web_get_parser.add_argument("--hostid", required=True, help="Host ID")
  web_get_parser.add_argument("--name", required=True, help="Web scenario name")
  #web - list
  web_list_parser = web_subparsers.add_parser("list",help="list all web scenarios")
  web_list_parser.add_argument("--hostid", required=True, help="Host ID")

   # Trigger commands
  trigger_parser = subparsers.add_parser("trigger", help="Manage Zabbix triggers")
  trigger_subparsers = trigger_parser.add_subparsers(title="trigger_commands", dest="trigger_command")
   # trigger - get
  trigger_get_parser = trigger_subparsers.add_parser("get", help="Get a trigger")
  trigger_get_parser.add_argument("--hostid", required=True, help="Host ID")
  trigger_get_parser.add_argument("--description", required=True, help="Trigger description")
   # trigger - list
  trigger_list_parser = trigger_subparsers.add_parser("list",help="list all triggers")
  trigger_list_parser.add_argument("--hostid", required=True, help="Host ID")

  # group commands
  group_parser = subparsers.add_parser("group", help="Manage Zabbix host groups")
  group_subparsers = group_parser.add_subparsers(title="group_commands", dest="group_command")
   # group - get
  group_get_parser = group_subparsers.add_parser("get", help="Get a group")
  group_get_parser.add_argument("--name", required=True, help="Group name")
   # group - list
  group_list_parser = group_subparsers.add_parser("list",help="list all groups")

  # template commands
  template_parser = subparsers.add_parser("template", help="Manage Zabbix templates")
  template_subparsers = template_parser.add_subparsers(title="template_commands", dest="template_command")
  # template - get
  template_get_parser = template_subparsers.add_parser("get", help="Get a template")
  template_get_parser.add_argument("--name", required=True, help="Template name")
    # template - list
  template_list_parser = template_subparsers.add_parser("list",help="list all templates")

  args = parser.parse_args()

  if args.command == "host":
     if args.host_command == "create":
        try:
            result = hosts.create_host(args.name, args.group_ids, args.ip)
            print(f"Host created: {result}")
        except Exception as e:
            print(f"Error: {e}")
     elif args.host_command == "get":
          try:
            host = hosts.get_host(args.name)
            print(f"Host: {host}")
          except Exception as e:
              print(f"Error: {e}")
     elif args.host_command == "update":
           try:
               result= hosts.update_host(hostid=args.hostid,status=args.status)
               print(f"Host updated: {result}")
           except Exception as e:
                print(f"Error: {e}")
     elif args.host_command == "delete":
        try:
          result=hosts.delete_host(args.hostid)
          print(f"Host deleted: {result}")
        except Exception as e:
            print(f"Error: {e}")
     elif args.host_command == "list":
        try:
            hosts_list = hosts.list_hosts(filters=eval(args.filter) if args.filter else None)
            print(f"List of Hosts: {hosts_list}")
        except Exception as e:
             print(f"Error: {e}")

  elif args.command == "item":
      if args.item_command == "get":
        try:
            item_data = items.get_item(args.item_name,args.hostid)
            print(f"Item: {item_data}")
        except Exception as e:
             print(f"Error: {e}")
      elif args.item_command == "list":
        try:
             items_list = items.list_items(hostid=args.hostid,filters=eval(args.filter) if args.filter else None)
             print(f"List of Items: {items_list}")
        except Exception as e:
             print(f"Error: {e}")
  elif args.command == "web":
       if args.web_command == "create":
           try:
             result = web.create_web_scenario(
                hostid=args.hostid,
                name=args.name,
                url=args.url,
                status_codes=args.status_codes,
                required=args.required,
                delay=args.delay
             )
             print(f"Web scenario created: {result}")
           except Exception as e:
                print(f"Error: {e}")
       elif args.web_command == "get":
           try:
              web_scenario = web.get_web_scenario(hostid=args.hostid, name=args.name)
              print(f"Web Scenario: {web_scenario}")
           except Exception as e:
               print(f"Error: {e}")
       elif args.web_command == "list":
            try:
                web_scenarios = web.list_web_scenarios(hostid=args.hostid)
                print(f"List of Web Scenarios: {web_scenarios}")
            except Exception as e:
                print(f"Error: {e}")
  elif args.command =="trigger":
     if args.trigger_command == "get":
        try:
            trigger_data = triggers.get_trigger(hostid=args.hostid,description=args.description)
            print(f"Trigger: {trigger_data}")
        except Exception as e:
             print(f"Error: {e}")
     elif args.trigger_command == "list":
       try:
            trigger_list = triggers.list_triggers(hostid=args.hostid)
            print(f"List of Triggers: {trigger_list}")
       except Exception as e:
            print(f"Error: {e}")

  elif args.command == "group":
      if args.group_command == "get":
         try:
              group_data = groups.get_group(name=args.name)
              print(f"Group: {group_data}")
         except Exception as e:
              print(f"Error: {e}")
      elif args.group_command == "list":
         try:
            group_list = groups.list_groups()
            print(f"List of Groups: {group_list}")
         except Exception as e:
              print(f"Error: {e}")
  elif args.command =="template":
      if args.template_command == "get":
         try:
             template_data = templates.get_template(name=args.name)
             print(f"Template: {template_data}")
         except Exception as e:
             print(f"Error: {e}")
      elif args.template_command == "list":
        try:
             template_list = templates.list_templates()
             print(f"List of Templates: {template_list}")
        except Exception as e:
             print(f"Error: {e}")

if __name__ == "__main__":
    main()