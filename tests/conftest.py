import pytest
from peewee import SqliteDatabase

from config import TestConfig
from main import app as flask_app
from src import DataBaseDrivers


@pytest.fixture(scope="module")
def app():
    flask_app.config.from_object(TestConfig)
    yield flask_app


@pytest.fixture(scope="module")
def client(app):
    yield app.test_client()


@pytest.fixture(autouse=True)
def test_db():
    test_db = SqliteDatabase(':memory:')
    test_db.bind([DataBaseDrivers], bind_refs=False, bind_backrefs=False)
    test_db.connect()
    test_db.create_tables([DataBaseDrivers])
    yield test_db
    test_db.drop_tables([DataBaseDrivers])
    test_db.close()
