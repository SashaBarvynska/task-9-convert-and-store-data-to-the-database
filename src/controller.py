from typing import Any

from flask import jsonify, make_response, wrappers
from simplexml import dumps
from task_Barvynska import Driver, Drivers, Files, FormatFile

from config import Config


def get_drivers() -> list[Driver]:
    file_start, file_end, abbreviations_file = Files.find_files(Config.FOLDER_FILES)
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),
        )
    return list_drivers


class DriverAdaptor:
    def __init__(self):
        self.list_drivers = get_drivers()

    def sort_data(self, order: bool) -> list[Driver]:
        return Drivers.sort_data(self.list_drivers, order)

    def get_driver(self, key: str, value) -> Driver or None:
        driver_list = [driver for driver in self.list_drivers if getattr(driver, key).lower() == value.lower()]
        if not len(driver_list):
            return None
        return driver_list[0]


def make_xml_response(list_drivers: list[dict[str, Any]], code: int) -> wrappers.Response:
    response = make_response(dumps({'response': list_drivers}), code)
    response.mimetype = 'application/xml'
    return response


def make_json_response(list_drivers: list[dict[str, str]], code: int) -> wrappers.Response:
    response = make_response(jsonify(list_drivers), code)
    response.mimetype = 'application/json'
    return response
