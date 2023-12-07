class Chisla:
     chislo_1 = 6
     chislo_2 = 112

     def ekran(self):   #вывод на экран chislo_1 and chislo_2
         print(f'chislo 1: {Chisla.chislo_1}')
         print(f'chislo 2: {Chisla.chislo_2}')

     def change(self):  # изменяем chislo_1 and chislo_2
         self.chislo_1 = self.chislo_1 + 34
         self.chislo_2 = self.chislo_2 + 1000
         print(f'izmen chislo 1 : {self.chislo_1}')
         print(f'izmen chislo 2 : {self.chislo_2}')

     def sum(self):     # суммируем chislo_1 and chislo_2
         return print(f'сумма chislo 1 + chislo 2: {self.chislo_1 + self.chislo_2}')


     def rock_num(self):    # вывод ниабольшего числа из chislo_1 or chislo_2
         if self.chislo_1 > self.chislo_2:
             print(self.chislo_1)
         else:
             print(self.chislo_2)

chisla = Chisla()
chisla.ekran()          #вывод атрибутов на экран
Chisla.change(chisla)   #изменение атрибутов
chisla.sum()    # сумма chislo_1 + chislo_2
chisla.rock_num() #наибольшее из чисел