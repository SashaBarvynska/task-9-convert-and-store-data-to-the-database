import pytest

from config import TestConfig
from main import app as flask_app


@pytest.fixture(scope="module")
def app():
    flask_app.config.from_object(TestConfig)
    yield flask_app


@pytest.fixture(scope="module")
def client(app):
    yield app.test_client()
