#Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов

def my_func(a, b, c):
    if (a + b) > (a + c) and (a + b) > (b + c):
        return a + b
    if (a + c) > (a + b) and (a + c) > (b + c):
        return a + c
    if (b + c) > (a + b) and (b + c) > (a + c):
        return b + c
try:
    num_1 = int(input('Введите число а '))
    num_2 = int(input('Введите число b '))
    num_3 = int(input('Введите число с '))
    print(f'Сумма двух максимальных чисел равна:  {my_func(num_1, num_2, num_3)}')
except ValueError as e:
    print(f'{e}')