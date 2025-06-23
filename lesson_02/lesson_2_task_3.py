from math import ceil

def square(x):
    return ceil(x*x)

x = float(input('Введите сторону квадрата: '))

print(f'Округленная в большую сторону площадь квадрата - {square(x)}')