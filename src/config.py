from typing import Any
import yaml

with open('config.yaml') as f:
    CONFIG: dict[str, Any] = yaml.safe_load(f)