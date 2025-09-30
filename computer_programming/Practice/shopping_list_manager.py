#BHR 2nd Shopping List Manager

shopping_list = []
while True:
    action = input("Do you want to add to(1), remove(2), or inspect(3) your list? If so, please input the respective character. If you want to leave, press 4. ")
    if action == "1":
        new_item = input("Please enter the item you are adding. ")
        shopping_list.insert(-1, new_item)
    elif action == "2":
        task = input("Which one do you want to remove? ")
        if task in shopping_list:
            shopping_list.remove(task)
            print(f"{task} has been removed. ")
        else:
            print(f"{task} not found. ")
    elif action == "3":
        if shopping_list:
            for index in shopping_list:
                print(index)
        else:
            print("There is not any items in the shopping list. ")
    elif action == "4":
        break
    else:
        print("That is an invalid input. ")

