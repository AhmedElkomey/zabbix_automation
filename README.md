# Zabbix Automator

A powerful Python package that provides both a CLI and programmatic interface for automating Zabbix operations. Available on PyPI as `zabbix-automator`.

## Key Features

- **Host Operations**: Create, read, update, delete, and list hosts
- **Monitoring Management**: 
  - Items: Get and list monitoring items
  - Web Scenarios: Create, get, and list web monitoring
  - Triggers: Retrieve and list alert triggers
- **Organization**: 
  - Host Group management
  - Template management
- **Flexible Interface**: 
  - Command-line tool (`zabbix-cli`)
  - Python API for automation scripts
  - Comprehensive documentation and examples

## Quick Start

### Installation

```bash
# From PyPI
pip install zabbix-automator

# From source
git clone https://github.com/AhmedElkomey/zabbix_automation.git
cd zabbix_automation
pip install .
```

### Basic Usage

```bash
# CLI Examples
zabbix-cli host create --name webserver-01 --group-ids 2 --ip 192.168.1.100
zabbix-cli web create --hostid 10084 --name "HTTP Check" --url "https://example.com" --status-codes "200,301" --required "Welcome"

# Python API Example
from zabbix_automator.modules import hosts, web

# Create a host
new_host = hosts.create_host(
    name="db-server-01",
    group_ids=["2"],
    ip="192.168.1.101"
)

# Add web monitoring
web.create_web_scenario(
    hostid=new_host["hostids"][0],
    name="Database Health Check",
    url="http://localhost:8080/health",
    status_codes="200",
    required="healthy"
)
```

## Documentation

- [User Guide](docs/README.md): Detailed usage instructions and examples
- [API Reference](docs/api.md): Complete API documentation
- [Examples](examples/): Sample scripts for common use cases

## Configuration

Create a `config.yaml` file:

```yaml
zabbix_url: "https://zabbix.your-domain.com"
api_token: "your_api_token_here"
```

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Submit a Pull Request

## License

MIT License - See [LICENSE](LICENSE) file