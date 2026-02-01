#Create a class (2-D vector) and use it to create another class representing a 3-D vector.

class Vector2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"{self.i}i + {self.j}j")


class Vector3D(Vector2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")


v = Vector3D(2, 3, 4)
v.show()     #2i + 3j + 4k
