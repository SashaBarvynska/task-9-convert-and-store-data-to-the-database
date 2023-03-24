import random

from faker import Faker
from faker_vehicle import VehicleProvider
from task_Barvynska import Driver

fake = Faker()
fake.add_provider(VehicleProvider)


def create_driver(number_of_drivers: int) -> list[Driver]:
    drivers_list = []
    for _ in range(number_of_drivers):
        abbreviation = fake.bothify("???", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        driver = fake.name()
        car = fake.vehicle_make()
        start_time = random.choice(["12:02:58.917", "12:00:00.000"])
        end_time = random.choice(["12:04:03.332", "12:01:12.434"])
        speed = random.choice(["1:04.415", "1:12.434", "1:04.000", "1:12.123", "1:07.415", "1:56.434"])
        driver = Driver(abbreviation, driver, car, start_time, end_time, speed)
        drivers_list.append(driver)
    return drivers_list
