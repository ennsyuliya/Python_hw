# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

print('Решение через list')


def season(m):
    if m == 12 or m == 1 or m == 2:
        return 'Это зима'
    elif m == 3 or m == 4 or m == 5:
        return 'Это весна'
    elif m == 6 or m == 7 or m == 8:
        return 'Это лето'
    elif m == 9 or m == 10 or m == 11:
        return 'Это осень'
    else:
        return 'Нет такого месяца'
result = season(int(input('Введите номер месяца: ')))
print(result)

print('Решение через dict')
seasons_list = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month_dict = int(input('Введите месяц: '))
for key in seasons_list.keys():
    if month_dict in seasons_list[key]:
        print(key)

