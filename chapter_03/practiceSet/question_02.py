 #Write a program to fill in a letter template given below with name and date

name= input("Enter the name :")
date= input("Enter the date :")

letter= "Dear" + name + "\n" + "You are selected!\n" + date 
print(letter)
print(f"Dear {name}\nYou are selected!\n{date} ")
# done