from classes import Point,  Figure,  Circle,  Triangle,  Square

def main():
    point_a = Point(2, 4)
    point_b = Point(6, 11)
    point_c = Point(3, 4)
    triangle_1 = Triangle(point_a, point_b, point_c)
    print(triangle_1.triangle_S())
    print(triangle_1.triangle_P())
    print('=' * 20)
    square_1 = Square(point_a, point_b)
    print(square_1.square_S())
    print(square_1.square_P())
    print('=' * 20)
    circle_1 = Circle(point_a, 15)
    print(circle_1.circle_S())
    print(circle_1.circle_P())


if __name__ == '__main__':
    main()