#Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def speak(self):
        print("Animal makes a sound")


class Pets(Animals):
    def friendly(self):
        print("Pet is friendly")


class Dog(Pets):
    def bark(self):
        print("Dog barks: Woof Woof")


d = Dog()
d.speak()    #Animal makes a sound
d.friendly()   #Pet is friendly
d.bark()  #Dog barks: Woof Woof