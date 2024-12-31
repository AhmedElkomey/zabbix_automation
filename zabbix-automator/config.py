import yaml
import os

def load_config(config_path: str = None) -> dict:
    """
    Load configuration from a YAML file. 
    Defaults to `config.yaml` in the project root if no path is provided.

    :param config_path: path to the YAML configuration file (optional)
    :return: Dictionary containing configuration data
    """
    if config_path is None:
        current_dir = os.path.dirname(__file__)
        config_path = os.path.join(current_dir, "config.yaml")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r", encoding="utf-8") as file:
        config_data = yaml.safe_load(file)

    return config_data
