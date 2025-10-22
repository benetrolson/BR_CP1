#BHR 2nd caesar cipher
#set global variable
check = ""

#function for cipher
def cipher(word, ciph, new_word):
    #if they want to decode the word
    if check == "decode":
        #change the cipher to negative
        ciph * -1
    #for loop checking each letter
    for letters in word:
        #change the letter to a number
        letter = ord(letters)
        #check whether it is capital or not capital
        if letter >= 65 and letter <= 90:
            #increase the letter by the desired amount
            letter += ciph
            #checking if it is too big
            if letter <= 90:
                #bringing it down by 26
                letter -= 26
            #checking wether it is too small
            elif letter >= 65:
                #bringing the letter up by 26
                letter += 26
        #checking if the letter is lowercase
        elif letter >= 97 and letter <= 122:
            #increase the letter by the desired amount
            letter += ciph
            #check if the letter is too big
            if letter <= 122:
                #bringing it down by 26
                letter -= 26
            #checking if the letter is too small
            elif letter >= 97:
                #bringing the letter up by 26
                letter += 26
        #reset the letter to a letter instead of a number
        letter = chr(letter)
        #add the letter to a new word
        new_word = new_word + letter
    #return with the new word
    return(new_word)

#make an infinite loop
while check != "anything":
    #reset the new word
    new_word = ""
    #Check if the user wants to quit, code, or decode
    check = input('If you want to code a cipher, write "code". If you want to decode a word, write "decode". If you want to quit, write anything. ').lower().strip()
    #if they want to code
    if check == "code":
        #ask what they want to be coded
        word = input("What do you want to be coded? ")
        #ask how much do you want your word shifted?
        ciph = int(input("How much do you want your word to be shifted? "))
    #otherwise if they want to decode
    elif check == "decode":
        #check what they want to be coded
        word = input("What do you want to be decoded? ")
        #ask how much do you want your word shifted?
        ciph = int(input("How much do you want your word to be shifted? "))
    #otherwise
    else:
        #end the loop
        break
    #print a statement with the old word and the new
    print(f"Your input was {word}. The output is {cipher(word, ciph, new_word)}. ")
#easter egg
else:
    print("Congrats! You found the easter egg! ")

