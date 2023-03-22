import json
from unittest.mock import patch

import pytest
from flask import Response
from simplexml import dumps

from src.controller import create_driver
from tests.test_helpers import json_format, sort_list, xml_format

drivers_list_1 = create_driver(2)

sorted_list_drivers_asc = sort_list(drivers_list_1, True)
sorted_list_drivers_desc = sort_list(drivers_list_1, False)

drivers_list_2 = create_driver(1)
driver = drivers_list_2[0]


@patch("src.controller.get_drivers_from_db", return_value=drivers_list_1)
@pytest.mark.parametrize("order, format, result", [
    (
        "desc", "json", json_format(sorted_list_drivers_asc)
    ),
    (
        "asc", "json", json_format(sorted_list_drivers_desc)
    ),
    (
        "desc", "xml", xml_format(sorted_list_drivers_asc)
    ),
    (
        "asc", "xml", xml_format(sorted_list_drivers_desc)
    )
    ])
def test_show_report(mock_get_drivers_from_db, order, format, result, client):
    response: Response = client.get(f"/report?order={order}&format={format}")
    assert response.status_code == 200
    assert result == response.data


@patch("src.controller.get_drivers_from_db", return_value=drivers_list_1)
@pytest.mark.parametrize("order, format, result", [
    (
        "desc", "json", json_format(sorted_list_drivers_asc, 2)
    ),
    (
        "asc", "json", json_format(sorted_list_drivers_desc, 2)
    ),
    (
        "desc", "xml", xml_format(sorted_list_drivers_asc, 2)
    ),
    (
        "asc", "xml", xml_format(sorted_list_drivers_desc, 2)
    )
    ])
def test_show_drivers(mock_get_drivers, order, format, result, client):
    response: Response = client.get(f"/report/drivers?order={order}&format={format}")
    assert response.status_code == 200
    assert response.data == result


@patch("src.controller.get_drivers_from_db", return_value=drivers_list_2)
@pytest.mark.parametrize("format, result", [
    (
        "json", f'{json.dumps(driver.__dict__)}'.encode()
    ),
    (
        "xml", f'{dumps({"response": driver.__dict__})}'.encode()
    ),
    ])
def test_get_info(mock_get_drivers, format, result, client):
    response: Response = client.get(f"/report/drivers/{driver.abbreviation}?format={format}")
    assert response.status_code == 200
    assert response.data == result


@patch("src.controller.get_drivers_from_db", return_value=drivers_list_2)
@patch("src.routes.DriverAdaptor.get_driver", return_value=None)
def test_get_info_error(mock_get_driver, mock_get_drivers, client):
    response: Response = client.get("/report/drivers/DRghfgR?format=json")
    assert response.status_code == 404
    assert response.data == b'{"message": "No such driver"}'
    mock_get_driver.assert_called_with("abbreviation", "DRghfgR")


def test_wrong_routes(client):
    response: Response = client.get("/report/&^%SashaBarvynska474")
    assert response.status_code == 404
    assert response.data == b'{"message": "Page Not Found"}'
