#Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!


hindi_dict = {
    "paani": "water",
    "kitaab": "book",
    "kursi": "chair",
    "ladka": "boy"
}

word = input("Enter a Hindi word: ")
print("Meaning:", hindi_dict.get(word, "Word not found"))

