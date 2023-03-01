import os
from dotenv import load_dotenv

from src.core.ports.secondary.env_config_output_port import EnvConfigOutputPort


class EnvGateway(EnvConfigOutputPort):
    """Gateway to access environment variables."""
    def __init__(self) -> None:
        super().__init__()
        load_dotenv()

    def get(self, name: str) -> str:
        value = os.getenv(name)
        if value is None:
            raise Exception(f"Environment variable {name} is not set")