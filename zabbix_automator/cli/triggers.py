import logging
from zabbix_automator.modules import triggers

def register_trigger_commands(subparsers):
    """Register 'trigger' sub-commands."""
    trigger_parser = subparsers.add_parser("trigger", help="Manage Zabbix triggers")
    trigger_subparsers = trigger_parser.add_subparsers(title="trigger_commands", dest="trigger_command")

    # trigger get
    get_parser = trigger_subparsers.add_parser("get", help="Get a trigger")
    get_parser.add_argument("--hostid", required=True, help="Host ID")
    get_parser.add_argument("--description", required=True, help="Trigger description")
    get_parser.set_defaults(func=_handle_trigger_get)

    # trigger list
    list_parser = trigger_subparsers.add_parser("list", help="List all triggers")
    list_parser.add_argument("--hostid", required=True, help="Host ID")
    list_parser.set_defaults(func=_handle_trigger_list)

def _handle_trigger_get(args):
    try:
        data = triggers.get_trigger(args.hostid, args.description)
        logging.info(f"Trigger data: {data}")
    except Exception as e:
        logging.error(f"Failed to get trigger: {e}")

def _handle_trigger_list(args):
    try:
        data = triggers.list_triggers(args.hostid)
        logging.info(f"Trigger list: {data}")
    except Exception as e:
        logging.error(f"Failed to list triggers: {e}")
