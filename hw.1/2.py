#Пользователь вводит время в секундах.
# Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.

tame = int(input('Введите время в секундах '))
hour = (tame) // 3600
minute = (tame-hour * 3600) // 60
seconds = (tame - (hour*3600) - (minute * 60))



print(f"'Время ' {hour:02} : {minute:02} : {seconds:02}")
