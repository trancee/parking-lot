class Vehicle:
    def __init__(self, registration_number, colour):
        self.__registration_number = registration_number
        self.__colour = colour

    def __eq__(self, other):
        return (
            self.__registration_number == other.__registration_number and
            self.__colour == other.__colour
        )

class ParkingLot:
    def __init__(self, num_slots):
        self.__slots = [None] * num_slots
        self.__vehicles = []
        print ('Created a parking lot with %d slots' % (len(self.__slots)))

    @property
    def slots(self):
        return self.__slots
    @property
    def vehicles(self):
        return self.__vehicles

    def park(self, registration_number, colour):
        __vehicle = Vehicle(registration_number, colour)

        if __vehicle in self.__vehicles:
            print ('Vehicle already in parking slot %d' % (self.__slots.index(__vehicle)))
            return False

        try:
            slot = next(i for i, slot in enumerate(self.__slots) if slot is None)

        except StopIteration:
            print ('Parking lot is full')
            return False

        self.__slots[slot] = __vehicle
        print ('Allocated slot number: %d' % (slot))

        self.__vehicles.append(__vehicle)
        return True

    def leave(self, slot):
        if slot >= 0 and slot < len(self.__slots):
            __vehicle = self.__slots[slot]

            self.__slots[slot] = None
            print ('Slot number %d is free' % (slot))

            self.__vehicles.remove(__vehicle)
            return True

        return False


parking_lot = None

def create_parking_lot(num_slots):
    global parking_lot

    if isinstance(num_slots, str):
        num_slots = int(num_slots)

    if isinstance(num_slots, int):
        if parking_lot:
            parking_lot = ParkingLot(num_slots)
            return True

    return False


def park(registration_number, colour):
    global parking_lot

    if parking_lot:
        return parking_lot.park(registration_number, colour)

def leave(slot):
    global parking_lot

    if isinstance(slot, str):
        slot = int(slot)

    if isinstance(slot, int):
        if parking_lot:
            return parking_lot.leave(slot)

    return False


def status():
    global parking_lot

    if parking_lot:
        return parking_lot.slots

    return False


def registration_numbers_for_cars_with_colour(colour):
    return False

def slot_numbers_for_cars_with_colour(colour):
    return False

def slot_number_for_registration_number(registration_number):
    return False
