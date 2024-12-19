print('Задача "Developer - не только разработчик"')
print()
print('Название и кол-во этажей:')
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'Номер этажа {self.name}, на который нужно приехать:',new_floor)
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print( f'{self.name}, этаж:', floor)
        else:
            print(f'В {self.name} Такого этажа не существует')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
print(h1.name,h1.number_of_floors)
print(h2.name,h2.number_of_floors)
print()
h1.go_to(5)
h2.go_to(10)




