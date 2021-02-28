from math import pi

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError


class Figure:
    def __init__(self, point_a):
        self.point_a = point_a


class Circle(Figure):
    def __init__(self, point_a, r):
        super().__init__(point_a)
        self.r = r

    def circle_S(self):
        return pi * self.r ** 2

    def circle_P(self):
        return 2 * pi * self.r


class Triangle(Figure):
    def __init__(self, point_a, point_b, point_c):
        super().__init__(point_a)
        self.point_b = point_b
        self.point_c = point_c

    def triangle_S(self):
        vector_ab = ((self.point_a[0] - self.point_b[0]) ** 2 + (self.point_a[1] - self.point_b[1]) ** 2) ** 0.5
        vector_ac = ((self.point_a[0] - self.point_c[0]) ** 2 + (self.point_a[1] - self.point_c[1]) ** 2) ** 0.5
        vector_cb = ((self.point_c[0] - self.point_b[0]) ** 2 + (self.point_c[1] - self.point_b[1]) ** 2) ** 0.5
        return (vector_ab + vector_ac + vector_cb) * 0.5

    def triangle_P(self):
        vector_ab = ((self.point_a[0] - self.point_b[0]) ** 2 + (self.point_a[1] - self.point_b[1]) ** 2) ** 0.5
        vector_ac = ((self.point_a[0] - self.point_c[0]) ** 2 + (self.point_a[1] - self.point_c[1]) ** 2) ** 0.5
        vector_cb = ((self.point_c[0] - self.point_b[0]) ** 2 + (self.point_c[1] - self.point_b[1]) ** 2) ** 0.5
        return vector_ab + vector_ac + vector_cb


class Square(Figure):
    def __init__(self, point_a, point_b):
        super().__init__(point_a)
        self.point_b = point_b

    def square_S(self):
        vector_ab = ((self.point_a[0] - self.point_b[0]) ** 2 + (self.point_a[1] - self.point_b[1]) ** 2) ** 0.5
        return vector_ab ** 2

    def square_P(self):
        vector_ab = ((self.point_a[0] - self.point_b[0]) ** 2 + (self.point_a[1] - self.point_b[1]) ** 2) ** 0.5
        return vector_ab * 4