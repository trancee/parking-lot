import pytest

from tests import MainTestCase

from app.parking_lot import ParkingLot
from app.vehicle import Vehicle


class ParkingLotTestCase(MainTestCase):

    num_slots = 3

    registration_number = 'KA-01-HH-1234'
    colour = 'White'

    def test_constructor(self):
        parking_lot = ParkingLot(self.num_slots)
        assert parking_lot

    def test_constructor_fail(self):
        with pytest.raises(TypeError):
            parking_lot = ParkingLot(None)

    def test_property(self):
        parking_lot = ParkingLot(self.num_slots)
        assert parking_lot

        assert isinstance(parking_lot.slots, list)
        assert len(parking_lot.slots) is self.num_slots
        assert parking_lot.slots == [None, None, None]

    def test_property_empty(self):
        parking_lot = ParkingLot(0)
        assert parking_lot

        assert isinstance(parking_lot.slots, list)
        assert len(parking_lot.slots) is 0
        assert parking_lot.slots == []

    def test_park(self):
        parking_lot = ParkingLot(self.num_slots)
        assert parking_lot

        result = parking_lot.park(self.registration_number, self.colour)
        assert result is True

    def test_park_full(self):
        parking_lot = ParkingLot(1)
        assert parking_lot

        result = parking_lot.park(self.registration_number, self.colour)
        assert result is True
        result = parking_lot.park(self.registration_number, None)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 1 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Sorry, parking lot is full'

    def test_park_same(self):
        parking_lot = ParkingLot(1)
        assert parking_lot

        result = parking_lot.park(self.registration_number, self.colour)
        assert result is True
        result = parking_lot.park(self.registration_number, self.colour)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 1 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Allocated slot number: 1'

    def test_leave(self):
        parking_lot = ParkingLot(self.num_slots)
        assert parking_lot

        assert isinstance(parking_lot.slots, list)
        assert len(parking_lot.slots) is self.num_slots
        assert parking_lot.slots == [None, None, None]

        result = parking_lot.park(self.registration_number, self.colour)
        assert result is True

        assert isinstance(parking_lot.slots, list)
        assert len(parking_lot.slots) is self.num_slots
        assert parking_lot.slots == [Vehicle(self.registration_number, self.colour), None, None]

        result = parking_lot.leave(1)
        assert result is True

        assert isinstance(parking_lot.slots, list)
        assert len(parking_lot.slots) is self.num_slots
        assert parking_lot.slots == [None, None, None]

    def test_leave_invalid(self):
        parking_lot = ParkingLot(self.num_slots)
        assert parking_lot

        result = parking_lot.leave(0)
        assert result is False
