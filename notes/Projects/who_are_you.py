# BHR 2nd Who are you
name = input("Howdy. My name is George. What's your name? ")
age = int(input("Nice to meet you. Say, how old are you?(please just answer with a number, not written out)"))
if age >= 18:
    color = input("You are very old. What is your favorite color? ")
else:
    color = input("You are really young. What is your favorite color? ")
print("So ", name, ",you are ", age, "years old, and your favorite color is ", color, ". That is a rather disgusting color, by the way. Bye. ")
