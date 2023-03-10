from task_Barvynska import Drivers, Files, FormatFile

from config import Config
from src.models import DB_drivers


def get_drivers_from_files() -> list[dict[str, str]]:
    file_start, file_end, abbreviations_file = Files.find_files(Config.FOLDER_FILES)
    list_drivers = Drivers.build_report(
        FormatFile.format_file_abbreviation_data(Files.open_files(abbreviations_file)),
        FormatFile.format_file_time(Files.open_files(file_start)),
        FormatFile.format_file_time(Files.open_files(file_end)),
        )
    return [x.__dict__ for x in list_drivers]


if DB_drivers.__len__() == 0:
    DB_drivers.insert_many(get_drivers_from_files()).execute()
