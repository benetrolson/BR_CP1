#BHR 2nd flexible calculator

#function that accepts the numbers and whether they want to do a sum, an average, a min, a max, or a product
def claculator(check, *nums):
    #reset the total
    total = 0
    #if they want to do a sum
    if check == "sum":
        #for every number
        for num in nums:
            if isinstance(num, list):
                for number in num:
                    total += number
            elif isinstance(num, float):
                #add them to the total
                total += num
    #otherwise if they want to do an average
    elif check == "average":
        length = 0
        #for every number
        for num in nums:
            if isinstance(num, list):
                for number in num:
                    #add it to the total
                    total += number
                    length += 1
            elif isinstance(num, float):
                total += num
                length += 1
        #divide the total by the amount of numbers
        total /= length
    #otherwise if they want to do a min
    elif check == "min":
        #for every number
        for num in nums:
            if isinstance(num, list):
                for number in num:
                    if number < total:
                        total = number
            elif isinstance(num, float):
                #if the number before was smaller
                if num < total:
                    #change the total to the smaller number
                    total = num
    #otherwise if they want to do a max
    elif check == "max":
        #for every number
        for num in nums:
            if isinstance(num, list):
                for number in num:
                    if number > total:
                        total = number
            elif isinstance(num, float):
                #if the number before was bigger
                if num > total:
                    #change the total to the bigger number
                    total = num
    #otherwise if they want to do a product
    elif check == "product":
        #reset the total to 1
        total = 1
        #for every number
        for num in nums:
            if isinstance(num, list):
                for number in num:
                    total *= number
            elif isinstance(num, float):
                #multiply it by the total
                total *= num
    #otherwise
    else:
        #change the total to a string that says invalid input
        total = "invalid"
    return(total)

#infinite loop
while True:
    #reset the list of numbers
    nums = []
    ask = input("Do you want to use the same numbers? If so, write 'yes'. ").lower()
    #infinite loop
    while True:
        if ask == "yes":
            break
        #ask for a new number
        num = input("What number do you want to your list? Once you are done, write 'done'. ")
        #check if it is possible to change it to an integer or a float
        if num.isdigit():
            #if it is, change it to an integer or a float
            num = float(num)
            #add it to the list of numbers
            nums.append(num)
        #if they want to leave
        if num == "done":
            #end the loop
            break
    #ask them what they want to do: a sum or a min or an average or a max or a product
    check = input("Which computation do you want to do? A sum, an average, a min, a max, or a product? ").lower()
    #run the function
    print(f"The {check} is {claculator(check, nums)}. ")
    #check if they want to quit
    check = input("If you want to quit, write 'quit'. ").lower()
    #if they want to quit
    if check == "quit":
        #end the loop
        break




