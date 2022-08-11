import databases
from config.config import env

def get_database_url()->str:
    return env("DATABASE_URL")

database_url = get_database_url()
database = databases.Database(database_url)