from src.controller import create_driver
from src.db_connect import db
from src.models import DataBaseDrivers

list_drivers = [x.__dict__ for x in create_driver(20)]


def create_tables() -> None:
    db.create_tables([DataBaseDrivers])


def insert_data_in_db() -> None:
    DataBaseDrivers.insert_many(list_drivers).execute()
