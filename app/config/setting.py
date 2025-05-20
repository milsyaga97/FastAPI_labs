from pydantic_settings import BaseSettings, SettingsConfigDict


class Setting(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_db: str

    @property
    def url(self):
        return f'postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}/{self.postgres_db}'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')

setting = Setting()