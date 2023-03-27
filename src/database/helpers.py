from peewee import Model

from logging_config import logging

from .connect import db
from .fixtures import create_driver
from .models import MODELS


def create_tables() -> None:
    db.create_tables(MODELS)
    logging.info('created table in database.')


def insert_data_in_db(model: Model) -> None:
    list_drivers = [x.__dict__ for x in create_driver(20)]
    logging.info('data added in database.')
    model.insert_many(list_drivers).execute()
