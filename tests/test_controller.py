from unittest.mock import patch

import pytest

from src import DriverAdaptor, get_drivers_from_db
from src.database.models import DataBaseDrivers
from tests.test_helpers import many_drivers_in_list, one_driver_in_list


@patch("src.controller.get_drivers_from_db", return_value=one_driver_in_list)
@pytest.mark.parametrize("key,value,result", [
    (
        "abbreviation",
        one_driver_in_list[0].abbreviation,
        one_driver_in_list[0]
    ),
    (
        "driver",
        one_driver_in_list[0].driver,
        one_driver_in_list[0]
    ),
    (
        "abbreviation",
        "Sebastidsffsdfdsfsfel",
        None
    ),
])
def test_get_driver(mock_get_drivers_from_db, key, value, result):
    instance = DriverAdaptor()
    mock_get_drivers_from_db.assert_called_once()
    assert instance.get_driver(key, value) == result


@patch("src.controller.get_drivers_from_db", return_value=many_drivers_in_list)
@pytest.mark.parametrize("order,result", [
    (
        True,
        sorted(many_drivers_in_list, key=lambda x: x.speed, reverse=True)
    ),
    (
        False,
        sorted(many_drivers_in_list, key=lambda x: x.speed, reverse=False)
    ),
])
def test_sort_data(mock_get_drivers_from_db, order, result):
    instance = DriverAdaptor()
    assert instance.sort_data(order) == result
    mock_get_drivers_from_db.assert_called_once()


def test_get_drivers_from_db():
    DataBaseDrivers.insert_many([x.__dict__ for x in many_drivers_in_list]).execute()
    assert get_drivers_from_db() == many_drivers_in_list
