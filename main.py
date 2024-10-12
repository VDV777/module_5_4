# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
#
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
#
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
#
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class House:

    houses_history: list = []

    def __new__(cls, *args, **kwargs):

        cls.houses_history += [*args]

        return super().__new__(cls)

    def __init__(self, name: str, numberOfFloors: int):

        self.name: str = name
        self.numberOfFloors: int = numberOfFloors

    def goto(self, floor: int):
        if floor < 1 or floor > self.numberOfFloors:
            print('Такого этажа не существует')
        else:
            [print(x) for x in range(1, floor + 1)]

    def __len__(self):
        return self.numberOfFloors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numberOfFloors}'

    def __eq__(self, other):

        if isinstance(other, House):
            return self.numberOfFloors == other.numberOfFloors
        return False

    def __lt__(self, other):

        if isinstance(other, House):
            return self.numberOfFloors < other.numberOfFloors
        return False

    def __le__(self, other):

        if isinstance(other, House):
            return self.numberOfFloors <= other.numberOfFloors
        return False

    def __gt__(self, other):

        if isinstance(other, House):
            return self.numberOfFloors > other.numberOfFloors
        return False

    def __ge__(self, other):

        if isinstance(other, House):
            return self.numberOfFloors >= other.numberOfFloors
        return False

    def __ne__(self, other):

        if isinstance(other, House):
            return self.numberOfFloors != other.numberOfFloors
        return False

    def __add__(self, value: int):

        self.numberOfFloors += value

        return self

    def __radd__(self, value: int):

        self.numberOfFloors += value

        return self

    def __iadd__(self, value: int):

        self.numberOfFloors += value

        return self

    def __del__(self):

        print(f'{self.name} снесён, но он останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
