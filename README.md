# Password Manager CLI
Simple CLI tool fro managing your password made using Python and SQLite.

## Prequisites
1. Python3 installed.
2. Install the required libraries `pip install`

## Functionalities
- Add a password for a given acocunt name.
- Read a password and store it in the clipboard.
- Remove a password for a given acocunt name.
- List all accounts.

## Usage

### Add the account for google
`python main.py -a google`

### Read the password for google
`python main.py -r google`

### Remove the account for google
`python main.py -x google`

### List all accounts
`python main.py -l`
