import os
from config.default_config import CONFIG as DEFAULT_CONFIG

def load_config():
    if os.path.exists("config_local.py"):
        from config_local import CONFIG as LOCAL_CONFIG
        return {**DEFAULT_CONFIG, **LOCAL_CONFIG}
    return DEFAULT_CONFIG
