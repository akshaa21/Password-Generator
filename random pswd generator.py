
# Random password generator
import random
import string

def pswd():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    all = lower + upper + numbers + symbols
    length = int(input("Enter the length of the password: "))
    password = ""

    for x in range(length):
        password += random.choice(all)

    print("Your password is: ",password )    
    print("\n-----------------------------------------------------------------------\n")
    pswd()
pswd()    
