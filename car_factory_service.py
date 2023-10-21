from car import Car
from datetime import date
import parts.engine.engine_collections as engine_collection
import parts.battery.battery_collections as battery_collection


class CarFactory:
    def create_calliope(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = engine_collection.CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.SpindlerBattery(
            last_service_date=last_service_date
        )

        return Car(engine=engine, battery=battery)

    def create_glissade(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = engine_collection.SternmanEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.SpindlerBattery(
            last_service_date=last_service_date
        )

        return Car(engine=engine, battery=battery)

    def create_palindrome(last_service_date: date, warning_light_on: bool) -> Car:
        engine = engine_collection.SternmanEngine(warning_light_on=warning_light_on)
        battery = battery_collection.SpindlerBattery(
            last_service_date=last_service_date
        )

        return Car(engine=engine, battery=battery)

    def create_rorschach(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = engine_collection.WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.NubbinBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)

    def create_thovex(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = engine_collection.CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.NubbinBattery(last_service_date=last_service_date)

        return Car(engine=engine, battery=battery)


thovex_car = CarFactory.create_thovex(
    last_service_date=date.today(), current_mileage=50000, last_service_mileage=0
)

print(thovex_car.needs_service)
print(thovex_car.battery.needs_service())
