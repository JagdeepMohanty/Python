# Override the __len__() method on vector of problem 5 to display the dimension of the vector

class Vector:
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)


v = Vector([1, 2, 3, 4])
print(len(v))
