from unittest.mock import patch

from src import MODELS, DataBaseDrivers, create_tables, insert_data_in_db


@patch("src.db.create_tables")
def test_create_tables_in_db(mock_create_tables):
    create_tables()
    mock_create_tables.assert_called_with(MODELS)


@patch("src.DataBaseDrivers.insert_many")
def test_insert_data_in_db(mock_insert_many):
    insert_data_in_db(DataBaseDrivers)
    mock_insert_many.assert_called_once()
