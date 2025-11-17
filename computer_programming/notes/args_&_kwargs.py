# BHR 2nd args and kwargs notes

"""def hello(name = "Tia", age = 29):
    return f"Hello {name}! You are {age}!"

print(hello())
print(hello(age = 19, name = "Treyson"))
print(hello("Xavier"))"""

#positional arguments, *args, keyword arguments, **kwargs
def hello(*names, **last):
    for name in names:
        if name == "Vienna":
            print(f"Hello {name} {last['alast']} {last['vlast']}. ")
        else:
            print(f"Hello {name} {last['alast']}. ")

hello("Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Xavier", "Jake", alast = "LaRose", vlast = "Arkwin")







