from dotenv import load_dotenv
from pathlib import Path

import os


path_env = Path('.') / '.env'
load_dotenv(dotenv_path=path_env)


def env(name: str) -> str or None:
    if name in os.environ:
        return os.environ[name]
    else:
        return None
