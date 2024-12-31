import logging
from modules import hosts  # The underlying logic from modules/hosts.py

def register_host_commands(subparsers):
    """Register 'host' sub-commands under the top-level CLI parser."""
    host_parser = subparsers.add_parser("host", help="Manage Zabbix hosts")
    host_subparsers = host_parser.add_subparsers(title="host_commands", dest="host_command")

    # host create
    create_parser = host_subparsers.add_parser("create", help="Create a new host")
    create_parser.add_argument("--name", required=True, help="Host name")
    create_parser.add_argument("--group-ids", required=True, nargs='+', help="Host group IDs")
    create_parser.add_argument("--ip", required=True, help="Host IP address")
    create_parser.set_defaults(func=_handle_host_create)

    # host get
    get_parser = host_subparsers.add_parser("get", help="Get a host")
    get_parser.add_argument("--name", required=True, help="Host name")
    get_parser.set_defaults(func=_handle_host_get)

    # host update
    update_parser = host_subparsers.add_parser("update", help="Update a host")
    update_parser.add_argument("--hostid", required=True, help="Host ID")
    update_parser.add_argument("--status", type=int, help="Host status")
    update_parser.set_defaults(func=_handle_host_update)

    # host delete
    delete_parser = host_subparsers.add_parser("delete", help="Delete a host")
    delete_parser.add_argument("--hostid", required=True, help="Host ID")
    delete_parser.set_defaults(func=_handle_host_delete)

    # host list
    list_parser = host_subparsers.add_parser("list", help="List all hosts")
    list_parser.add_argument("--filter", help="Filter in JSON (e.g. '{\"host\": \"myHost\"}')", default=None)
    list_parser.set_defaults(func=_handle_host_list)

def _handle_host_create(args):
    try:
        result = hosts.create_host(args.name, args.group_ids, args.ip)
        logging.info(f"Host created: {result}")
    except Exception as e:
        logging.error(f"Failed to create host: {e}")

def _handle_host_get(args):
    try:
        data = hosts.get_host(args.name)
        logging.info(f"Host data: {data}")
    except Exception as e:
        logging.error(f"Failed to get host: {e}")

def _handle_host_update(args):
    try:
        result = hosts.update_host(hostid=args.hostid, status=args.status)
        logging.info(f"Host updated: {result}")
    except Exception as e:
        logging.error(f"Failed to update host: {e}")

def _handle_host_delete(args):
    try:
        result = hosts.delete_host(args.hostid)
        logging.info(f"Host deleted: {result}")
    except Exception as e:
        logging.error(f"Failed to delete host: {e}")

def _handle_host_list(args):
    import json
    try:
        filters = json.loads(args.filter) if args.filter else None
        result = hosts.list_hosts(filters=filters)
        logging.info(f"Host list: {result}")
    except Exception as e:
        logging.error(f"Failed to list hosts: {e}")
