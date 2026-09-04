import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

password = ""

length = int(input("How long should the password be? "))

for _ in range(length):
    characters = letters + numbers + symbols
    password += random.choice(characters)

print(f"Your password is: {password}")