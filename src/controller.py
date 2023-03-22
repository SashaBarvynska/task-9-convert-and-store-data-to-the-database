import json
import random
from typing import Any

from flask import make_response, wrappers
from simplexml import dumps
from task_Barvynska import Driver, Drivers, Files, FormatFile

from config import Config
from src.models import DataBaseDrivers


def get_drivers_from_files() -> list[dict[str, str]]:
    file_start, file_end, abbreviations_file = Files.find_files(Config.FOLDER_FILES)
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),
        )
    return [x.__dict__ for x in list_drivers]


def get_drivers_from_db() -> list[Driver]:
    query = DataBaseDrivers.select()
    list_drivers = []
    for i in query:
        list_drivers.append(Driver(i.abbreviation, i.driver, i.car, i.start_time, i.end_time, i.speed))
    return list_drivers


class DriverAdaptor:
    def __init__(self):
        self.list_drivers = get_drivers_from_db()

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
    response = make_response(json.dumps(list_drivers), code)
    response.mimetype = 'application/json'
    return response


def create_driver(number_of_drivers: int) -> list[Driver]:
    drivers_list = []
    for _ in range(number_of_drivers):
        abbreviation = random.choice(["DRR", "AAA"])
        driver = random.choice(["Sasha Barvynska", "Andrew Holenkov"])
        car = random.choice(["RED BULL RACING TAG HEUER", "MERCEDES"])
        start_time = random.choice(["12:02:58.917", "12:00:00.000"])
        end_time = random.choice(["12:04:03.332", "12:01:12.434"])
        speed = random.choice(["1:04.415", "1:12.434", "1:04.000", "1:12.123", "1:07.415", "1:56.434"])
        driver = Driver(abbreviation, driver, car, start_time, end_time, speed)
        drivers_list.append(driver)
    return drivers_list
