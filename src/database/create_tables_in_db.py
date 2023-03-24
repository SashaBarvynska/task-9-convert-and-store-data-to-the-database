from peewee import Model

from logging_config import logging

from .db_connect import db
from .fixtures import create_driver
from .models import MODELS

list_drivers = [x.__dict__ for x in create_driver(20)]


def create_tables() -> None:
    logging.info('created table in database.')
    db.create_tables(MODELS)


def insert_data_in_db(model: Model) -> None:
    logging.info('data added in database.')
    model.insert_many(list_drivers).execute()
