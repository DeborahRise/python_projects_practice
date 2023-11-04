#!/usr/bin/python3
username = "deb"
password = "A2023alx"

print("Nice! You joined us!")
user = input("username: ").lower()
passs = input("password: ")

if (user == username and passs == password):
    print("Welcome")
else:
    print("access denied")
