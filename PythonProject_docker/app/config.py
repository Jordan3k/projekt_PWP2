
from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Config:
    """Application configuration loaded from environment variables."""


    database_uri: str
    secret_key: str


    @staticmethod
    def from_env() -> "Config":
        db_uri = os.getenv(
        "DATABASE_URL",
        # Sensible default for local dev via docker-compose
        "postgresql+psycopg://postgres:postgres@localhost:5432/calculator",
        )
        secret = os.getenv("SECRET_KEY", "dev-secret-change-me")
        return Config(database_uri=db_uri, secret_key=secret)