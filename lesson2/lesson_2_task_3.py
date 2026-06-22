import math


def square(side):
    """Возвращает площадь квадрата, округляя вверх при необходимости."""
    area = side * side
    return math.ceil(area)


# Примеры:
print(square(5))    # 25
print(square(2.5))  # 6.25 -> округляем до 7
