print('Задача "Нужно больше этажей"')
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def __str__(self):
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
    #Метод для сравнения количества этажей
    def __eq__(self, other):
        if isinstance(other, House):
            return  self.number_of_floors == other. number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == number_of_floors

    # Метод для проверки меньше чем (<)
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    # Метод для проверки меньше либо равно (<=)
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other. number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
#h2 = [2, 3]
print(h1)
print(h2)
print('"h1=h2"', h1 == h2) # __eq__
print('"h1<h2"', h1 < h2) # __lt__
print('"h1<=h2"', h1 <= h2) # __le__