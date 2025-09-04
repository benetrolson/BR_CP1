#BHR 2nd string methods notes

name = input("What is your name? ").strip().title()
first_name = name.find(" ")
sentence = "The quick brown fox jumps over the lazy dog!"
word = "brown"
length = len(word)
start = sentence.find(word)
print(sentence.replace(word, "yellow"))
print(f"Hello {name}, it is nice to meet you. ")

