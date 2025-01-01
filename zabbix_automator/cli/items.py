import logging
import json
from zabbix_automator.modules import items

def register_item_commands(subparsers):
    """Register 'item' sub-commands."""
    item_parser = subparsers.add_parser("item", help="Manage Zabbix items")
    item_subparsers = item_parser.add_subparsers(title="item_commands", dest="item_command")

    # item get
    get_parser = item_subparsers.add_parser("get", help="Get an item")
    get_parser.add_argument("--hostid", required=True, help="Host ID")
    get_parser.add_argument("--item-name", required=True, help="Item key name")
    get_parser.set_defaults(func=_handle_item_get)

    # item list
    list_parser = item_subparsers.add_parser("list", help="List all items")
    list_parser.add_argument("--hostid", required=True, help="Host ID")
    list_parser.add_argument("--filter", default=None, help="Filter in JSON format")
    list_parser.set_defaults(func=_handle_item_list)

def _handle_item_get(args):
    try:
        data = items.get_item(args.item_name, args.hostid)
        logging.info(f"Item data: {data}")
    except Exception as e:
        logging.error(f"Failed to get item: {e}")

def _handle_item_list(args):
    try:
        filters = json.loads(args.filter) if args.filter else None
        data = items.list_items(hostid=args.hostid, filters=filters)
        logging.info(f"Item list: {data}")
    except Exception as e:
        logging.error(f"Failed to list items: {e}")
