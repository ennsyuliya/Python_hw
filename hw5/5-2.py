# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

lines = 0
letters = 0
out_f = open("out_file.txt", "w")
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
out_f.writelines(str_list)
out_f.close()
str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
for line in open('out_file.txt', 'r'):
    lines += 1
    letters += len(line)
print("Lines:", lines)
print("Letters:", letters)
