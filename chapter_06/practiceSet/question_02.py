 # Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

maths = int(input("Enter marks of maths: "))
english = int(input("Enter marks of english: "))
science = int(input("Enter marks of science: "))

total = maths + english + science
percentage = (total / 300) * 100

if maths >= 33 and english >= 33 and science >= 33 and percentage >= 40:
    print("Student has PASSED")
else:
    print("Student has FAILED")
