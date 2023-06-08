# Всі пункти є частиною одного завдання, тому можна використовувати функції кілька разів та не дублювати код.
# Якщо хочете, можете використовувати дефолтні значення та анотацію типів.
#
# 1. Написати функцію, яка отримує один параметр - ім'я директорії та повертає словник виду
# {'filenames': [список файлів у папці], 'dirnames': [список усіх підпапок у папці]}.
# Підпапки враховувати лише першого рівня вкладення. Папка в папці в папці - таке не брати))
import os

def file_dict(folder=r'E:\pythonProject2\Lesson11A') -> dict:
    allfiles = os.listdir(folder)
    folders = []
    files = []
    for i in allfiles:
        obj_path = os.path.join(folder, i)
        if os.path.isdir(obj_path):
            folders.append(i)
        elif os.path.isfile(obj_path):
            files.append(i)
        else:
            pass
    dictionary = {'filenames': files, 'dirnames': folders}
    return dictionary

print(file_dict(folder=r'E:\pythonProject2\Lesson11A'))

# 2. Написати функцію, яка отримує два параметри – словник, описаний у пункті 1
# і значення булю (True/False) - можна зробити за замовчуванням.
# Функція повертає той самий словник, але з відсортованими іменами файлів та папок у відповідних списках.
# Булеве значення True означає, що порядок сортування алфавітний, False – зворотний порядок.

def sort_dict(allfiles: dict, without_reverse=True):
    for key in allfiles:
        allfiles[key].sort(reverse = not without_reverse)
    return allfiles
file_objects = file_dict((r'E:\pythonProject2\Lesson11A'))
print(sort_dict(file_objects, False))
# 3. Написати функцію, яка отримує два параметри - словник, описаний у пункті 1 та рядок, який може бути
# або ім'ям файлу, або ім'ям папки. (У імені файлу має бути точка).
# Залежно від того, що функція отримала (ім'я файлу або ім'я папки) – записати його у відповідний список
# та повернути оновлений словник.
def file_folder(allfiles: dict, string: str):
    key = "dirnames"
    if "." in string:
        key = "filenames"
    allfiles[key].append(string)
    return allfiles
file_objects = file_dict((r'E:\pythonProject2\Lesson11A'))
print(file_folder(file_objects, "jyfg.png"))


