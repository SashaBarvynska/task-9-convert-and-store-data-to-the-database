import json
import random

from simplexml import dumps
from task_Barvynska import Driver


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


def sort_list(drivers_list: list[Driver], order: bool) -> list[Driver]:
    return sorted(drivers_list, key=lambda x: x.speed, reverse=order)


def json_format(drivers_list: list[Driver], columns: int = 6) -> bytes:
    if columns == 2:
        result = json.dumps(
            [
                {"abbreviation": x.abbreviation, "driver": x.driver} for x in drivers_list
                ]
            ).replace(": ", ":").replace(", ", ",")
    else:
        result = json.dumps([x.__dict__ for x in drivers_list]).replace(": ", ":").replace(", ", ",")
    return f'{result}\n'.encode()


def xml_format(drivers_list: list[Driver], columns: int = 6) -> bytes:
    if columns == 2:
        result = dumps({'response': [{"abbreviation": x.abbreviation, "driver": x.driver} for x in drivers_list]})
    else:
        result = dumps({'response': [x.__dict__ for x in drivers_list]})
    return f'{result}'.encode()
