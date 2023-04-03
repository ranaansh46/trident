from crypto import cryptograph 
from Models import models

import string,rich,os

from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
from rich.console import Console
from rich import print

#Used for Hashing
from re import compile, search
from hashlib import sha256

#for generating password
import random
import secrets

def signup():
    """ Summary:
    This function is used to initiate database class and read username, pin and master password then writes
    hash of master password in the database file then returns username , pin and db object. 

    Returns:
        Object : db object is returned, this object is used to add, remove and show passwords.
        String : Username string is returned, this object is used as the database file name and part of the key.
        Int : pin is returned this number is later used as part of key.
    """
    print("[bold red]Important! please note your pin and username as you cannot change them in future") 
    x = compile('[@_!#$%^&*()<>?/\|}{~:]')
    while True:
        username = Prompt.ask("[bold]Enter username")

        if len(username)<6:
            print("[red]Username must have atleast 6 characters!")
            continue
        if (x.search(username)):
            print("[red]special characters not allowed!")
            continue
        if os.path.isfile(f"{username}.db"):
            print("[red]username already exists please select another username")
            continue
        else :
            db = models.Database0x(username)
            break
    
    while True:
        pin = str(Prompt.ask("[bold]Enter your pin[/bold]"))   
        if len(pin)<4:
            print("pin must have atleast 4 characters!")
            continue
        else:
            break
    _init_crypto = cryptograph.Cryptograph(username,pin)
    _key = _init_crypto.makekey()
    _hash = sha256(_key.encode('utf-8')).hexdigest()
    db.createmasterpwd(_hash)
    return db,username,pin

def signin():
    """ Summary: This is function reads username, pin and master password it confirms the master password from the database and then returns 
    
    Returns:
        Object : db object is returned, this object is used to add, remove and show passwords.
        String : Username string is returned, this object is used as the database file name and part of the key.
        Int : pin is returned this number is later used as part of key.
    """
    while True:
        username = Prompt.ask("[bold]Enter username")
        if os.path.isfile(f"{username}.db"): #to check is  database file  for username already exists
            pin = str(Prompt.ask("[bold]Enter your pin"))
            db = models.Database0x(username)
            _init_crypto = cryptograph.Cryptograph(username,pin)
            _key = _init_crypto.makekey()
            _hash = sha256(_key.encode('utf-8')).hexdigest()
            if _hash == db.returnhash():
                return db,username,pin
            else:
                rich.print("[red bold]Wrong credentials!!")
                continue
            
        else:
            choice = Prompt.ask("[bold red]Username Invalid![/bold red] [bold]Signup : S or Retry : R[/bold]",choices=["s","r"],default="r")
            if choice == "s":
               db,username,pin = signup()
               return db,username,pin
            else:
                continue

def passGenerator():
    specialCharacters = "!@#$%^&*"
    numberOfUpperCase = 4
    numberOfLowerCase = 4
    numberOfDigits = 4
    numberOfSpecialCharacters = 4
    randomUppercase = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(numberOfUpperCase))
    randomLowercase = ''.join(secrets.choice(string.ascii_lowercase) for _ in range(numberOfLowerCase))
    randomDigits = ''.join(secrets.choice(string.digits) for _ in range(numberOfDigits))
    randomSpecialCharacters = ''.join(secrets.choice(specialCharacters) for _ in range(numberOfSpecialCharacters))

    tempStr = randomUppercase + randomLowercase + randomDigits + randomSpecialCharacters
    finalString = list(tempStr)
    random.shuffle(finalString)
    return ''.join(finalString)

def addpasswd(username,pin,db,check:bool=True):
    """This password reads website name , username for website, password and writes it in the database file

    Args:
        username (String): Username entered by user at signin/signup used in key
        pin (Int): pin entered by user at signin/signup used in key 
        db (Object): this object is used to pass values in the database
        check (bool, optional): this check is used to avoid the no entry error when new user writes password. Defaults to True.
    """
    if check:
        __sno = db.returnsno()
    else:
        __sno = 0
    _sno = __sno + 1
    website = Prompt.ask("Enter website name")
    _username = Prompt.ask("Enter username for website")
    choice = Prompt.ask("Generate Password : g or enter mannualy : m",choices=['g','m'],default='g')
    if choice == 'g':
        password = passGenerator()
        rich.print("Generated password : ",password)
    elif choice == 'm':
        password = Prompt.ask("Enter password")
    _init_crypto = cryptograph.Cryptograph(username,pin)
    _key = _init_crypto.makekey()
    _xor_passwd= _init_crypto.xorthese(password,_key)
    db.intovalue(_sno,website,_username,_xor_passwd)

def rempasswd(username,pin,db):
    """
    Summary: 
    

    Args:
        username (_type_): _description_
        pin (_type_): _description_
        db (_type_): _description_
    """
    showpasswd(db, username, pin)
    sno = int(input("Enter S.no for the password you want to remove: "))
    db.deletevalue(sno)

def showpasswd(db,username,pin):
    _init_crypto = cryptograph.Cryptograph(username, pin)
    table = Table(title="List of your password")
    table.add_column("[blue]S.no[/blue]",style="#FFA500")
    table.add_column("[blue]Website[/blue]",style="white")
    table.add_column("[blue]Username[/blue]")
    table.add_column("[blue]Passwords[/blue]",style="green")
    i = db.returnsno()
    _key = _init_crypto.makekey()
    for x in range(1,i+1):
        s,w,u,p = db.returnvalue(x)
        _p = _init_crypto.binxor(p,_key)
        _p = _init_crypto.charthis(_p)
        table.add_row(str(s),str(w),str(u),str(_p))
    console = Console()
    console.print(table)
        

if __name__ == "__main__":
    rich.print(Panel.fit("[bold white]Welcome to Trident Password Manager",subtitle="TPM version 0.0.1 alpha"))
    choice = Prompt.ask("Choose Signup : u or Signin : i",choices=["u","i"], default="u")
    if choice == "u": #this is sign up section of the program
        db,username,pin = signup()
        sno = 0
        ch = 1
        db.createtable()
        addpasswd(username,pin,db,check=False)
        while ch!=0:
            choice = Prompt.ask("add more : a or Save and exit : s",choices=['a','s'],default='s')
            if choice == 'a':
                addpasswd(username, pin, db)
                showpasswd(db,username,pin)
            else:
                ch=0

    else: #this is sign in section
        db,username,pin = signin()
        while True:
            choice = Prompt.ask("Edit: e / Show: s / Exit: x",choices=['e','s','x'],default='s')
            if choice == 's':
                showpasswd(db,username,pin)
            elif choice == 'e':
                while True:
                    _choice = Prompt.ask("Add: a / Remove: r / Back: b",choices=['a','r','b'],default='b')
                    if _choice == 'a':
                        addpasswd(username,pin,db)
                        showpasswd(db,username,pin)        
                    elif _choice == 'r':
                        rempasswd(username,pin,db)
                        showpasswd(db,username,pin)
                    else:
                        break
            else:
                break