#BHR 2nd caesar cipher
#set global variable
check = ""

#function for cipher
def cipher(word, shift):
    #reset the word
    new_word = ""
    #for loop checking each letter
    for letter in word:
        #if the letter isn't alphabetic
        if not letter.isalpha():
            #add the letter to the word
            new_word = new_word + letter
            #begin a new iteration of the loop
            continue
        #change the letter to a number
        letter = ord(letter)
        #check whether it is capital or not capital
        if letter <= 90 and letter >= 65:
            #increase the letter by the desired amount
            letter += shift
            #checking if it is too big
            if letter > 90:
                #bringing it down by 26
                letter -= 26
            #checking wether it is too small
            elif letter < 65:
                #bringing the letter up by 26
                letter += 26
        #checking if the letter is lowercase
        elif letter >= 97 and letter <= 122:
            #increase the letter by the desired amount
            letter += shift
            #check if the letter is too big
            if letter > 122:
                #bringing it down by 26
                letter -= 26
            #checking if the letter is too small
            elif letter < 97:
                #bringing the letter up by 26
                letter += 26
        #reset the letter to a letter instead of a number
        letter = chr(letter)
        #add the letter to a new word
        new_word = new_word + letter
    #return with the new word
    return(new_word)

#make an infinite loop
while True:
    #Check if the user wants to quit, code, or decode
    check = input('If you want to code a cipher, write "code". If you want to decode a word, write "decode". If you want to quit, write anything. ').lower().strip()
    #if they want to code
    if check == "code":
        #ask what they want to be coded
        word = input("What do you want to be coded? ")
        #ask how much do you want your word shifted?
        shift = int(input("How much do you want your word to be shifted? "))
    #otherwise if they want to decode
    elif check == "decode":
        #check what they want to be coded
        word = input("What do you want to be decoded? ")
        #ask how much do you want your word shifted?
        shift = int(input("How much do you want your word to be shifted? "))
        #make the shift negative
        shift = shift * -1
    #otherwise
    else:
        #end the loop
        break
    #making the shift so it doesn't go too big
    shift = shift % 26
    #print a statement with the old word and the new
    print(f"Your input was {word}. The output is {cipher(word, shift)}. ")