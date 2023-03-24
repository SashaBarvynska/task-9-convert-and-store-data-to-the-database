from unittest.mock import patch

import pytest

from src import DriverAdaptor, create_driver, get_drivers_from_db
from tests.conftest import drivers_list_6

drivers_list_3 = create_driver(1)
driver = drivers_list_3[0]

drivers_list_4 = create_driver(3)
drivers_list_5 = create_driver(2)
list_drivers_files = [x.__dict__ for x in drivers_list_5]

DICT_ABB = {x.abbreviation: {"driver": x.driver, "car": x.car} for x in drivers_list_5}
DICT_TIME = {x.abbreviation: x.start_time for x in drivers_list_5}


@patch("src.controller.get_drivers_from_db", return_value=drivers_list_3)
@pytest.mark.parametrize("key,value,result", [
    (
        "abbreviation",
        driver.abbreviation,
        driver
    ),
    (
        "driver",
        driver.driver,
        driver
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


@patch("src.controller.get_drivers_from_db", return_value=drivers_list_4)
@pytest.mark.parametrize("order,result", [
    (
        True,
        sorted(drivers_list_4, key=lambda x: x.speed, reverse=True)
    ),
    (
        False,
        sorted(drivers_list_4, key=lambda x: x.speed, reverse=False)
    ),
])
def test_sort_data(mock_get_drivers_from_db, order, result):
    instance = DriverAdaptor()
    assert instance.sort_data(order) == result
    mock_get_drivers_from_db.assert_called_once()


def test_get_drivers_from_db():
    assert get_drivers_from_db() == drivers_list_6
