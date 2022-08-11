import os
from environs import Env


def env_reader() -> Env:
    env = Env()
    if os.path.exists("config/.env.local"):
        env.read_env("config/.env.local")
    else:
        env.read_env("config/.env.cloud")
    return env


env = env_reader()
