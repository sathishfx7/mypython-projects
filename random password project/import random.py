import random
print("Welcome to your password generator")
 
characters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*(),.1234567890"

number = input ("amount of passwords to generate: ")
number = int(number)

length = input ("input your password length: ")
length = int(length)

print ("\nHere are your passwords: ")

for pwd in range(number):
    passwords = ''
    for c in range (length):
        passwords += random.choice(characters)
print(passwords)