from abc import ABC
from parts import battery, engine


class Car(ABC):
    def __init__(self, engine: engine.Engine, battery: battery.Battery):
        self.engine = engine
        self.battery = battery

    @property
    def needs_service(self):
        if self.engine.needs_service or self.battery.needs_service:
            return True
        return False

    ...
