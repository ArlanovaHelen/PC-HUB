# Написати клас та реалізувати його методи: (основа – ДЗ № 10)
#
# 1. Ініціалізація класу з одним параметром – ім'я файлу.
#
# 2. Написати метод екземпляра класу, який створює атрибут екземпляра класу
# у вигляді списку рядків (назви повертати без крапки)
#
# 2. Написати метод екземпляра класу, який повертає список усіх прізвищ із файлу.
# Кожен рядок файлу містить номер, прізвище, країну, кілька (таблиця взята з вікіпедії).
# Розділювач - символ табуляції "t"
#
# 3. Написати метод екземпляра класу, який повертає список
# словників виду {"date": date} у яких date - це дата з рядка (якщо є),
# Наприклад [{"date": "1st January 1919"}, {"date": "8th February 1828"}, ...]
class Files:

    def __init__(self, my_file):
        self.my_file = my_file


    def read_file(self, my_file):
        with open(my_file, 'r') as input_file:
            domain = input_file.read().splitlines()
            dom_list = [i.replace('.', '') for i in domain]
        return dom_list

    def read_surnames(self, my_file):
        with open(my_file, 'r') as input_file:
            name = input_file.read().splitlines()
        names = [line.split('\t')[1] for line in name if line]
        return names

    def read_data(self, my_file):
        with open(my_file, 'r') as input_file:
            date = input_file.read().splitlines()
        date_list = [{'date': line.split(' - ')[0]} for line in date if line]
        return date_list

file_1 = Files('domains.txt')
print(file_1.my_file)
print(file_1.read_file('domains.txt'))
print(file_1.read_surnames('names.txt'))
print(file_1.read_data('data.txt'))


