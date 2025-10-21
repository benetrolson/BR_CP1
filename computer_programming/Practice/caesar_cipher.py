#BHR 2nd caesar cipher
#ord for converting to number, chr for converting back
letter = ""
def cipher(word, ciph):
    for letters in word:
        letter = ord(letters)
        if letter >= 65 and letter <= 90:
            letter += ciph
            if letter <= 90:
                letter -= 25
            elif letter >= 65:
                letter += 25
        elif letter >= 97 and letter <= 122:
            letter += ciph
            if letter <= 122:
                letter -= 25
            elif letter >= 97:
                letter += 25

while True:
    check = input('If you want to code a cipher, write "code". If you want to decode a word, write "decode"')
    letter = input("What do you want to be")
