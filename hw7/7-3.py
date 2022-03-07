# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

class Cell:
    def __init__(self, parts):
        self.parts = int(parts)

    def __add__(self, other):
        return Cell (self.parts + other.parts)

    def __sub__(self, other):
        diff = self.parts - other.parts
        if diff >= 0:
            return Cell(diff)
        else:
            return f'Ошибка'

    def __mul__ (self, other):
        return Cell (self.parts*other.parts)

    def __truediv__(self, other):
         return self.parts // other.parts


    def make_order(self, count):
        result = ''
        for i in range(int(self.parts // count)):
            result += '*' * count + '\n'
        result += '*' * (self.parts % count) + '\n'
        return result

    def __str__(self):
        return f'{self.parts}'

cell = Cell(24)
cell_2 = Cell(2)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(7))

