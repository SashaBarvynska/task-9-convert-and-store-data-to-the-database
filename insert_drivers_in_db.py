
from src.controller import get_drivers_from_files
from src.models import DB_drivers

if __name__ == '__main__':
    DB_drivers.create_table()
    if DB_drivers.__len__() == 0:
        DB_drivers.insert_many(get_drivers_from_files()).execute()
