"""
Password manager stores password in a json
Allows adding new password and retrieving existing passwords
"""

from DB_Ops import *
from time import sleep
from sys import exit
import pyperclip

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
    con = initial_setup()
    if choice == '1':
        account_name = input("Enter account name\n> ")
        if add_password(con, account_name):
            print("Password added")
        else:
            print("Password already exists for the given account name")
        returnToMenu()
    elif choice == '2':
        account_name = input("Enter account name\n> ")
        password = get_password(con, account_name)
        if password:
            pyperclip.copy(password)
            print("Password copied to clipboard.\nNote: This tool will not remove the password from the clipboard after you exit.")
        else:
            print("Account not found")
        returnToMenu()
    elif choice == '3':
        exit(0)

if __name__ == '__main__':
    menu()