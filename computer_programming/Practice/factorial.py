#BHR 2nd factorial

#def function multiply (num)
def multiply(num):
    #num2 = num1
    num2 = num - 1
    #while num2 > 0
    while num2 > 0:
        #num *= num2
        num *= num2
        #num2 -= 1
        num2 -= 1
    #return num
    return(num)

#while loop
while True:
    #user input number as num
    num = input("Please input a whole number to find the factorial. ")
    #if user input is not digit
    if not num.isdigit():
        #tell them they are wrong
        print("Invalid input. Please try again. ")
    #if the user input is a float
    elif not num.isdecimal():#I had to change this to an else if statement
        #tell them they are wrong
        print("Invalid input. Please try again. ")
    #otherwise
    else:
        num = int(num)#I had to change the number into an integer
        #break out of the loop
        break

#call the function
result = multiply(num)#I had to add something to recieve the info
#print the number the user inputed and then the result
print(f"The factorial of {num} is {result}. ")
