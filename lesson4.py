#У вас є змінна величина, тип - int. Напишіть тернарний оператор для змінної new_value за таким правилом: якщо
#значення менше 100, то new_value дорівнює половині значення, у протилежному випадку - протиположне
#значенню число

value = 978
if (value < 100):
    new_value = value / 2
else:
    new_value = - value
print(new_value)

#2) У вас є змінна величина, тип - int. Написати тернарний оператор для змінної new_value за таким правилом: якщо
# значення менше 100, то new_value дорівнює 1, у протилежному випадку - 0
value = 567
if (value < 100):
    new_value = 1
else:
    new_value = 0
print(new_value)
#3) У вас є змінна величина, тип - int. Напишіть тернарний оператор для змінного new_value за таким правилом: якщо
# значення менше 100, то new_value дорівнює True, у протилежному випадку - False

value = 98
if (value < 100):
    new_value = True
else:
    new_value = False
print(new_value)
#4) У вас є змінна my_str, тип - str. Якщо її довше менше 5, то допишіть в кінці строки її ж.
# Приклад: було - "qwer", стало - "qwerqwer". Якщо довжина не менше 5, то залишити строку як є.

my_str = 'yyjo'
if len(my_str) < 5:
    new_str = 2 * my_str
else:
    new_str = my_str
print(new_str)
#У вас є змінна my_str, тип - str. Якщо її довжина менше 5, то допишіть в кінці рядка перевернуту її ж.
# Приклад: було - "qwer", стало - "qwerrewq". Якщо довжина не менше 5, то залишити строку як є.
my_str = 'ukgi'
if len(my_str) < 5:
    new_str = my_str[::-1]
else:
    new_str = my_str
print(new_str)

#Допрацювати завдання з калькулятором, щоб в кінці вичислення у користувача запитало, чи потрібен  калькулятор ще.
# Якщо так, то запустити програму з початку.
flag = True
while flag:
    try:
        value_1 = (input("Please type a number: "))
        value_float_1 = float(value_1)
        value_2 = (input("Please type another number: "))

        value_float_2 = float(value_2)
        value_operator = input("Please choose operator:\n 1 '+'\n 2 '-'\n 3 '*'\n 4 '/'\n your answer:")
        if value_operator == '1':
            result = value_float_1 + value_float_2
        elif value_operator == '2':
            result = value_float_1 - value_float_2
        elif value_operator == '3':
            result = value_float_1 * value_float_2
        elif value_operator == '4':
            result = value_float_1 / value_float_2
        else:
            result = "Ви ввели некоректну операцію"
        print(result)
        answer = input('Чи потрібен Вам калькулятор далі? (Так\Ні): ')
        if answer == 'Так' or 'так':
            flag = True
        else:
            flag = False

    except ValueError:
        print('Ви ввели не число!')
    except ZeroDivisionError:
        print('Ееей, на нуль ділити не можна!!!')