from setuptools import setup, find_packages

setup(
    name="zabbix-automator",
    version="0.1.2",
    description="Zabbix Automation CLI and Modules",
    author="Ahmed Elkomey",
    author_email="ahmedelkomey961@gmail.com",
    license="MIT",
    url="https://github.com/AhmedElkomey/zabbix_automation.git",
    keywords=["zabbix", "automation"],
    packages=find_packages(),  # Or find_packages(where="src") if using a src/ layout
    install_requires=[
        "zabbix-utils",
        "pyyaml",
    ],
    entry_points={
        "console_scripts": [
            "zabbix-cli=zabbix_automator.cli.main:main",
        ]
    },
)
