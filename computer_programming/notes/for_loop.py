# BHR 2nd for loop notes

import time

nums = [6, 51, 61, 94, 351, 946, 5489, 4, 654, 684]

for num in nums:
    div = num/2
    if div > 100:
        print(f"{div} is half of {num}. It is still a large number! ")
    else:
        print(num)
print("We have completed all the numbers. ")
time.sleep(2)
for x in range(1, 10):
    print(x)
time.sleep(2)
print("Count by 2! ")

for x in range(2, 11, 2):
    print(x)
time.sleep(2)
print("Count Down! ")
time.sleep(1)
for x in range(10, 0, -1):
    print(x)
    time.sleep(1)
print("Let's eat some cheese! ")









