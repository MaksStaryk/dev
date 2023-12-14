import time
from abc import ABC, abstractmethod

class Alive(ABC):

    @abstractmethod
    def count_alive_instance(self):
        pass

class Plants(Alive):
    def __init__(self, count_plants, koef_grown = 30, koef_rabbits_attack:int =10):
        self.count_plants = count_plants
        self.koef_grown = koef_grown
        self.koef_rabbits_attack = koef_rabbits_attack

    @property
    def count_alive_instance(self) -> int:
        return self.count_plants

    def  year_grown(self,):
        self.count_plants *= self.koef_grown
    def rabbits_attack(self,count_rabbits):
        self.count_plants -= count_rabbits * self.koef_rabbits_attack
class Rabbits(Alive):
    def __init__(self, count_rabbits, koef_reproduction = 15, koef_rabbits_attack:int =10, koef_fox_attack:int =3 ):
        self.count_rabbits = count_rabbits
        self.koef_reproduction = koef_reproduction
        self.koef_rabbits_attack = koef_rabbits_attack
        self.koef_fox_attack = koef_fox_attack

    @property
    def count_alive_instance(self) -> int:
        return self.count_rabbits

    def  year_reproduction(self,):
        self.count_rabbits *= self.koef_reproduction

    def enough_food(self, count_plants):
        if self.count_rabbits * self.koef_rabbits_attack  > count_plants:
            rabbits_sell = self.count_rabbits - count_plants //self.koef_rabbits_attack
            print(f'warning Problem!!!! sell rabbits {rabbits_sell}')
            time.sleep(3)
            self.count_rabbits -= int(rabbits_sell * 0.8)


    def fox_attack(self, count_fox):
        self.count_rabbits -= count_fox * self.koef_fox_attack
        print(f'{self.count_rabbits}')


class Fox(Alive):
    def __init__(self, count_fox =1, koef_fox = 10, koef_fox_attack:int =2):
        self.count_fox = count_fox
        self.koef_fox = koef_fox
        self.koef_fox_attack = koef_fox_attack

    @property
    def count_alive_instance(self) -> int:
        return self.count_fox

    def  year_to_world(self,):
        self.count_fox *= self.koef_fox
    def enough_rabbits(self,count_rabbits):
        if self.count_fox * self.koef_fox > count_rabbits:
            fox_to_free = self.count_fox - count_rabbits // self.koef_fox_attack
            print(f'мы отпускаем кол-во лис :{fox_to_free}')
            time.sleep( 3)
            self.count_fox -= int(fox_to_free *8)


plants = Plants(20)

rabbits = Rabbits(6)

fox = Fox()

year = 1

while year <= 20:
    print(f'year {year}')
    print(f'count plants: {plants.count_alive_instance}')
    print(f'count rabbits: {rabbits.count_rabbits}')
    print(f'count fox: {fox.count_fox}')
    plants.year_grown()
    rabbits.year_reproduction()
    rabbits.enough_food(rabbits.count_rabbits)
    plants.rabbits_attack(rabbits.count_rabbits)
    rabbits.fox_attack(fox.count_fox)
    year += 1
