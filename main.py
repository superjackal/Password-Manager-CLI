from argparse import ArgumentParser
import pyperclip
from DB_Ops import *

def main():
    parser = ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-a", "--add", help="Add a password with the given account name")
    group.add_argument("-r", "--read", help="Read a password of the given account name")
    group.add_argument("-l", "--list", help="List all accounts for which password is stored", action="store_true")
    group.add_argument("-x", "--delete", help="Remove a password")
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
    elif args.list:
        con = initial_setup()
        for account in get_accounts(con):
            print(account)
    elif args.delete:
        delete_account(con, args.delete)
    con.close()
if __name__ == '__main__':
    main()
