# Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

with open('test1.txt', 'w') as file:
    input_line= input('text: \n')
    while input_line:
        file.write(f'{input_line}\n')
        input_line=input('text: \n')
