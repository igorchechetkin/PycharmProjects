import math

def calculation(radius, height):

    square_circle = math.pi * (radius ** 2)
    side = 2 * math.pi * radius * height
    full = side + 2 * square_circle

    return side, full


radius = float(input("Введите радиус: "))
height = float(input("Введите высоту: "))

side, full = calculation(radius, height)

print(f"Площадь боковой поверхности цилиндра: {round(side, 2)}")
print(f"Полная площадь цилиндра: {round(full, 2)}")
