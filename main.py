from argparse import ArgumentParser
import pyperclip
from DB_Ops import *

def main():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", help="Add a password with the given account name")
    group.add_argument("-r", "--read", help="Read a password of the given account name")

    args = parser.parse_args()
    con = initial_setup()
    if args.read:
        password = get_password(con, account_name=args.read)
        if password:
            pyperclip.copy(password)
            print("Password copied to clipboard.\nNote: This tool will not remove the password from the clipboard after you exit.")
        else:
            print("Account not found")
    elif args.add:
        if add_password(con, account_name=args.add):
            print("Password Added")
        else:
            print("Password already exists for the given account name")

if __name__ == '__main__':
    main()
