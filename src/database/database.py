from peewee import Model, PostgresqlDatabase
from dotenv import load_dotenv
from src.utils.environments import env
from pathlib import Path

import os

path_env = Path('.') / '.env'
load_dotenv(dotenv_path=path_env)


postgres = PostgresqlDatabase(
    env('DATABASE_NAME'),
    user=env('DATABASE_USER'),
    password=env('DATABASE_PASS'),
    host=env('DATABASE_HOST'),
    port=env('DATABASE_PORT')
)


class BaseModel(Model):
    class Meta:
        database = postgres
