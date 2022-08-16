class Rec:
    def __init__(self, l, w):
        self.l = l
        self.w = w


class Rectan(Rec):
    def perimeter(self):
        print(2 * (self.l + self.w))

    def area(self):
        print(self.l * self.w)


ob = Rectan(2, 2)
ob.perimeter()
ob.area()


class Circle:
    def __init__(self, r):
        self.r = r


class Cir(Circle):
    def perimeter(self):
        print(2 * 3.14 * self.r)

    def area(self):
        print(3.14 * self.r * self.r)


ob = Cir(4)
ob.perimeter()
ob.area()


class Triangle:
    def __init__(self, base, s1, s2, h):
        self.base = base
        self.s1 = s1
        self.s2 = s2
        self.h = h


class Tri(Triangle):
    def perimeter(self):
        print(self.base + self.s1 + self.s2)

    def area(self):
        print(0.5 * self.base * self.h)


ob = Cir(3)
ob.perimeter()
ob.area()