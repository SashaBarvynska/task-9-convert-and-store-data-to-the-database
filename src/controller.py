import json
from typing import Any

from flask import make_response, wrappers
from simplexml import dumps
from task_Barvynska import Driver, Drivers

from src.database.models import DataBaseDrivers


class DriverAdaptor:
    def __init__(self):
        self.list_drivers = self.get_drivers_from_db()

    def get_drivers_from_db(self) -> list[Driver]:
        query = DataBaseDrivers.select()
        list_drivers = []
        for i in query:
            list_drivers.append(Driver(i.abbreviation, i.driver, i.car, i.start_time, i.end_time, i.speed))
        return list_drivers

    def sort_data(self, order: bool) -> list[Driver]:
        return Drivers.sort_data(self.list_drivers, order)

    def get_driver(self, key: str, value) -> Driver or None:
        driver_list = [driver for driver in self.list_drivers if getattr(driver, key).lower() == value.lower()]
        if not driver_list:
            return None
        return driver_list[0]


def make_xml_response(list_drivers: list[dict[str, Any]], code: int) -> wrappers.Response:
    response = make_response(dumps({'response': list_drivers}), code)
    response.mimetype = 'application/xml'
    return response


def make_json_response(list_drivers: list[dict[str, str]], code: int) -> wrappers.Response:
    response = make_response(json.dumps(list_drivers), code)
    response.mimetype = 'application/json'
    return response
