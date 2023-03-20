# 1. Дано ціле число (int). Визначити скільки нулів у цьому числі.
num = 2340790060
str_num = str(num)
count = str_num.count('0')
print(count)
# 2. Дано ціле число (int). Визначити скільки нулів наприкінці цього числа. Наприклад для числа 1002000 - три нулі
num = 77006043000000
num_str = str(num)
result = (len(num_str) - len(num_str.rstrip('0')))
print(result)

# 3. Дано списки my_list_1 та my_list_2.
# Створити список my_result, який спочатку помістити
# елементи на парних місцях my_list_1, а потім всі елементи на парних місцях my_list_2.
my_list_1 = [8, 'o', 0, 9, 5]
my_list_2 = [9, 93,23, 'i', 38]
my_result = []
for i in my_list_1[1::2]:
    my_result.append(i)
for i in my_list_2[1::2]:
    my_result.append(i)
print(my_result)

# 4. Наведено список my_list. СТВОРИТИ НОВИЙ список new_list у якого перший елемент з my_list
# стоїть на останньому місці. Якщо my_list [1,2,3,4], то new_list[2,3,4,1]
my_list = [4, 7, 'ft', 'pr', 98, 27]
count_list = []
count_list.append(my_list.pop(0))
new_list = []
for i in my_list:
    new_list.append(i)
new_list.extend(count_list)
print(new_list)

# 5. Даний список my_list. У цьому списку перший елемент переставити на останнє місце.
# [1,2,3,4] -> [2,3,4,1]. Перестворювати список не можна! (використовуйте метод pop)

my_list = [9, 334, 245, 22]
my_list.append(my_list.pop(0))
print(my_list)
# 6. Дано рядок у якому є числа (розділяються пробілами).
# Наприклад "43 більше ніж 34, але менше ніж 56". Знайти суму ВСІХ ЧИСЕЛ (А НЕ ЦИФР) у цьому рядку.
# Для цього прикладу відповідь - 133. (використовуйте split та перевірку isdigit)
my_string = "129 більше ніж 120, але менше ніж 150"
new_list = list(my_string)
my_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', " "]
end_list = []
for i in new_list:
    if i in my_list:
        end_list.append(i)
new_string = ''
x = new_string.join(end_list)
list_5 = x.split(' ')
number = 0
for i in list_5:
    if i != '':
        number += int(i)
print(number)

# 7. Наведено список чисел. Визначте, скільки в цьому списку елементів,
# які більше суми двох своїх сусідів (ліворуч і праворуч), і НАДРУКАЙТЕ КІЛЬКІСТЬ таких елементів.
# Останні елементи списку ніколи не враховуються, оскільки у них недостатньо сусідів.
# Для списку [2,4,1,5,3,9,0,7] відповіддю буде 3, тому що 4> 2+1, 5> 1+3, 9>3+0.
my_list = [2,4,1,5,3,9,0,7]
count = 0

for i in range(1, len(my_list)-1):
    if my_list[i] > my_list[i - 1] + my_list[i + 1]:
        count += 1

print(count)
# 8. Даний список my_list, в якому можуть бути як рядки (type str), так і цілі числа (type int).
# Наприклад [1, 2, 3, "11", "22", 33]
# Створити новий список у який помістити лише рядки з my_list.
my_list = [1, 2, 3, "11", "22", 33]
new_list = [i for i in my_list if isinstance(i, str)]
print(new_list)

# 9. Дано рядок my_str. Створити список в який помістити символи з my_str,
# які зустрічаються в рядку ТІЛЬКИ ОДИН разів.

my_str = "iwejiwroi voieioe93 02sk"
my_list = []

for i in set(my_str):
    if my_str.count(i) == 1:
        my_list.append(i)

print(my_list)
# 10. Дано два рядки. Створити список, у якому помістити ті символи,
# які є в обох рядках хоча б один раз.

my_str_1 = "ougup68unt"
my_str_2 = "guiuolp85ewo24"

symbols = set(my_str_1).intersection(set(my_str_2))
result = list(symbols)
print(result)
# 11. Дано два рядки. Створити список, у якому помістити ті символи, які є в обох рядках,
# але в кожній ТІЛЬКИ З одного разу.
# Приклад: для рядків "aaaasdf1" та "asdfff2" відповідь ["s", "d"], т.к. ці символи є в кожному рядку по одному раз
my_str_1 = "ougup68nt"
my_str_2 = "guiuolp85oew24"
my_list =[]
for i in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(i) == 1 and my_str_2.count(i) == 1:
        my_list.append(i)

print(my_list)