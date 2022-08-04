from statistics import mode
from xml.parsers.expat import model
from rich.prompt import Prompt
from rich.panel import Panel
import rich,os
from crypto import cryptograph 
from Models import models

global username
global pin
global sno
sno = 0
# def signup():
    # ch=1
    # while ch!=0:
    #     username = Prompt.ask("Enter username")
    #     pin = int(Prompt.ask("Enter your pin"))
    #     if os.path.isfile(f"{username}.db"):
    #         Prompt("username already exists please select another username")
    #     else:
    #         db = models.Database0x(username)
    #         ch=0

# def signin():
    # ch=1
    # while ch!=0:
    #     username = Prompt.ask("Enter username")
    #     pin = int(Prompt.ask("Enter your pin"))
    #     if os.path.isfile(f"{username}.db"):
    #         ch=0
    #     else:
    #         choice = Prompt.ask("Username Invalid! [bold]Signup : S or Retry : R[/bold]",choices=["s","r"],default="r")
    #         if choice == "s":
    #             signup()
    #         else:
    #             ch=1

def addpasswd():
    sno += 1
    website = Prompt.ask("Enter website name")
    password = Prompt.ask("Enter password")
    _init_crypto = cryptograph.Cryptograph(username,pin)
    _key = _init_crypto.makekey()
    _xor_passwd= _init_crypto.xorthese(password,_key)
    db = models.Database0x(username)
    db.intovalue(sno,website,_xor_passwd)

rich.print(Panel("[bold white]Welcome to Trident Password Manager",subtitle="TPM version 0.0.1"))
choice = Prompt.ask("Choose Signup : u or Signin : i",choices=["u","i"], default="u")
if choice == "u":
    ch=1
    while ch!=0:
        username = Prompt.ask("Enter username")
        pin = int(Prompt.ask("Enter your pin"))
        if os.path.isfile(f"{username}.db"):
            print("username already exists please select another username")
        else:
            db = models.Database0x(username)
            ch=0
    ch=1
    sno = 0
    while ch!=0:
        db.createtable()
        addpasswd()
        choice = Prompt.ask("add more : a or Save and exit : s",choices=['a','s'],default='s')
        if choice == 'a':
            pass
        else:
            ch=0

else:
    ch=1
    while ch!=0:
        username = Prompt.ask("Enter username")
        pin = int(Prompt.ask("Enter your pin"))
        if os.path.isfile(f"{username}.db"):
            ech=1
            while ech!=0:
                addpasswd()
                choice = Prompt.ask("add more : a or Save and exit : s",choices=['a','s'],default='s')
                if choice == 'a':
                    pass
                else:
                    ech=0    
            ch=0
        else:
            choice = Prompt.ask("Username Invalid! [bold]Signup : S or Retry : R[/bold]",choices=["s","r"],default="r")
            if choice == "s":
                ech=1
                while ech!=0:
                    username = Prompt.ask("Enter username")
                    pin = int(Prompt.ask("Enter your pin"))
                    if os.path.isfile(f"{username}.db"):
                        print("username already exists please select another username")
                    else:
                        db = models.Database0x(username)
                        ech=0
            else:
                ch=1
    

#  finalchar=_init_crypto.binxor(_key,_xor_passwd)
#         print(finalchar)
#         paswd = _init_crypto.charthis(finalchar)
#         print(paswd)