import parts.engine.engine_collections as engine_collection
import unittest


class TestWilloughbyEngine(unittest.TestCase):
    def create_engine(self, current_mileage: int, last_service_mileage: int):
        WilloughbyEngine = engine_collection.WilloughbyEngine

        return WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )

    def test_engine_needs_service(self):
        willoughby_engine = self.create_engine(
            current_mileage=360000, last_service_mileage=12000
        )
        self.assertTrue(willoughby_engine.needs_service())
        self.assertEqual(willoughby_engine.current_mileage, 360000)
        self.assertEqual(willoughby_engine.last_service_mileage, 12000)

    def test_engine_not_needs_service(self):
        willoughby_engine = self.create_engine(
            current_mileage=360000, last_service_mileage=360000
        )
        self.assertFalse(willoughby_engine.needs_service())
        self.assertEqual(willoughby_engine.current_mileage, 360000)
        self.assertEqual(willoughby_engine.last_service_mileage, 360000)


class TestCapuletEngine(unittest.TestCase):
    def create_engine(self, current_mileage: int, last_service_mileage: int):
        CapuletEngine = engine_collection.CapuletEngine

        return CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )

    def test_engine_needs_service(self):
        capulet_engine = self.create_engine(
            current_mileage=48000, last_service_mileage=12000
        )
        self.assertTrue(capulet_engine.needs_service())
        self.assertEqual(capulet_engine.current_mileage, 48000)
        self.assertEqual(capulet_engine.last_service_mileage, 12000)

    def test_engine_not_needs_service(self):
        capulet_engine = self.create_engine(
            current_mileage=36000, last_service_mileage=360000
        )
        self.assertFalse(capulet_engine.needs_service())
        self.assertEqual(capulet_engine.current_mileage, 36000)
        self.assertEqual(capulet_engine.last_service_mileage, 360000)


class TestSternmanEngine(unittest.TestCase):
    def create_engine(self, warning_light_on: bool):
        SternmanEngine = engine_collection.SternmanEngine

        return SternmanEngine(warning_light_is_on=warning_light_on)

    def test_engine_needs_service(self):
        sternman_engine = self.create_engine(warning_light_on=True)
        self.assertTrue(sternman_engine.needs_service())
        self.assertEqual(sternman_engine.warning_light_is_on, True)

    def test_engine_not_needs_service(self):
        sternman_engine = self.create_engine(warning_light_on=False)
        self.assertFalse(sternman_engine.needs_service())
        self.assertEqual(sternman_engine.warning_light_is_on, False)


if __name__ == "__main__":
    unittest.main()
