import yaml
from urllib.parse import urlparse

def load_config(path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)

    for entry in config:
        if "url" not in entry or "name" not in entry:
            raise ValueError("Each endpoint must have a 'name' and 'url' field")
    return config

def normalize_domain(url):
    parsed = urlparse(url)
    return parsed.hostname  # ignores port numbers
