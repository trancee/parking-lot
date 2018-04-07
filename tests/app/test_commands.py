import pytest

from tests import MainTestCase

from app.commands import Commands


class CommandsTestCase(MainTestCase):

    num_slots = 3

    registration_number = 'KA-01-HH-1234'
    colour = 'White'

    def setUp(self):
        self.commands = Commands()

    def test_create_parking_lot(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

    def test_create_parking_lot_str(self):
        result = self.commands.create_parking_lot(str(self.num_slots))
        assert result is True

    def test_create_parking_lot_invalid(self):
        result = self.commands.create_parking_lot(None)
        assert result is False

    def test_create_parking_lot_same(self):
        result = self.commands.create_parking_lot(0)
        assert result is True

        result = self.commands.create_parking_lot(0)
        assert result is False

    def test_park(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

    def test_park_fail(self):
        result = self.commands.park(self.registration_number, self.colour)
        assert result is False

    def test_leave(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.leave(1)
        assert result is True

    def test_leave_str(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.leave(str(1))
        assert result is True

    def test_leave_fail(self):
        result = self.commands.leave(1)
        assert result is False

    def test_status(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.status()
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Slot No.\tRegistration No.\tColour'
        assert outs[3] == '1\tKA-01-HH-1234\tWhite'

    def test_status_fail(self):
        result = self.commands.status()
        assert result is False

    def test_registration_numbers_for_cars_with_colour(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True
        result = self.commands.park(None, self.colour)
        assert result is True

        result = self.commands.registration_numbers_for_cars_with_colour(self.colour)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Allocated slot number: 2'
        assert outs[3] == 'KA-01-HH-1234, None'

    def test_registration_numbers_for_cars_with_colour_not_found(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.registration_numbers_for_cars_with_colour(None)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Not found'

    def test_registration_numbers_for_cars_with_colour_fail(self):
        result = self.commands.registration_numbers_for_cars_with_colour(None)
        assert result is False

    def test_slot_numbers_for_cars_with_colour(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True
        result = self.commands.park(None, self.colour)
        assert result is True

        result = self.commands.slot_numbers_for_cars_with_colour(self.colour)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Allocated slot number: 2'
        assert outs[3] == '1, 2'

    def test_slot_numbers_for_cars_with_colour_not_found(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.slot_numbers_for_cars_with_colour(None)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Not found'

    def test_slot_numbers_for_cars_with_colour_fail(self):
        result = self.commands.slot_numbers_for_cars_with_colour(None)
        assert result is False

    def test_slot_number_for_registration_number(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.slot_number_for_registration_number(self.registration_number)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == '1'

    def test_slot_number_for_registration_number_not_found(self):
        result = self.commands.create_parking_lot(self.num_slots)
        assert result is True

        result = self.commands.park(self.registration_number, self.colour)
        assert result is True

        result = self.commands.slot_number_for_registration_number(None)
        assert result is True

        out, err = self.capsys.readouterr()
        print (out) if out else None
        print (err) if err else None

        outs = out.split('\n')
        assert outs[0] == 'Created a parking lot with 3 slots'
        assert outs[1] == 'Allocated slot number: 1'
        assert outs[2] == 'Not found'

    def test_slot_number_for_registration_number_fail(self):
        result = self.commands.slot_number_for_registration_number(None)
        assert result is False
