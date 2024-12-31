import logging
from modules import templates

def register_template_commands(subparsers):
    """Register 'template' sub-commands."""
    template_parser = subparsers.add_parser("template", help="Manage Zabbix templates")
    template_subparsers = template_parser.add_subparsers(title="template_commands", dest="template_command")

    # template get
    get_parser = template_subparsers.add_parser("get", help="Get a template")
    get_parser.add_argument("--name", required=True, help="Template name")
    get_parser.set_defaults(func=_handle_template_get)

    # template list
    list_parser = template_subparsers.add_parser("list", help="List templates")
    list_parser.set_defaults(func=_handle_template_list)

def _handle_template_get(args):
    try:
        data = templates.get_template(args.name)
        logging.info(f"Template data: {data}")
    except Exception as e:
        logging.error(f"Failed to get template: {e}")

def _handle_template_list(args):
    try:
        data = templates.list_templates()
        logging.info(f"Template list: {data}")
    except Exception as e:
        logging.error(f"Failed to list templates: {e}")
