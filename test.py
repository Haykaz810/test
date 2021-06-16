import sys
class All:
    def __init__(self, length):
        self.length = length

    def test(self):
        if 2 <= len(self.length) < 5:
            return self.length
        else:
            sys.exit("I do not know what is this")


class Rectangle(All):
    def __init__(self, length):
        super().__init__(length)

    def area(self):
        num = super().test()
        if len(num) == 3:
                if self.length[0] + self.length[1] >= self.length[2] and \
                         self.length[0] + self.length[2] >= self.length[1] \
                        and self.length[1] + self.length[2] >= self.length[0]:
                         return "Triangle"


class Square(All):
    def __init__(self, length):
        super().__init__(length)

    def fish(self):
        if len(super().test()) == 4:
            return "this is Painting"


list = [1, 2, 3, 4]
square = Square(list)
painting = Rectangle(list)
print(painting.area())
print(square.fish())