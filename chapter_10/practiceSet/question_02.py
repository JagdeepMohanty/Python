#Write a class “Calculator” capable of finding square, cube and square root of a number

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print("Square:", self.n ** 2)

    def cube(self):
        print("Cube:", self.n ** 3)

    def square_root(self):
        print("Square Root:", self.n ** 0.5)


c = Calculator(9)
c.square()
c.cube()
c.square_root()
