class Square():

    def __init__(self, w1, w2, w3):
        # in this example, width is used as one of the sides of a square

        self.width1 = w1
        self.width2 = w2
        self.width3 = w3

    def Volume(self):
        return self.width1 * self.width2 * self.width3


square = Square(20, 20, 20)
print(square.Volume())


class Square2():

    def __init__(self, s):
        self.side = s

    def side_area(self):
        return 6 * (self.side ** 2)


square1 = Square2(6)
print(square1.side_area())


