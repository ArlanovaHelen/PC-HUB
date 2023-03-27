# 1. Наведено список рядків my_list. Створити новий список до якого помістити елементи з my_list за таким правилом:
# Якщо рядок стоїть на непарному місці my_list, то його замінити на перевернутий рядок. "qwe" на "ewq".
# Якщо на парному – залишити без зміни. Завдання зробити за допомогою enumerate або range.
my_list = [
    'wehifuh',
    'weihf',
    '2839soe',
    'ijwd',
    92093
]
new_list = []
for i in range(len(my_list)):
    if i / 2 == 0:
        new_list.append(my_list[i][::-1])
    else:
        new_list.append(my_list[i])
print(new_list)

# 2. Наведено список рядків my_list. Створити новий список до якого помістити елементи my_list
# у яких перший символ - буква "a".
my_list = [
    'aehifuh',
    'aeihf',
    '2839soe',
    'ajwd',
    92093
]
new_list = []
for i in range(len(my_list)):
    if str(my_list[i]).startswith('a'):
        new_list.append(my_list[i])
print(new_list)
# 3. Наведено список рядків my_list. Створити новий список до якого помістити
# елементи з my_list, у яких є символ - буква "a" на будь-якому місці.
my_list = [
    'aehifuh',
    'eihf',
    '283asoe',
    'ajwd',
    92093
]
new_list = []
for i in range(len(my_list)):
    if 'a' in str(my_list[i]):
        new_list.append(my_list[i])
print(new_list)
# 4) Даний список словників людей у форматі [{"name": "John", "age": 15}, ..., {"name": "Jack", "age": 45}]

name_list = [{"name": "Robert", 'age': 36},
{"name": "Nick", 'age': 24},
{"name": "John", 'age': 65},
{"name": "Eva", 'age': 8},
{"name": "Monica", 'age': 39},
{"name": "Arina", 'age': 19},]
# а) Створити список і помістити туди ім'я наймолодшої людини. Якщо вік збігається – помістити всі імена наймолодших.            ]
age_list = []
youngest = []
for i in name_list:
    age_list.append(i["age"])
min_age = min(age_list)
for i in name_list:
    if i["age"] == min_age:
        youngest.append(i["name"])
print(youngest)

# б) Створити список та помістити туди найдовше ім'я. Якщо довжина імені збігається - помістити такі імена.
long_list = []
longest = []
for i in name_list:
    long_list.append(len(i["name"]))
longest_name = max(long_list)
for i in name_list:
    if len(i["name"]) == longest_name:
        longest.append(i["name"])
print(longest)

# в) Порахувати середню вік усіх людей із початкового списку.

new_age_list = []
for i in name_list:
    new_age_list.append(i["age"])
print(new_age_list)
average = sum(new_age_list)/len(new_age_list)
print(average)

# 5) Дано два словники my_dict_1 і my_dict_2.
my_dict_1 = {"name": "Robert", 'age': 36, 'hobby': "swimming"}
my_dict_2 = {"name": "Marta", 'age': 15, 'ocupation': 'Project Manager'}
# а) Створити список із ключів, які є в обох словниках.
same_list = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
print(same_list)
# б) Створити список із ключів, які є у першому, але немає у другому словнику.
different_list = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
print(different_list)
# в) Створити новий словник з пар {ключ:значення} для ключів, які є в першому, але немає в другому словнику.
differ_keys_list = {key: my_dict_1[key] for key in different_list}
print(differ_keys_list)
# г) Об'єднати ці два словники у новий словник за правилом:
# якщо ключ є тільки в одному з двох словників - помі стити пару ключ: значення,
# якщо ключ є у двох словниках - помістити пару {ключ: [значення_з_першого_словника, значення_з_другого_словника]},
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}
united_list = my_dict_1.copy()
for key in my_dict_2:
    if key in united_list:
        united_list[key] = [united_list[key], my_dict_2[key]]
    else:
        united_list[key] = my_dict_2[key]
print(united_list)
