def area(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом.")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return a * a

def perimeter(a):
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом.")
    if a < 0:
        raise ValueError("Сторона не может быть отрицательной.")
    return 4 * a
