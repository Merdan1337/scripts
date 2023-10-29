# Import libraries and set current directory
import string
import random
import os
from pathlib import Path
os.chdir(Path(__file__).parent)


character = string.ascii_letters
numbers = string.digits
sonderzeichen = string.punctuation
allchars = character+numbers+sonderzeichen
charsnumbers = character+numbers
loopingtext = "Your new generated password"


input_length = int(input("Enter the password length: "))
input_special_chars = input("With Special Special Charachter [y/n] ? ")
input_duplicate = input("With duplicate [y/n] ? ")


if input_length > 0:
    if input_special_chars == "y" :
        if input_duplicate == "y" :
            loopingtext += " with special chars & duplicates is: "
            generated_password = random.choices(allchars, k = input_length) 
        else:
            loopingtext += " without duplicates is:  "
            generated_password = random.sample(allchars, k = input_length)
    elif input_special_chars == "n" :
        if input_duplicate == "y" :
            loopingtext += " without special chars is:  "
            generated_password = random.choices(charsnumbers, k = input_length)
        else:
            loopingtext += " without special chars nor duplicates is:  "
            generated_password = random.sample(charsnumbers, k = input_length)
else:
    print("The Password length needs to be atleast 1")


generated_password = "".join(generated_password)
everything = loopingtext + generated_password
print(everything)


# generates passwort.txt file with generated password in it
with open("password.txt", mode= "w", encoding= "UTF-8") as file:
    file.write(everything)
