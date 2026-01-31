#Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute?


class Demo:
    a = 5   

obj = Demo()
obj.a = 0   

print(obj.a)     # 0
print(Demo.a)    # 5
