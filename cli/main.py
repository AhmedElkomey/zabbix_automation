import argparse
import logging
# Import each CLI module
from cli.hosts import register_host_commands
from cli.groups import register_group_commands
from cli.items import register_item_commands
from cli.triggers import register_trigger_commands
from cli.web import register_web_commands
from cli.templates import register_template_commands

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def main():
    parser = argparse.ArgumentParser(description="Zabbix Automation CLI")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Register each top-level command (host, group, item, etc.)
    register_host_commands(subparsers)
    register_group_commands(subparsers)
    register_item_commands(subparsers)
    register_trigger_commands(subparsers)
    register_web_commands(subparsers)
    register_template_commands(subparsers)

    args = parser.parse_args()

    if not args.command:
        # If no command was provided, print help
        parser.print_help()
        return

    # Execute the appropriate function if it exists:
    # We store the "handler" function on the parser in each register_*_commands call
    if hasattr(args, "func"):
        try:
            args.func(args)  # Call the function with the parsed arguments
        except Exception as e:
            logging.error(f"Error: {e}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
