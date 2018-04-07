from app.vehicle import Vehicle


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
            i = next(i for i, vehicle in enumerate(self.__slots) if vehicle is None)

            # Adjust the index
            slot = i + 1

        except StopIteration:
            print ('Sorry, parking lot is full')
            return False

        self.__slots[i] = __vehicle
        print ('Allocated slot number: %d' % (slot))

        self.__vehicles.append(__vehicle)
        return True

    def leave(self, slot):
        if slot > 0 and slot <= len(self.__slots):
            # Adjust the index
            i = slot - 1

            __vehicle = self.__slots[i]

            self.__slots[i] = None
            print ('Slot number %d is free' % (slot))

            self.__vehicles.remove(__vehicle)
            return True

        return False
