from setuptools import setup, find_packages

setup(
    name="zabbix-automation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "zabbix-utils",
        "pyyaml"
    ],
    entry_points={
        "console_scripts": [
            "zabbix-cli=cli.main:main",
        ]
    },
    # Optional metadata:
    # author="Your Name",
    # author_email="your.email@example.com",
    # description="Zabbix Automation CLI and Modules",
    # license="MIT",
    # keywords="zabbix automation",
    # url="https://github.com/yourusername/zabbix-automation"
)
