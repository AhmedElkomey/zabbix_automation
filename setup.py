from setuptools import setup, find_packages

setup(
    name="zabbix-automator",
    version="0.1.2",
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
    # author="Ahmed Elkomey",
    # author_email="ahmedelkomey961@gmail.com",
    # description="Zabbix Automation CLI and Modules",
    # license="MIT",
    # keywords="zabbix automation",
    # url="https://github.com/AhmedElkomey/zabbix_automation.git"
)
