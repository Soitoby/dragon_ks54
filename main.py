import math

x = int(input("какая задача?(1 - обьем цилиндра, 2 - 2 выражения):"))
if x == 1:
    print("вычисление обьема цилиндра")
    r = int(input("радиус цилиндра(см):"))
    h = int(input("высота цилиндра(см):"))
    print("обьем цилиндра:", 3.14*(r**2)*h)
if x == 2:
    z1 = lambda b: (math.sqrt(2 * b * math.sqrt(b * 2 - 4))) / (math.sqrt(b ** 2 - 4) + b + 2)
    z2 = lambda a, b: math.sqrt((a + b) / (a - 3))
    b = int(input('введите значение b:'))
    a = int(input('введите значение a:'))
    print("уравнение z1:", z1(b))
    print("уравнение z2:", z2(a, b))
