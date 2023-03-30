# Для завданнь 1-7 за основу можете взяти код із попередніх ДЗ.
#
# 1. Написати функцію яка приймає один параметр – список рядків my_list. Функція повертає новий список у якому міститься
# елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщона парному – залишити без зміни.
my_list = [
    'wehifuh',
    'weihf',
    '2839soe',
    'ijwd',
    92093
]
new_list = []
def new_func(my_list):
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(str(my_list[i])[::-1])
        else:
            new_list.append(my_list[i])
    return new_list
print(new_func(my_list))
# 2. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи my_list у яких перший символ - буква "a".
my_list = [
    'aehifuh',
    'aeihf',
    '2839soe',
    'ajwd',
    92093
]
a_list = []
def a_func(my_list):
    for i in range(len(my_list)):
        if str(my_list[i]).startswith('a'):
            a_list.append(my_list[i])
    return a_list
print(a_func(my_list))
# 3. Написати функцію яка приймає один параметр – список рядків my_list.
# Функція повертає новий список у якому міститься елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
my_list = [
    'aehifuh',
    'eihf',
    '283asoe',
    'ajwd',
    92093
]
a_find_list = []
def a_find_func(my_list):
    for i in range(len(my_list)):
        if 'a' in str(my_list[i]):
            a_find_list.append(my_list[i])
    return a_find_list
print(a_find_func(my_list))
# 4. Написати функцію яка приймає один параметр - список рядків my_list у якому може бути як рядки (type str) і цілі числа (type int).
# Функція повертає новий список у якому містяться лише рядки з my_list.
my_list = [1, 2, 3, "11", "22", 33]
new_list = []
def str_find_func(my_list):
    new_list = [i for i in my_list if isinstance(i, str)]
    return new_list
print(str_find_func(my_list))
# 5. Написати функцію яка приймає один параметр – рядок my_str.
# Функція повертає новий список у якому містяться ті символи з my_str, які зустрічаються у рядку лише один раз.
my_str = "iwejiwroi voieioe93 02sk"
once_list = []
def once_func(my_str):
    for i in set(my_str):
        if my_str.count(i) == 1:
            once_list.append(i)
    return once_list
print(once_func(my_str))
# 6. Написати функцію яка приймає один параметр - два рядки.
# Функція повертає список у який помістити ті символи, які є в обох рядках хоча б один раз.
my_str_1 = "ougup68unt"
my_str_2 = "guiuolp85ewo24"
def find_symbols(my_str_1, my_str_2):
    symbols = set(my_str_1).intersection(set(my_str_2))
    count_symbols = list(symbols)
    return count_symbols
print(find_symbols(my_str_1, my_str_2))
# 7. Написати функцію яка приймає два параметри - два рядки.
# Функція повертає список до якого входять ті символи, які є в обох рядках, але в кожному лише по одному разу.
my_str_1 = "ougup68nt"
my_str_2 = "guiuolp85oew24"
my_list =[]
def find_one_symbols(my_str_1, my_str_2):
    for i in set(my_str_1).intersection(set(my_str_2)):
        if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
            my_list.append(i)
    return my_list
print(find_one_symbols(my_str_1, my_str_2))
# 8. Дано списки names та domains (створити самостійно). Написати функцію для генерування e-mail у форматі:
#     "ім'я . число від 100 до 999 @ стрінга з літер довжиною від 5 до 7 символів . домен"
# Прізвище та домен брати випадковим чином із заданих списків переданих у функцію у вигляді параметрів.
# Рядок і число генерувати випадковим чином.
from random import randint, choice
from string import ascii_lowercase
names = ['johnson', 'stark', 'clarck', 'air']
domains = ["net", "com", "ua"]
def generating_email(names, domains):
    str_line = "".join([choice(ascii_lowercase) for _ in range(randint(5, 7))])
    email = f"{choice(names)}{str(randint(100, 999))}{'@'}{str_line}{choice(domains)}"
    return email
print(generating_email(names, domains))
# Приклад використання функції:
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
#
# Відповідь: miller.249@sgdyyur.com