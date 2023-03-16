import json
import os


class Config:
    FOLDER_FILES = os.environ.get('FOLDER_FILES', 'data_files')
    DATABASE = os.environ.get('DATABASE', 'bd')
    DEBUG = os.environ.get('debug', True)
    SORT_KEY = json.sort_keys = False


class TestConfig(Config):
    TESTING = os.environ.get('TESTING', True)
