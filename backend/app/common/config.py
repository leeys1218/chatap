from dataclasses import dataclass, asdict
from os import path, environ

# app 패키지를 가리키는 path
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


@dataclass
class Config:
    """
    기본 Configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True
    DB_URL: str = "mysql+pymysql://root:1234@localhost:3306/chatap"


@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False
    user = "fastapi"
    pwd = "fastapi123"
    host = "chataprds.cz0kxq7yhsfp.ap-northeast-2.rds.amazonaws.com"
    port = "3306"
    DB_URL: str = f'mysql+pymysql://{user}:{pwd}@{host}:{port}/chatpapdb'


def conf():
    """
    환경 불러오기
    """
    config = dict(prod=ProdConfig(), local=LocalConfig())
    return config.get(environ.get("API_ENV", "local"))

