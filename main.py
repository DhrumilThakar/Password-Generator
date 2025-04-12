import string
import random

string_of_upper = string.ascii_letters.upper()
string_of_lower = string.ascii_letters.lower()
string_of_number = string.digits
string_of_punctuation = string.punctuation

password_string = []
password_length = int(input("Enter the length of password : "))

password_string.extend(string_of_number)
password_string.extend(string_of_lower)
password_string.extend(string_of_upper)
password_string.extend(string_of_punctuation)

print("Your password is : ")
print("".join(random.sample(password_string,password_length)))
