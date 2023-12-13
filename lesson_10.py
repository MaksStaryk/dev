"""task 2"""
class Passanger:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name

class Ticket:
    def __init__(self, passenger, put):
        self.passenger = passenger
        self.put = put

class Polet:
    def __init__(self, flight_number, napravlen):
        self.flight_number = flight_number
        self.napravlen = napravlen
        self.zakaz_bilet = []

    def zakaz(self,passanger):
        bilet = Ticket(passanger,self.napravlen)
        self.zakaz_bilet.append(bilet)
        print(f'zabronirovan bilet na {passanger.first_name} {passanger.second_name} na {self.napravlen}')

    def otmena_zakaza(self, passenger):
        for bilet in self.zakaz_bilet:
            if bilet.passenger == passenger:
                self.zakaz_bilet.remove(bilet)
                print(f'zakaz otmenen dlaj {passenger.first_name} {passenger.second_name} na {self.napravlen}')
                return

    def tablo(self):
        print(f'bilets zabronirovani dlaj poleta {self.flight_number} {self.napravlen}')
        for  bilet in self.zakaz_bilet:
            print(f'{bilet.passenger.first_name} {bilet.passenger.second_name}')

class Belavia:
    def __init__(self, name):
        self.name = name
        self.flight = []

    def create_flight(self,flight_number, napravlen):
        flight = Polet(flight_number, napravlen)
        self.flight.append(flight)
        return flight

belavia = Belavia("First Polet")

flight_1 = belavia.create_flight('BE234', 'Klaipeda')
flight_2 = belavia.create_flight('BE689', 'Guanchzou')

passanger_1 = Passanger('Kevin', 'Malcolm')
passanger_2 = Passanger('Natali', 'Portman')

flight_1.zakaz(passanger_1)
flight_1.zakaz(passanger_2)

flight_2.zakaz(passanger_2)
print()
flight_1.tablo()
print()
flight_2.tablo()



