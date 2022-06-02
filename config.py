from dataclasses import dataclass
from environs import Env
from pathlib import Path

@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass()
class Directory:
    ROOT_DIR: Path = None
    HOME_DIR: Path = None

@dataclass
class Config:
    db: DbConfig
    misc: Miscellaneous
    dir: Directory



def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        db=DbConfig(
            host=env.str('DB_HOST'),
            password=env.str('DB_PASS'),
            user=env.str('DB_USER'),
            database=env.str('DB_NAME')
        ),
        misc=Miscellaneous(),
        dir=Directory(
            ROOT_DIR=Path.cwd(),
            HOME_DIR=Path.home()
        )
    )
