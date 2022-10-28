# решим задачу 2 через collections, не использую функцию hex()

from collections import defaultdict
num_1_16 = input('введите первое шестнадцатеричное число: ')
num_2_16 = input('введите второе шестнадцатеричное число: ')

def list_num(num):
    result = []
    for i in num:
        result.append(i)
    return result

nums = [('0', 0), ('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8),
        ('9', 9), ('A', 10), ('B', 11), ('C', 12), ('D', 13), ('E', 14), ('F', 15)]
dict_nums = defaultdict(list)
for k, v in nums:
    dict_nums[k].append(v)
# Функция по переводу шестнацатеричное число в десятиричное
def convert_from_16_to_10(my_list):
    out = 0
    for i in range(len(my_list)):
        res = dict_nums[list(reversed(my_list))[i]][0]
        out += res * 16 ** i
    return out
# Рекурсия по переводу десятиричного числа в шестнадцатеричное
def convert_from_10_to_16(num, result = ''):
    if num == 0:
        return list(reversed(result))
    else:
        elem = num % 16
        next_num = num // 16
        for k, v in dict_nums.items():
            if v[0] == elem:
                return convert_from_10_to_16(next_num, result=result + k)

list_1_16 = list_num(num_1_16)
list_2_16 = list_num(num_2_16)
num_1_10 = convert_from_16_to_10(list_1_16)
num_2_10 = convert_from_16_to_10(list_2_16)
print(convert_from_10_to_16(num_1_10 + num_2_10))
print(convert_from_10_to_16(num_1_10 * num_2_10))


