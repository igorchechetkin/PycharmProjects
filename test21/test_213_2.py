# Задача 2. Непонятно!
# Друг никак не может понять эту тему с изменяемыми и неизменяемыми типами, ссылками, объектами и их id.
# Видя, как он мучается, вы решили помочь ему и объяснить эту тему наглядно.
#
# Пользователь вводит любой объект. Напишите программу, которая выводит на экран тип введённых данных,
# информацию о его изменяемости, а также id этого объекта.
#
# Пример 1:
#
# Введите данные: привет
#
# Тип данных: str (строка)
#
# Неизменяемый (immutable)
#
# Id объекта: 1705156583984
#
# Пример 2:
#
# Введите данные: {‘a’: 10, ‘b’: 20}
#
# Тип данных: dict (словарь)
#
# Изменяемый (mutable)
#
# Id объекта: 1705205308536

def check_data(data):

    type_of_data = type(data)
    name_of_data = ""

    if str(type_of_data) in data_names_dict:
        name_of_data = data_names_dict[str(type_of_data)]

    if name_of_data[1] in mutable_check_helper["mutable"]:
        property_of_data = "Изменяемый (mutable)"

    else:
        property_of_data = "Неизменяемый (immutable)"

    print(f"Тип данных: {name_of_data[0]} ({name_of_data[1]})")
    print(f"{property_of_data}")
    print(f"Id объекта: {id(data)}")


data_names_dict = {
    "<class 'str'>": ["str", "строка"],
    "<class 'dict'>": ["dict", "словарь"],
    "<class 'list'>": ["list", "список"],
    "<class 'set'>": ["set", "множество"],
    "<class 'int'>": ["int", "число"]
}

mutable_check_helper = {
    "mutable": ("словарь", "список", "множество")
}

some_data = ["int", "число"]

check_data(some_data)
