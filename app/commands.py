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

        return False

    def leave(self, slot):
        if self.parking_lot:
            if isinstance(slot, str):
                slot = int(slot)

            if isinstance(slot, int):
                return self.parking_lot.leave(slot)

        return False


    def status(self):
        if self.parking_lot:
            print ('Slot No.\tRegistration No.\tColour')

            for i, vehicle in enumerate(self.parking_lot.slots):
                if vehicle:
                    # Adjust the index
                    slot = i + 1

                    print ('%d\t%s\t%s' % (slot, vehicle.registration_number, vehicle.colour))

            return True

        return False


    def registration_numbers_for_cars_with_colour(self, colour):
        if self.parking_lot:
            registration_numbers = [vehicle.registration_number for vehicle in self.parking_lot.slots if vehicle and vehicle.colour == colour]

            if registration_numbers:
                print (', '.join(registration_numbers))
                return True

            else:
                print ('Not found')

        return False

    def slot_numbers_for_cars_with_colour(self, colour):
        if self.parking_lot:
            # Adjust the index
            slots = [str(i + 1) for i, vehicle in enumerate(self.parking_lot.slots) if vehicle and vehicle.colour == colour]

            if slots:
                print (', '.join(slots))
                return True

            else:
                print ('Not found')

        return False

    def slot_number_for_registration_number(self, registration_number):
        if self.parking_lot:
            try:
                i = next(i for i, vehicle in enumerate(self.parking_lot.slots) if vehicle and vehicle.registration_number == registration_number)

                # Adjust the index
                slot = i + 1

            except StopIteration:
                print ('Not found')
                return False

            print (slot)
            return True

        return False
