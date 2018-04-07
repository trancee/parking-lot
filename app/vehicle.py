class Vehicle:
    def __init__(self, registration_number, colour):
        self.__registration_number = registration_number
        self.__colour = colour

    def __eq__(self, other):
        return (
            self.__registration_number == other.__registration_number and
            self.__colour == other.__colour
        )

    @property
    def registration_number(self):
        return self.__registration_number

    @property
    def colour(self):
        return self.__colour
