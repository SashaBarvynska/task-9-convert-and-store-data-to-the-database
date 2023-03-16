from unittest.mock import patch

import pytest

from config import Config
from src.controller import (DriverAdaptor, get_drivers_from_db,
                            get_drivers_from_files)
from tests.test_helpers import create_driver

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


@patch(
    "src.controller.Files.find_files",
    return_value=["path_1", "path_2", "path_3"],
)
@patch(
    "src.controller.Files.open_files",
    return_value="file_content",
)
@patch(
    "src.controller.FormatFile.format_file_abbreviation_data",
    return_value=DICT_ABB,
)
@patch(
    "src.controller.FormatFile.format_file_time",
    return_value=DICT_TIME,
)
@patch("src.controller.Drivers.build_report", return_value=drivers_list_5)
def test_get_drivers_from_files(mock_build_report, mock_format_file_time, mock_format_file_abbr, mock_open_files, mock_find_files):
    assert get_drivers_from_files() == list_drivers_files
    mock_find_files.assert_called_with(Config.FOLDER_FILES)
    mock_open_files.assert_called_with("path_2")
    mock_format_file_abbr.assert_called_with("file_content")
    mock_format_file_time.assert_called_with("file_content")
    mock_build_report.assert_called_with(DICT_ABB, DICT_TIME, DICT_TIME)


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


@patch("src.models.DataBaseDrivers.select", return_value=drivers_list_3)
def test_get_drivers_from_db(mock_DataBaseDrivers):
    assert get_drivers_from_db() == drivers_list_3
    mock_DataBaseDrivers.assert_called_once()
