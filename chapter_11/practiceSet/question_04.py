#Write a class ‘Complex’ to represent complex numbers, along with overloaded operators ‘+’ and ‘*’ which adds and multiplies them.


class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, c):
        return Complex(self.real + c.real, self.imag + c.imag)

    def __mul__(self, c):
        real = self.real * c.real - self.imag * c.imag
        imag = self.real * c.imag + self.imag * c.real
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


c1 = Complex(2, 3)
c2 = Complex(1, 4)

print(c1 + c2)
print(c1 * c2)
