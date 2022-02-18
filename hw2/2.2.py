#Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

print('Первый вариант')
string = input('Введите элемент ')
str_reverse = ''
symbols = list(string)
for el in range(len(string) // 2):
    tmp = symbols[el]
symbols[el] = symbols[len(string) - el - 1]
symbols[len(string) - el - 1] = tmp
str_reverse = ''.join(symbols)
print(str_reverse)

print('второй вариант')

list = input("Введите элементы списка ")
my_list = list[::-1]
print(my_list)
# если ввести буквы как-то затрудняюсь

print('Третий вариант')
var_1, var_2, var_3, var_4 = input('Введите элемент (4 знака)  ')
print(var_1, var_2, var_3, var_4)
var_1, var_2, var_3, var_4 = var_2, var_1, var_4,var_3
print(var_1, var_2, var_3, var_4)
# здесь не знаю как правильно, получается только с 4 значениями(
