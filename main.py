import math
import random
import sys
from cipher_art import logo
logo()

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h" ,"i", "j" ,"k", "l", "m", "n","o", "p",\
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
continue_to_cipher = True
while continue_to_cipher:
    direction = input("Type 'Encode' to encrypt, type 'Decode' to decrypt:\n").lower()
    text = input("Type your message: ")
    shift = int(input("what is your shift number?\n"))
    random.seed(shift)
    shift = random.randint(0, 2^128)
    print(shift)
    
    

    def caesar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
                shift_amount *= -1
        for element in start_text:
            if element in alphabet:
                position = alphabet.index(element)
                new_position = position + shift_amount
                new_position = new_position % len(alphabet)
                end_text += alphabet[new_position]
            else:
                end_text += element
        print(f"The {cipher_direction}d text is {end_text}.")

    #shift = shift % 26# the remainder is your shift
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "no":
        print("Goodbye")
        break
