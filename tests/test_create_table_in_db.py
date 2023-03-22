from unittest.mock import patch

from src.create_tables_in_db import (create_tables, insert_data_in_db,
                                     list_drivers)
from src.models import DataBaseDrivers


@patch("src.create_tables_in_db.db.create_tables")
def test_create_tables_in_db(mock_create_tables):
    create_tables()
    mock_create_tables.assert_called_with([DataBaseDrivers])


@patch("src.create_tables_in_db.DataBaseDrivers.insert_many")
def test_insert_data_in_db(mock_insert_many):
    insert_data_in_db()
    mock_insert_many.assert_called_with(list_drivers)
