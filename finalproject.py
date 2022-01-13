#!/usr/bin/env python3

master_pwd = input("What is the master password? ")

def view():
     with open("password.txt", "r") as f:
         for line in f.readlines():
             print(line)

view()

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones (view, add) or press q to quit?  ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid action.")
        continue
