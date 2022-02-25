#Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, first_param, second_param, third_param = argv

print("Имя скрипта: ", script_name)
print("\n<< Программа рассчета заработной платы сотрудника >>")
print("Выработка в часах: ", first_param)
print("Ставка в час: ", second_param)
print("Премия: ", third_param)

print("Зарплата сотрудника: ", (float(first_param) * float(second_param)) + float(third_param))

