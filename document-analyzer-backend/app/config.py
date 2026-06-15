from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://docmind_user:docmind_pass@db:5432/docmind"
    secret_key: str = "change-this-secret"
    anthropic_api_key: str = ""
    azure_storage_connection_string: str = ""
    azure_storage_container: str = "documents"

    class Config:
        env_file = ".env"


settings = Settings()
