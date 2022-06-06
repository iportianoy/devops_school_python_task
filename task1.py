from dataclasses import dataclass


@dataclass
class Triangle:
    a: int
    b: int
    c: int


def read_data() -> Triangle:
    sides_names = ['a', 'b', 'c']
    sides = []
    for side_name in sides_names:
        side = None
        while not side:
            try:
                side = int(input(f"Enter integer for side {side_name}: \n"))
            except ValueError:
                print('Side must be integer! Try again!')

        sides.append(side)

    return Triangle(*sides)


def check_triangle(triangle: Triangle) -> bool:
    a, b, c = triangle.a, triangle.b, triangle.c
    return all([
        a + b > c,
        a + c > b,
        c + b > a
    ])


def guess_triangle_type(triangle: Triangle) -> str:
    a, b, c = triangle.a, triangle.b, triangle.c
    if a == b == c:
        return 'Рівносторонній'
    if any([
        a == b,
        a == c,
        b == c
    ]):
        return 'Рівнобедренний'
    if any([
        a**2 + b**2 == c**2,
        a**2 + c**2 == b**2,
        b**2 + c**2 == a**2,
    ]):
        return 'Прямокутний'

    return 'Різносторонній'


def triangle_checker() -> None:
    triangle: Triangle = read_data()
    if not check_triangle(triangle):
        print('Sides are incorrect')
        exit()

    print('Sides are correct')
    triangle_type = guess_triangle_type(triangle)
    print(f'Type: {triangle_type}')
    exit()


if __name__ == '__main__':
    triangle_checker()
