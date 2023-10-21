from abc import ABC
from parts import battery, engine, tyre


class Car(ABC):
    def __init__(
        self, engine: engine.Engine, battery: battery.Battery, tyres: tyre.Tyres
    ):
        self.engine = engine
        self.battery = battery
        self.tyres = tyres

    @property
    def needs_service(self):
        if (
            self.engine.needs_service
            or self.battery.needs_service
            or self.tyres.needs_service
        ):
            return True
        return False

    ...
