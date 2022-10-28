# решим задачу 2 через ООП
class HexNumber:
    def __init__(self, num):
        self.num = int(num.upper(), 16)

    def __add__(self, other):
        add_nums = self.num + other.num
        return list(hex(add_nums)[2:].upper())

    def __mul__(self, other):
        mul_nums = self.num * other.num
        return list(hex(mul_nums)[2:].upper())

hx_1 = HexNumber(input('Введите шестнадцатеричное число: '))
hx_2 = HexNumber(input('Введите шестнадцатеричное число: '))
print(hx_1 + hx_2)
print(hx_1 * hx_2)

