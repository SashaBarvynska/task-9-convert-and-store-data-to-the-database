from typing import Any

from task_Barvynska import Driver


def data_to_json(list_drivers: list[Driver]) -> list[dict[str, str]]:
    return [{"abbreviation": x.abbreviation, "driver": x.driver} for x in list_drivers]


def data_to_xml(list_drivers: list[Driver]) -> list[dict[str, Any]]:
    return [x.__dict__ for x in list_drivers]
