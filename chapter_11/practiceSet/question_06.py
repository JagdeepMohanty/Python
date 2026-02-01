# Write __str__() method to print the vector as follows:
#  7i + 8j +10k
# Assume vector of dimension 3 for this problem


class Vector3:
    def __init__(self, i, j, k):
        self.values = [i, j, k]

    def __str__(self):
        return f"{self.values[0]}i + {self.values[1]}j + {self.values[2]}k"


v = Vector3(7, 8, 10)
print(v)
