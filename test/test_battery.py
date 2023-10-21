import parts.battery.battery_collections as battery_collection
import unittest
from datetime import date, datetime


class TestnubbinBattery(unittest.TestCase):
    def create_battery(self, last_service_date: date):
        NubbinBattery = battery_collection.NubbinBattery

        return NubbinBattery(last_service_date=last_service_date)

    def test_battery_needs_service_happy_path(self):
        four_years_ago = datetime.now()
        four_years_ago = four_years_ago.replace(year=four_years_ago.year - 4)
        nubbin_battery = self.create_battery(last_service_date=four_years_ago.date())
        self.assertTrue(nubbin_battery.needs_service())

    def test_battery_not_needs_service(self):
        today = datetime.now()
        nubbin_battery = self.create_battery(last_service_date=today.date())
        self.assertFalse(nubbin_battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def create_battery(self, last_service_date: date):
        SpindlerBattery = battery_collection.SpindlerBattery

        return SpindlerBattery(last_service_date=last_service_date)

    def test_battery_needs_service_happy_path(self):
        two_years_ago = datetime.now()
        two_years_ago = two_years_ago.replace(year=two_years_ago.year - 2)
        spindler_battery = self.create_battery(last_service_date=two_years_ago.date())
        self.assertTrue(spindler_battery.needs_service())

    def test_battery_not_needs_service(self):
        today = datetime.now()
        spindler_battery = self.create_battery(last_service_date=today.date())
        self.assertFalse(spindler_battery.needs_service())


if __name__ == "__main__":
    unittest.main()
