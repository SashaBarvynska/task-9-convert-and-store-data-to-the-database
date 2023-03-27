from logging_config import logging
from src import MODELS, create_tables, insert_data_in_db

if __name__ == '__main__':

    logging.info('starting file execution...')
    create_tables()
    [
        insert_data_in_db(MODEL) if MODEL.__len__() == 0
        else logging.info(f'data already exist in table: {MODEL.__name__}.')
        for MODEL in MODELS
    ]
    logging.info('file execution is finished.')
