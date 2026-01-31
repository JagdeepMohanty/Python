# Write a program to find whether a given username contains less than 10 characters or not.

user_name= input("enter username :")

userName_length= len(user_name)

if(userName_length>=10):
    print("username contains than 10 or more characters")
else:  
    print("username contains less than 10 characters")                    