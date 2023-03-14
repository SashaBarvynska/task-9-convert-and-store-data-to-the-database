import os

from src.app import app

app.json.sort_keys = False


class Config:
    FOLDER_FILES = os.environ.get('FOLDER_FILES', 'data_files')
    DATA_BASE = os.environ.get('DATA_BASE', 'bd')
    DEBUG = os.environ.get('debug', True)


class TestConfig(Config):
    TESTING = os.environ.get('TESTING', True)
