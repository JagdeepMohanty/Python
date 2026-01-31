#Write a python function to remove a given word from a list ad strip it at the same time.

def remove_and_strip(word_list, word):
    new_list = []
    for item in word_list:
        if item.strip() != word:
            new_list.append(item.strip())
    return new_list

l = ["  Harry ", " Rahul ", "  Aman ", "Harry  "]
print(remove_and_strip(l, "Harry"))

