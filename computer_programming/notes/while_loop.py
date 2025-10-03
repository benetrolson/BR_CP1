# BHR 2nd While Loops Notes
import time
import random

num = 0
break_point = random.randint(1,40)
while num < 20:
    num += 1 #fixed my loop. 
    if num == break_point:
        break
    elif num%2 != 0:
        continue
    print(num)
    time.sleep(0.01)
else:
    print("This loop exited by meeting the condition! ")

print("The loop is over. ")
