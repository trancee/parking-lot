from app.parking_lot import ParkingLot


class Commands:
    parking_lot = None

    def create_parking_lot(self, num_slots):
        if isinstance(num_slots, str):
            num_slots = int(num_slots)

        if isinstance(num_slots, int):
            if self.parking_lot:
                return False

            self.parking_lot = ParkingLot(num_slots)
            return True

        return False


    def park(self, registration_number, colour):
        if self.parking_lot:
            return self.parking_lot.park(registration_number, colour)

    def leave(self, slot):
        if isinstance(slot, str):
            slot = int(slot)

        if isinstance(slot, int):
            if self.parking_lot:
                return self.parking_lot.leave(slot)

        return False


    def status(self):
        if self.parking_lot:
            print ('Slot\tRegistration No.\tColour')

            for i, vehicle in enumerate(self.parking_lot.slots):
                if vehicle:
                    # Adjust the index
                    slot = i + 1

                    print ('%d\t%s\t%s' % (slot, vehicle.registration_number, vehicle.colour))

            return True

        return False


    def registration_numbers_for_cars_with_colour(self, colour):
        return False

    def slot_numbers_for_cars_with_colour(self, colour):
        return False

    def slot_number_for_registration_number(self, registration_number):
        return False
