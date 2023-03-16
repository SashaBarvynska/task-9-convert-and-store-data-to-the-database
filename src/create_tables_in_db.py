from src.db_connect import db
from src.models import DataBaseDrivers


def create_tables_in_db():
    db.create_tables([DataBaseDrivers])
