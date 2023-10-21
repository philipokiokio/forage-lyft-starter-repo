from car import Car
from datetime import date
import parts.engine.engine_collections as engine_collection
import parts.battery.battery_collections as battery_collection
import parts.tyre.tyre_collections as tyre_collextion
from typing import List


class CarFactory:
    def create_calliope(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        sensor_readings: List[int],
    ) -> Car:
        engine = engine_collection.CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.SpindlerBattery(
            last_service_date=last_service_date
        )
        tyres = tyre_collextion.CarriganTyres(sensor_readings=sensor_readings)

        return Car(engine=engine, battery=battery, tyres=tyres)

    def create_glissade(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        sensor_readings: List[int],
    ) -> Car:
        engine = engine_collection.SternmanEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.SpindlerBattery(
            last_service_date=last_service_date
        )
        tyres = tyre_collextion.CarriganTyres(sensor_readings=sensor_readings)

        return Car(engine=engine, battery=battery, tyres=tyres)

    def create_palindrome(
        last_service_date: date, warning_light_on: bool, sensor_readings: List[int]
    ) -> Car:
        engine = engine_collection.SternmanEngine(warning_light_on=warning_light_on)
        battery = battery_collection.SpindlerBattery(
            last_service_date=last_service_date
        )
        tyres = tyre_collextion.OctoprimeTyres(sensor_readings=sensor_readings)

        return Car(engine=engine, battery=battery, tyres=tyres)

    def create_rorschach(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        sensor_readings: List[int],
    ) -> Car:
        engine = engine_collection.WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.NubbinBattery(last_service_date=last_service_date)
        tyres = tyre_collextion.OctoprimeTyres(sensor_readings=sensor_readings)

        return Car(engine=engine, battery=battery, tyres=tyres)

    def create_thovex(
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        sensor_readings: List[int],
    ) -> Car:
        engine = engine_collection.CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        battery = battery_collection.NubbinBattery(last_service_date=last_service_date)
        tyres = tyre_collextion.CarriganTyres(sensor_readings=sensor_readings)

        return Car(engine=engine, battery=battery, tyres=tyres)
