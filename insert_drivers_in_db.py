from logging_config import logging
from src.create_tables_in_db import create_tables, insert_data_in_db
from src.models import DataBaseDrivers

if __name__ == '__main__':
    logging.info('starting file execution...')
    create_tables()
    logging.info('created table in database.')
    if DataBaseDrivers.__len__() == 0:
        logging.info('data added in database.')
        insert_data_in_db()
    else:
        logging.info('data already exist in database.')
    logging.info('file execution is finished.')
