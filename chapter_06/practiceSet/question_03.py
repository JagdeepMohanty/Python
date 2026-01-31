#A spam comment is defined as a text containing following keywords:“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

comment = input("Enter comment: ").lower() #case sensetivity se bachne ke liye 

if ("make a lot of money" in comment or
    "buy now" in comment or
    "subscribe this" in comment or
    "click this" in comment):
    print("Spam comment")
else:
    print("Not spam")


#another way

comment = input("Enter the comment: ")

spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

comment = comment.lower()

is_spam = False

for word in spam_keywords:
    if word in comment:
        is_spam = True
        break

if is_spam:
    print("This is a SPAM comment")
else:
    print("This is NOT a spam comment")