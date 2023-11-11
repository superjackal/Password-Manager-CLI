import sqlite3
def initial_setup() -> sqlite3.Connection:
    con = sqlite3.connect("database.db")    
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS passwords(account, password)")
    cur.close()
    return con

def password_gen(l:int) -> str:
    from random import choice
    from string import ascii_letters, digits
    return ''.join([choice(ascii_letters + digits + "!()-.?[]_`~;:!@#$%^&*+=") for _ in range(l)])

def check_exists(con:sqlite3.Connection, account_name:str) -> bool:
    cur = con.cursor()
    cur.execute("SELECT account FROM passwords")
    for (account,) in cur.fetchall():
        if account == account_name:
            return True
    return False

def add_password(con:sqlite3.Connection, account_name:str) -> bool:
    if not check_exists(con, account_name):
        cur = con.cursor()
        cur.execute("INSERT INTO passwords VALUES(?, ?)", (account_name, password_gen(20)))
        con.commit()
        cur.close()
        return True
    else:
        return False

def get_password(con:sqlite3.Connection, account_name:str) -> str | None:
    cur = con.cursor()
    cur.execute("SELECT password from passwords WHERE account=?", (account_name, ))
    res = cur.fetchall()
    cur.close()
    if res:
        return res[0][0]
    else:
        return None


if __name__ == '__main__':
    con = initial_setup()
    check_exists(con, "Google")
    con.close()