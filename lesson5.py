# 1. Дано рядок.

my_string = 'eufho7280'
# a. виведіть третій символ цього рядка.
print(my_string[2])
# b. виведіть передостанній символ цього рядка.
print(my_string[-2])
# c. виведіть перші п'ять символів цього рядка.
for letter in (my_string)[0:5]:
     print(letter)
# d. виведіть весь рядок, крім двох останніх символів.
for letter in (my_string)[0:-2]:
     print(letter)
# e. виведіть усі символи з парними індексами (вважаючи, що індексація починається з 0, тому символи виводяться починаючи)
# з першого).
for letter in (my_string)[::2]:
     print(letter)
# f. виведіть усі символи з непарними індексами, тобто, починаючи з другого символу рядка.
for letter in (my_string)[1::2]:
     print(letter)
# g. виведіть усі символи у зворотному порядку.
for letter in (my_string)[::-1]:
     print(letter)
# h. виведіть усі символи рядка через один у зворотному порядку, починаючи з останнього.
for letter in (my_string)[::-2]:
     print(letter)
# i. виведіть довжину цього рядка.
print(len(my_string))
# 2. Дано рядок, що складається зі слів, розділених пробілами. Визначте, скільки у ній слів. Використовуйте для вирішення
# завдання функцію `count`
count_string = 'shjhs hfsiur shbwe kdcu owjifo'
string1 = count_string.count(' ')
print(int(string1) + 1) #це єдиний варіант з "count", до якого я додумалась) взагалі, робила б наступним чином:

words = count_string.split( )
print(len(words))
# 3. Користувач вводить окремо рядок `s` та один символ `ch`. Необхідно здійснити пошук у рядку `s` всіх символів `ch`.
# Для вирішення можна використовувати тільки функцію `find` (rfind), оператори `if` та `for` (while).

s = (input('Please, send a string: '))
ch = (input('Please, choose a symbol: '))
m = 0
flag = True
while flag:
    x = s.find(ch, m, )
    if x == -1:
        flag = False
    else:
        print(x)
        m = x + 1

# 11. Дано рядок. Замініть у цьому рядку всі появи літери `h` на літеру `H`, крім першого та останнього входження.
string_txt = 'hojojwrhlwhhgjhhhfdrjjhio'
x = string_txt.count('h')
k = x - 1
string2 = string_txt.replace("h", "H", k)
string3 = string2.replace("H", "h", 1)
print(string3)