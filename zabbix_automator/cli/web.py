import logging
from zabbix_automator.modules import web

def register_web_commands(subparsers):
    """Register 'web' sub-commands."""
    web_parser = subparsers.add_parser("web", help="Manage Zabbix web scenarios")
    web_subparsers = web_parser.add_subparsers(title="web_commands", dest="web_command")

    # web create
    create_parser = web_subparsers.add_parser("create", help="Create a web scenario")
    create_parser.add_argument("--hostid", required=True, help="Host ID")
    create_parser.add_argument("--name", required=True, help="Web scenario name")
    create_parser.add_argument("--url", required=True, help="Web scenario URL")
    create_parser.add_argument("--status-codes", required=True, help="Status codes")
    create_parser.add_argument("--required", required=True, help="Required text")
    create_parser.add_argument("--delay", type=int, default=60, help="Delay")
    create_parser.set_defaults(func=_handle_web_create)

    # web get
    get_parser = web_subparsers.add_parser("get", help="Get a web scenario")
    get_parser.add_argument("--hostid", required=True, help="Host ID")
    get_parser.add_argument("--name", required=True, help="Web scenario name")
    get_parser.set_defaults(func=_handle_web_get)

    # web list
    list_parser = web_subparsers.add_parser("list", help="List web scenarios")
    list_parser.add_argument("--hostid", required=True, help="Host ID")
    list_parser.set_defaults(func=_handle_web_list)

def _handle_web_create(args):
    try:
        result = web.create_web_scenario(
            hostid=args.hostid,
            name=args.name,
            url=args.url,
            status_codes=args.status_codes,
            required=args.required,
            delay=args.delay
        )
        logging.info(f"Web scenario created: {result}")
    except Exception as e:
        logging.error(f"Failed to create web scenario: {e}")

def _handle_web_get(args):
    try:
        data = web.get_web_scenario(args.hostid, args.name)
        logging.info(f"Web scenario data: {data}")
    except Exception as e:
        logging.error(f"Failed to get web scenario: {e}")

def _handle_web_list(args):
    try:
        data = web.list_web_scenarios(args.hostid)
        logging.info(f"Web scenario list: {data}")
    except Exception as e:
        logging.error(f"Failed to list web scenarios: {e}")
