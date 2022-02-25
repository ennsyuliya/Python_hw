# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Решите задание в одну строку. Подсказка: используйте функцию range() и генератор.


my_list = range(20,240)
print(my_list)
new_list = [el for el in my_list if el % 20 == 0]
print(new_list)
new_list21 = [el for el in my_list if el % 21 == 0]
print(new_list21)
