from app.vehicle import Vehicle


class ParkingLot:
    def __init__(self, num_slots):
        self.__slots = [None] * num_slots
        print ('Created a parking lot with %d slots' % (len(self.__slots)))

    @property
    def slots(self):
        return self.__slots

    def park(self, registration_number, colour):
        __vehicle = Vehicle(registration_number, colour)

        try:
            i = next(i for i, vehicle in enumerate(self.__slots) if vehicle and vehicle == __vehicle)

            # Adjust the index
            slot = i + 1

            print ('Allocated slot number: %d' % (slot))
            return True

        except StopIteration:
            pass

        try:
            i = next(i for i, vehicle in enumerate(self.__slots) if vehicle is None)

            # Adjust the index
            slot = i + 1

            self.__slots[i] = __vehicle
            print ('Allocated slot number: %d' % (slot))

        except StopIteration:
            print ('Sorry, parking lot is full')

        return True

    def leave(self, slot):
        if slot > 0 and slot <= len(self.__slots):
            # Adjust the index
            i = slot - 1

            __vehicle = self.__slots[i]

            self.__slots[i] = None
            print ('Slot number %d is free' % (slot))

            return True

        return False
