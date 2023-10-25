# https://www.notion.so/Python-0053f6da788f4b8e9b141213935df3aa
# # my_number = 10
# print(id(my_number))
# # 140730756817992


# my_string = 'abc'
# print(id(my_string))
# # 140730755452704

# Многострочная строка
# info_msg = """YOu
# fd
# dfgd
# gdg
# d"""
# print(info_msg)

# # Встроенные функции и строки
# my_name = 'Sema'
# print(len(my_name))
# # 4
# print(my_name[0])
# # S
# print(my_name[2:4])
# # ma

# # Методы строк
# my_name = 'This is my short comment'
# print(my_name.upper())
# print(my_name.replace('short', 'long'))
# print(my_name.count('is'))
# print(my_name.index('s'))
# print(my_name.capitalize())
# print(my_name.lower())

# # Конвертация строки в число
# user_input = input("Enter any number: ")
# any_num = int(user_input)
# print(any_num)
# Или так
# any_num = int(input("Enter any number: "))
# print(any_num)

# # Возведение в степень
# base = 5
# power = 3
# print(pow(base, power))

# #float
# average_price = '14.5'
# tem = float(average_price)
# print(tem)

# # complex комплексныек числа
# complex_a = 3 + 5j
# complex_b = 4 + 7j
# sum = complex_a + complex_b
# print(sum)
# # (7+12j)

# #Логический тип
# db_is_available = False

# # Конвертация типов
# int_num = 5
# float_num = 4.5
# print(int_num + float_num)
# # 9.5

# bool_val = True
# int_val = 7
# print(int_val + bool_val)
# # 8

# int_num = 50
# str_val = 'abc'
# print(str_val * int_num)

# #удаление элемента del
# user_inputs = [1, 2, 3, 4, 5]
# del user_inputs[1]
# print(user_inputs)
# print(len(user_inputs))

# # Список словарей
# users = [
#     {
#         'users_id': 134,
#         'user_name': 'Alice'
#     },
#     {
#         'users_id': 831,
#         'user_name': 'Bob'
#     }
# ]
# print(len(users))
# print(users[1]['users_id'])

# # переменные
# my_fruit = 'apple'
# other_fruit = 'banana'
# new_fruit = 'lime'

# all_fruits = [my_fruit, other_fruit, new_fruit]
# print(all_fruits)
# # пайтон автоматом достанет значения из переменных

# # Методы списков
# append('') - добавлять в конец списка
# pop() - удаление с конца если пустой
# удалённый элемент можно записать в переменную
# pop и append мутируют исходник

# remove
# insert

# sort()-сортировка
# posts_ids.sort(reverse=True)(в обратку порядок)

# index
# clear
# copy
# extend
# reverse
# count

# # Конвертация в список
# greet = "Hello world"
# greet_letters = list(greet)
# print(greet_letters)
# # ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# # Арифметические операции в списках
# rat = [2.5, 5.0, 4.3, 3.7]
# print(min(rat))
# # 2.5

# # Объединение списков

# my_r = [2.5, 5.0]
# ot_r = [3.7, 4.5, 4.9]
# all_r = my_r+ot_r
# print(all_r)
# # [2.5, 5.0, 3.7, 4.5, 4.9]

# # Нарезка   списков

# rat = [1, 2, 3, 4, 5]
# rat_two = rat[:2]
# print(rat_two)  # [1,2]
# rat_thr = rat[1:-1]
# print(rat_thr)  # [2, 3, 4]
# rat_fr = rat[-2:] (два последних)
# print(rat_fr)  # [4, 5]

# копирование списка
# my_cars = ['BMW', 'Mercedes']
# new_my = my_cars[:]
# new_my.append('audi')
# print(new_my)
# #['BMW', 'Mercedes', 'audi']
# print(my_cars)
# #['BMW', 'Mercedes']

# копирование списка
# my_cars = ['BMW', 'Mercedes']
# new_my = my_cars.copy()
# new_my.append('audi')
# print(new_my)
# # ['BMW', 'Mercedes', 'audi']
# print(my_cars)
# # ['BMW', 'Mercedes']

