from peewee import CharField, Model

from src.db_connect import db


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class DB_drivers(BaseModel):
    abbreviation = CharField()
    driver = CharField()
    car = CharField()
    start_time = CharField()
    end_time = CharField()
    speed = CharField()
