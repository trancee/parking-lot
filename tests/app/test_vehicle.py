import pytest

from tests import MainTestCase

from app.vehicle import Vehicle


class VehicleTestCase(MainTestCase):

    registration_number = 'KA-01-HH-1234'
    colour = 'White'

    def test_constructor(self):
        vehicle = Vehicle(self.registration_number, self.colour)
        assert vehicle

    def test_constructor_fail(self):
        with pytest.raises(TypeError):
            vehicle = Vehicle()

    def test_equality(self):
        vehicle1 = Vehicle(self.registration_number, self.colour)
        assert vehicle1
        vehicle2 = Vehicle(self.registration_number, self.colour)
        assert vehicle2

        assert vehicle1 == vehicle2

    def test_inequality(self):
        vehicle1 = Vehicle(self.registration_number, self.colour)
        assert vehicle1
        vehicle2 = Vehicle(self.registration_number, None)
        assert vehicle2

        assert vehicle1 != vehicle2

    def test_property(self):
        vehicle = Vehicle(self.registration_number, self.colour)
        assert vehicle

        assert vehicle.registration_number == self.registration_number
        assert vehicle.colour == self.colour

    def test_property_none(self):
        vehicle = Vehicle(None, None)
        assert vehicle

        assert vehicle.registration_number != self.registration_number
        assert vehicle.registration_number is None
        assert vehicle.colour != self.colour
        assert vehicle.colour is None
