from pydantic import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_name: str
    db_port: str
    db_user: str
    db_user_password: str
    secret_key: str
    hashing_algorithm: str
    access_token_expire_days: int

    class Config:
        env_file = '.env'

settings = Settings()
