from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "outcome-first-controller"
    environment: str = "development"
    database_url: str = "sqlite+aiosqlite:///./data/controller.db"
    simulator_url: str = ""
    log_level: str = "INFO"


settings = Settings()
