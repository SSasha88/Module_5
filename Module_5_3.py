print('Задача "Нужно больше этажей"')
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):# - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>"
        return f'{self.name}, кол-во этажей: {self.number_of_floors}'
    def __len__(self):
        return self.number_of_floors
    def go_to(self, new_floor):
        print(f'Номер этажа {self.name}, на который нужно приехать:',new_floor)
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print( f'{self.name}, этаж:', floor)
        else:
            print(f'В {self.name} Такого этажа не существует')




h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print()
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))
#h1.go_to(5)
#h2.go_to(10)