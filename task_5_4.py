from collections import OrderedDict
from random import randint
from timeit import timeit
common_list = [i * randint(100, 1000) for i in range(1000)]
dict_1 = {}
dict_2 = OrderedDict()

#Функция наполнения словаря
def add_dict(dict):
    for i in common_list:
        dict[str(i)] = i
    return dict
#Функция получения элементов словаря
def get_items(dict):
    return dict.items()

#Функции по перемещению заданного элемента(number) в конец словаря

def move_to_end_dict(dict, number: int):
    key = list(dict.keys())[number]
    val = dict.pop(key)
    dict.update([(key, val)])
    return dict

def move_to_end_orderdict(dict, number: int):
    dict.move_to_end(list(dict.keys())[number])
    return dict


print(timeit("add_dict(dict_1)", globals=globals(), number=1000))                            # 0.330756087
print(timeit("add_dict(dict_2)", globals=globals(), number=1000))                            # 0.32394604000000005
print(timeit("get_items(add_dict(dict_1))", globals=globals(), number=1000))                 # 0.44792763599999996
print(timeit("get_items(add_dict(dict_2))", globals=globals(), number=1000))                 # 0.42624043300000003
print(timeit("add_dict(dict_1).popitem()", globals=globals(), number=1000))                  # 0.35477234700000015
print(timeit("add_dict(dict_2).popitem(last=True)", globals=globals(), number=1000))         # 0.33578201499999993
print(timeit("move_to_end_dict(add_dict(dict_1), 5)", globals=globals(), number=1000))       # 0.32068271300000006
print(timeit("move_to_end_orderdict(add_dict(dict_2), 5)", globals=globals(), number=1000))  # 0.7664249760000001

"""
Замер времени по исполненю кода по наполнению и извлечению элементов у обычного словаря и OrdereDict 
примерно одинаковое. Перемещение элемента в конец словаря при помощи втсроенного метода OrdereDict происходит в два 
раза медленне, чем методы pop и update у обычного словаря, но запись у OrdereDict получилась более лаконичная.
Можно сделать вывод, что нет смысла использовать OrdereDict в Phyton версияз 3.6. и выше.
"""
