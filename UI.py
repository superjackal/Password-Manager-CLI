"""
Password manager stores password in a json
Allows adding new password and retrieving existing passwords
"""

from Operations import *
from time import sleep
from sys import exit

def returnToMenu() -> None:
    sleep(1)
    choice = input("Return to Main Menu? y/n\n> ").strip().lower()
    if choice == 'y':
        menu()
    elif choice == 'n':
        exit(0)
    exit(10)

def menu() -> None:
    # Taking User Choice to add password or retrive existing password
    print("1.Add Password\n2.Read Existing Password\n3.Exit")
    while(True):
        print("Enter your choice")
        choice = input("> ").strip()
        if choice not in ['1', '2', '3']:
            print("Not a correct choice")
        else:
            break
    file= "new.json"    # Name of JSON File
    read_dict = read_file(file=file)
    if choice == '1':
        add_password(read_dict=read_dict, file=file)
        returnToMenu()
    elif choice == '2':
        password = get_password(read_dict=read_dict)
        print(password)
        returnToMenu()
    elif choice == '3':
        exit(0)


if __name__ == '__main__':
    menu()