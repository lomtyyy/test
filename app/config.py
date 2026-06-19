from pydantic_settings import BaseSettings
from pydantic import ConfigDict, computed_field

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "postgres"
    DB_PASS: str = "postgres"
    DB_NAME: str = "postgres"

    model_config = ConfigDict(env_file=".env")

    @computed_field  # ← вместо model_validator
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

settings = Settings()

# Проверка (можно удалить)
print(settings.DB_HOST)
print(settings.DATABASE_URL)  # теперь работает как свойство