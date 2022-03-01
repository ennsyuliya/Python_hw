#Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json
companies = {}
pos_count, pos_sum = 0, 0
with open('task7.txt') as file:
    file_lines = file.readlines()

for line in file_lines:
    data = line.split()
    profit = float (data [2]) - float (data [3])
    companies.update({data[0]:profit})
    if profit > 0:
        pos_count += 1
        pos_sum += pos_count

averge_profit = pos_sum / pos_count
result = [companies, {'averge_profit':averge_profit}]

with open('result.json','w',  encoding='utf-8') as file:
    json.dump(result, file)

with open('result.json', encoding='utf-8') as file:
    result = json.load(file)
    print(result)
