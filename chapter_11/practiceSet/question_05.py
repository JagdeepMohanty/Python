 #Write a class vector representing a vector of n dimensions. Overload the + and * operator which calculates the sum and the dot(.) product of them.



class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, v):
        return Vector([self.values[i] + v.values[i] for i in range(len(self.values))])

    def __mul__(self, v):
        return sum(self.values[i] * v.values[i] for i in range(len(self.values)))
