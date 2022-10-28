from collections import deque
from timeit import timeit

list_1 = [i for i in range(1000)]
deque_obj = deque(range(1000))
list_2 = [1, 'a', 2, 'b', 3, 'd']

print(timeit('list_1', globals=globals(), number=100000))      # 0.005647099984344095
print(timeit('deque_obj', globals=globals(), number=100000))   # 0.00054580002732465565

def simple_append(arr):
    for i in range(100):
        if i % 2 == 0:
            arr.append(i)
            return arr

print(timeit('simple_append(list_1)', globals=globals(), number=100000))      # 0.008138099976349622
print(timeit('simple_append(deque_obj)', globals=globals(), number=100000))   # 0.008142100006807595

def simple_pop(arr):
    arr.pop()
    return arr

print(timeit('simple_pop(list_1)', globals=globals(), number=100000))          # 0.003113799961283803
print(timeit('simple_pop(deque_obj)', globals=globals(), number=100000))       # 0.0031893999548628926

def simple_extend(arr):
    arr.extend(list_2)
    return arr

print(timeit('simple_extend(list_1)', globals=globals(), number=100000))          # 0.02556670003104955
print(timeit('simple_extend(deque_obj)', globals=globals(), number=100000))       # 0.012661899963859469
"""
Замеры показали, что создание списка(list) и очереди(deque) происходит примерно за одинаковое время. Методы 
append и pop у списка и очереди тоже выполняются примерно за одинаковое время, а метод extend у очереди 
выполняется примерно в 1,5 - 2 раза быстрее, чем у списка.   
"""

def append_left_list(arr):
    for i in range(100):
        if i % 2 != 0:
            arr.insert(0, i)
            return arr

def append_left_deque(arr):
    for i in range(100):
        if i % 2 != 0:
            arr.appendleft(i)
            return arr

print(timeit('append_left_list(list_1)', globals=globals(), number=1000))          # 6.973258199985139
print(timeit('append_left_deque(deque_obj)', globals=globals(), number=1000))       # 0.001110500015784055

def pop_left_list(arr):
    arr.pop(0)
    return arr

def pop_left_deque(arr):
    arr.popleft()
    return arr

print(timeit('pop_left_list(list_1)', globals=globals(), number=1000))          # 5.9158060000045225
print(timeit('pop_left_deque(deque_obj)', globals=globals(), number=1000))      # 0.0003288000007160008

def extend_left_list(arr):
    for i in reversed(list_2):
        arr.insert(0, i)
    return arr

def extend_left_deque(arr):
    arr.extendleft(list_2)
    return arr

print(timeit('extend_left_list(list_1)', globals=globals(), number=100))          # 0.0013124000000743763
print(timeit('extend_left_deque(deque_obj)', globals=globals(), number=100))      # 0.0008732999999665481

"""
Замер времени показал, что методы appendleft, popleft b extendleft у deque в разы быстрее работают аналогичным 
функциям у списка.
"""

def get_elem_list(arr, number):
    list_3 = arr[: number + 1]
    return list_3.pop()

def get_elem_deque(deq, number):
    deq_1 = deque()
    for i in range(len(deq)):
        if i < number + 1:
            deq_1.append(deq[i])
    return deq_1.pop()


print(timeit('get_elem_list(list_1, 2)', globals=globals(), number=1000))       # 0.0005799000000479282
print(timeit('get_elem_deque(deque_obj, 6)', globals=globals(), number=1000))   # 0.14135540000006586

"""
Замер времени показал, что получение рандомного элемента из списка происходит значительно(в разы) быстрее, чем
у deque. Можно сделать вывод, что, если нам нужно произвести какие-либо действия с началом или концом массива, то 
лучше использовать deque. Если предстоит работать со случайными элементами массива, то лучше использовать обычный 
список.
"""


