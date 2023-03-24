
from peewee import CharField, Model

from .db_connect import db


class BaseModel(Model):
    """A base model that will use our Sqlite database."""

    class Meta:
        database = db


class DataBaseDrivers(BaseModel):
    abbreviation = CharField()
    driver = CharField()
    car = CharField()
    start_time = CharField()
    end_time = CharField()
    speed = CharField()


MODELS: list[Model] = [DataBaseDrivers]
