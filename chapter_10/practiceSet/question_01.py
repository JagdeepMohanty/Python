#Create a class “Programmer” for storing information of few programmers working at Microsoft.

class Programmer:
    def __init__(self, name, language, experience):
        self.name = name
        self.language = language
        self.experience = experience

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Language: {self.language}")
        print(f"Experience: {self.experience} years")


p1 = Programmer("Amit", "Python", 3)
p2 = Programmer("Rahul", "Java", 5)

p1.get_info()
print()
p2.get_info()
