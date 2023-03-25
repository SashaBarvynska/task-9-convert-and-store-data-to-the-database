import json

from simplexml import dumps
from task_Barvynska import Driver

from src.database.fixtures import create_driver

one_driver_in_list = create_driver(1)
many_drivers_in_list = create_driver(3)


def sort_list(drivers_list: list[Driver], order: bool) -> list[Driver]:
    return sorted(drivers_list, key=lambda x: x.speed, reverse=order)


def json_format(drivers_list: list[Driver], columns: int = 6) -> bytes:
    if columns == 2:
        result = json.dumps(
            [
                {"abbreviation": x.abbreviation, "driver": x.driver} for x in drivers_list
                ]
            )
    else:
        result = json.dumps([x.__dict__ for x in drivers_list])
    return f'{result}'.encode()


def xml_format(drivers_list: list[Driver], columns: int = 6) -> bytes:
    if columns == 2:
        result = dumps({'response': [{"abbreviation": x.abbreviation, "driver": x.driver} for x in drivers_list]})
    else:
        result = dumps({'response': [x.__dict__ for x in drivers_list]})
    return f'{result}'.encode()
