import os

from src.app import app

app.json.sort_keys = False


class Config:
    FOLDER_FILES = os.environ.get('FOLDER_FILES', 'data_files')
    debug = os.environ.get('debug', True)


class TestConfig(Config):
    TESTING = os.environ.get('TESTING', True)
