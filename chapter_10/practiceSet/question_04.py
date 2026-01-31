#Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(self.n ** 2)

    @staticmethod
    def greet():
        print("Hello! Welcome to Calculator")


Calculator.greet()
