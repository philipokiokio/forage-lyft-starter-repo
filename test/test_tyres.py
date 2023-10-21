import unittest
import parts.tyre.tyre_collections as tyre_collection
from typing import List


class TestCarriganTyres(unittest.TestCase):
    def create_tyre(self, sensor_readings: List[int]):
        CarriganTyres = tyre_collection.CarriganTyres

        return CarriganTyres(sensor_readings=sensor_readings)

    def test_tyre_needs_service_happy_path(self):
        sensor_readings = [0.5, 0.7, 0.5, 0.9]

        carrigan_tyres = self.create_tyre(sensor_readings=sensor_readings)

        self.assertTrue(carrigan_tyres.needs_service)
        self.assertEqual(carrigan_tyres.sensor_readings, sensor_readings)

    def test_tyre_not_need_service(self):
        sensor_readings = [0.5, 0.7, 0.5, 0.8]

        carrigan_tyres = self.create_tyre(sensor_readings=sensor_readings)
        self.assertFalse(carrigan_tyres.needs_service)
        self.assertEqual(carrigan_tyres.sensor_readings, sensor_readings)


class TestOctoprimeTyres(unittest.TestCase):
    def create_tyre(self, sensor_readings: List[int]):
        OctoprimeTyres = tyre_collection.OctoprimeTyres

        return OctoprimeTyres(sensor_readings=sensor_readings)

    def test_tyre_needs_service_happy_path(self):
        sensor_readings = [0.5, 0.7, 0.9, 0.9]

        octoprime_tyres = self.create_tyre(sensor_readings=sensor_readings)

        self.assertTrue(octoprime_tyres.needs_service)
        self.assertEqual(octoprime_tyres.sensor_readings, sensor_readings)

    def test_tyre_not_need_service(self):
        sensor_readings = [0.1, 0.7, 0.5, 0.5]

        octoprime_tyres = self.create_tyre(sensor_readings=sensor_readings)
        self.assertFalse(octoprime_tyres.needs_service)
        self.assertEqual(octoprime_tyres.sensor_readings, sensor_readings)
