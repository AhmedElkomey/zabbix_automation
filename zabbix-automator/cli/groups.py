import logging
from modules import groups

def register_group_commands(subparsers):
    """Register 'group' sub-commands under the top-level CLI parser."""
    group_parser = subparsers.add_parser("group", help="Manage Zabbix host groups")
    group_subparsers = group_parser.add_subparsers(title="group_commands", dest="group_command")

    # group get
    get_parser = group_subparsers.add_parser("get", help="Get a group")
    get_parser.add_argument("--name", required=True, help="Group name")
    get_parser.set_defaults(func=_handle_group_get)

    # group list
    list_parser = group_subparsers.add_parser("list", help="List all groups")
    list_parser.set_defaults(func=_handle_group_list)

def _handle_group_get(args):
    try:
        data = groups.get_group(args.name)
        logging.info(f"Group data: {data}")
    except Exception as e:
        logging.error(f"Failed to get group: {e}")

def _handle_group_list(args):
    try:
        data = groups.list_groups()
        logging.info(f"Group list: {data}")
    except Exception as e:
        logging.error(f"Failed to list groups: {e}")
