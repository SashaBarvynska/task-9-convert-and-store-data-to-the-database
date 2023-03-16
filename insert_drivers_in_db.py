
import logging

from src.create_tables_in_db import create_tables_in_db
from src.models import DataBaseDrivers
from tests.test_helpers import create_driver

logging.basicConfig(level=logging.INFO)
if __name__ == '__main__':
    logging.info('starting file execution...')
    create_tables_in_db()
    logging.info('created table in database.')
    if DataBaseDrivers.__len__() == 0:
        logging.info('data added in database.')
        DataBaseDrivers.insert_many([x.__dict__ for x in create_driver(20)]).execute()
    else:
        logging.info('data already exist in database.')
    logging.info('file execution is finished.')
