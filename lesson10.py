# Всі пункти зробити як окремі функції та їх виклики.
#
# 1. Написати функцію, яка отримує як параметр ім'я файлу назви інтернет доменів (domains.txt)
# та повертає їх у вигляді списку рядків (назви повертати без крапки).
my_file = 'domains.txt'
def read_file(file):
    with open(file, 'r') as input_file:
        domain = input_file.read().splitlines()
        dom_list = [i.replace('.', '') for i in domain]
    return dom_list
print(read_file(my_file))


# 2. Написати функцію, яка отримує як параметр ім'я файла (names.txt)
# і повертає список усіх прізвищ із нього.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"
#
my_file = 'names.txt'
def read_file(name_file):
    with open(name_file, 'r') as input_file:
        name = input_file.read().splitlines()
    names = [line.split('\t')[1] for line in name if line]
    return names
print(read_file(my_file))

#
# 3. Написати функцію, яка отримує у вигляді параметра ім'я файлу (authors.txt) та повертає список
# словників виду {"date": date}
# у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
my_file = 'data.txt'
def read_file(name_file):
    with open(name_file, 'r') as input_file:
        date = input_file.read().splitlines()
    date_list = [{'date': line.split(' - ')[0]} for line in date if line]
    return date_list
print(read_file(my_file))
