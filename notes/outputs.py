#BHR 2nd format outputs notes

name = "Eric"
age = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
grade = .75
money = 25

print("Hello {}, nice to meet you! You are {:,}, that is really old! You have a {:%} in this class. You have ${:.2f}, that is a lot of money! ".format(name, age, grade, money))

print(f"Hello {name}, nice to meet you! You are {age:,}, that is really old! You have a {grade:%} in this class. You have ${money:.2f}, that is a lot of money! ")
