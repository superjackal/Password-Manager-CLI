# """Password Manager stores passwords in a master password protected zip file
# Each time program runs, new json file created and appended to zip"""


import json
from time import sleep

def password_gen(l:int) -> str:
    from random import choice
    from string import ascii_letters, digits
    return ''.join([choice(ascii_letters + digits + "!()-.?[]_`~;:!@#$%^&*+=") for _ in range(l)])

def read_file(file:str) -> dict:
    # Read Contents of json which stores the passwords
    try:
        with open(file) as f:
            read_dict = json.load(f)
    # If file not found then creates a new file
    except FileNotFoundError:
        with open(file,"w") as f:
            read_dict = {"foo":"bar"}
            # f.write(json.dumps(read_dict, indent=2))
            json.dump(read_dict, f, indent=2)
    return read_dict

def add_password(read_dict:dict, file:str) -> None:
    print(f"Enter Account Name to add(like 'Google' or 'Facebook')\nAccount Name has to be Unique")
    while(True):
        account_name = input("> ")
        if account_name not in read_dict:
            read_dict[account_name] = password_gen(20)
            break
        else:
            print("Account Name already exists.")
            sleep(1)
            print("Please enter a Unique Account Name")

    with open(file,"w") as f:
        f.write(json.dumps(read_dict, indent=2))
    print("Account Added")

def get_password(read_dict:dict) -> str:
    while True:
        account_name=input("Enter Account Name whose Password you need to retrive\n> ")
        if account_name in read_dict:
            return read_dict[account_name]
        else:
            print("Account does not exist. Try again.")
            sleep(1)


# from zipfile import ZipFile
# with ZipFile('new.zip','w') as zip:
#     zip.write('new.json')

# import json
# Writing to JSON
# a={1:2,3:4}
# with open("new.json","a") as f:
#     f.write(json.dumps(a))

# Reading JSON
# with open("new.json","r") as f:
#     b =json.load(f)