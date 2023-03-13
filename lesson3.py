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
except ValueError:
    print('Ви ввели не число!')
except ZeroDivisionError:
    print('Ееей, на нуль ділити не можна!!!')