# # копирование списка
# my_cars = ['BMW', 'Mercedes']
# new_my = list(my_cars)
# new_my.append('audi')
# print(new_my)
# # ['BMW', 'Mercedes', 'audi']
# print(my_cars)
# # ['BMW', 'Mercedes']

# вставка insert
# my_nums = [1, 2, 3, 4, 5, 6, 7]
# my_nums.insert(2, 5)
# print(my_nums)

# extend()
# my_nums = [1, 2, 3, 4, 5, 6, 7]
# my_nums.extend('abc')
# print(my_nums)
# # [1, 2, 3, 4, 5, 6, 7, 'a', 'b', 'c']

# practic 1
# my_list = [True, 1, 1.5, 'Ivan', {'name': 'Ivan'}]
# print(my_list)
# my_list2 = my_list.pop(3)
# my_list.reverse()
# print(my_list)
# my_list3 = my_list[:2].copy()
# print(my_list3)
# my_list.extend(my_list3)
# print(my_list)

# practic 2
# my_list = [10, 20, 30, 40, 50]
# my_list2 = [1, 2, 3, 4, 5]
# my_list3 = my_list+my_list2
# print(my_list3)

# Словари
# my_motorbike = {
#     'brand': 'Ducati',
#     'price': 25000,
#     'engine_vol': 1.2,
# }
# print(my_motorbike['brand'])
# # Ducati

# # добавление нового ключа
# my_motorbike['is_new'] = True

# # удаление ключа
# del my_motorbike['engine_vol']
# #переменная ключ
# key_name = 'brand'
# my_motorbike[key_name] = 'BMW'  # перезапишет ключ

# Вложенные словари
# my_motorbike = {
#     'brand': 'Ducati',
#     'engine_vol': 1.2,
#     'price_info': {
#         'price': 25000,
#         'is_available': True
#     }
# }
# print(my_motorbike['price_info']['price'])
# #25000

# переменные как значение
# brand = 'Ducati'
# bike_price = 25000
# engine_volume = 1.2
# my_motorbike = {
#     'brand': brand,
#     'engine_vol': engine_volume,
#     'price': bike_price,
# }
# print(my_motorbike)

# .items()
# my_disk = {}
# my_disk['price'] = 80
# my_disk['brand'] = 'Samsa'
# print(my_disk.items())
# # dict_items([('price', 80)(кортедж), ('brand', 'Samsa')])

# .keys() список ключей
# чтобы изменить класс  на список list(my_disk.keys())

# Копирование словаря
# my_disk = {}
# my_disk['price'] = 80
# my_disk['brand'] = 'Samsa'
# new_disk = my_disk.copy()
# print(new_disk)

# Создание словаря из других типов, например из списка
# my_list = [['first', 0], ['second', True]]
# my_dict = dict(my_list)
# print(my_dict)
# конвертирует списки в словарь

# Practic 3

# my_dict = dict()
# first_key = input('Введдите имя 1-го ключа: ')
# first_key_value = input('Ввведите значение 1-го ключа: ')
# second_key = input('Введдите имя 2-го ключа: ')
# second_key_value = input('Ввведите значение 2-го ключа: ')
# third_key = input('Введдите имя 3-го ключа: ')
# third_key_value = input('Ввведите значение 3-го ключа: ')
# my_dict = {
#     first_key: first_key_value,
#     second_key: second_key_value,
#     third_key: third_key_value,
# }
# print(my_dict)

# Кортежи
# my_nums = (10, 5, 100, 0)
# print(type(my_nums))

# Кортеж словарей
# users = (
#     {
#         'user_id': 134,
#         'user_name': 'Alice'},
#     {
#         'user_id': 831,
#         'user_name': 'Bob'
#     }
# )
# print(users[1]['user_id'])
# #831
# users[1]['user_id'] = 100
# print(users[1]['user_id'])
# #100

# Методы кортежей
# Их всего 2
# count и index счет и индекс элемента

# если нужно изменить кортеж
# то переводим его в список
# и затем меняем
# потом обратно инвертируем в кортеж
# posts_ids = (151, 245)
# posts_ids_list = list(posts_ids)
# posts_ids_list.append(351)
# print(posts_ids_list)
# #[151, 245, 351]
# posts_ids_tuple = tuple(posts_ids_list)
# print(posts_ids_tuple)
# #(151, 245, 351)

# Наборы (SET)
# my_fruits = {'apple', 'banana', 'lime'}

# В наборы нельзя добавлять list, dict,set
# my_set = {10, 5, 10, 15, 15}
# print(my_set)

# новый набор
# my_set = set()

# Методы наборов
# add, union, remove, difference, intersection,discard,clear,copy
# update,issubset, issuperset, pop

# # add(добавление)
# photo_sizes = {'1920x1080'}
# photo_sizes.add('1024x768')
# print(photo_sizes)

# # union (обьединение наборов)
# other_sizes = {'800x600', '1024x768', '100x100'}
# all_sizes = photo_sizes | other_sizes
# print(all_sizes)

# # intersection (перессечения )
# photo_s = {'1920x1080', '800x600'}
# other_s = {'800x600', '1024x768'}
# common_s = photo_s.intersection(other_s)
# print(common_s)
# #{'800x600'}

# Проверка включен ли один набор в другой
# nums = {10, 5, 35}
# other_nums = {20, 5, 12, 10, 35}
# res = nums.issubset(other_nums)
# print(res)
# True

# issuperset
# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'f', 'd'}
# print(my_set.issuperset(other_set))
# #True

# difference (покажет элементы которые различают наборы)
# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'f', 'd'}
# print(my_set.difference(other_set))
# {'y', 'abc'}

# Удаления элементов из множества Set
# discard (удалить)
# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}
# print(my_set.discard('d'))
# print(my_set)

# remove(удалить)
# my_set = {'abc', 'd', 'f', 'y'}
# other_set = {'a', 'f', 'd'}
# print(my_set.remove('d'))
# print(my_set)

# copy(копировать)
# my_set = {'a', 'b', 'c', 'd'}
# copied_set = my_set.copy()
# my_set.add('t')
# copied_set.add('l')
# print(my_set)
# print(copied_set)
# print(my_set & copied_set)

# Симметричная разница в наборах
# symmetric_difference()
# my_set = {'a', 'b', 'c', 'd'}
# copied_set = my_set.copy()
# my_set.add('t')
# copied_set.add('l')
# print(my_set.symmetric_difference(copied_set))

# a = {'a', 'b', 'c', 'x'}
# b = {'a', 'b', 'c', 'z'}
# print((a | b)-(a & b))
# объединили два набора и
# от объединения отняли пересечение двух наборов

# Диапазоны RANGE
# my_range = range(7)
# print(my_range)
# #range(0, 7)
# print(list(my_range))
# #[0, 1, 2, 3, 4, 5, 6]

# Добавление шага в Диапазонах
# my_range = range(10, 20, 3) (от:до:шаг)

# Индексы в диапазонах есть
# использование в циклах
# my_range = range(10, 20, 3)
# for n in my_range: #итерация по диапазону
#     print(n)

# методы range( )
# my_range = range(5)
# print(dir(my_range))

# Встроенная функция ZIP
# склеивает 2 списка и получается типо список с кортежами
# fr = ['a', 'b', 'c']
# qa = [1, 2, 3]
# fr_qa_zip = zip(fr, qa)
# fr_qa_list = list(fr_qa_zip)
# print(fr_qa_list)
# #[('a', 1), ('b', 2), ('c', 3)]

# Конвертация zip в dict создаст словарь
# fr = ['a', 'b', 'c']
# qa = [1, 2, 3]
# fr_qa_zip = zip(fr, qa)
# fr_qa_dict = dict(fr_qa_zip)
# print(fr_qa_dict)

# Изменение в объектах python

# Глубокое копирование
# from copy import deepcopy
# info = {
#     'a': 'a1',
#     'b': True,
#     'rev': []
# }
# inf_dpc = deepcopy(info)
# inf_dpc['rev'].append('Great')

# print(info)
# #{'a': 'a1', 'b': True, 'rev': []}
# print(inf_dpc)
# #{'a': 'a1', 'b': True, 'rev': ['Great']}
