from statistics import mode
from xml.parsers.expat import model
from rich.prompt import Prompt
from rich.panel import Panel
import rich,os
from crypto import cryptograph 
from Models import models
from rich.table import Table
from rich.console import Console

def signup():
    ch=1
    while ch!=0:
        username = Prompt.ask("Enter username")
        pin = int(Prompt.ask("Enter your pin"))
        if os.path.isfile(f"{username}.db"):
            Prompt("username already exists please select another username")
        else:
            db = models.Database0x(username)
            return db,username,pin
            ch=0

def signin():
    ch=1
    while ch!=0:
        username = Prompt.ask("Enter username")
        pin = int(Prompt.ask("Enter your pin"))
        if os.path.isfile(f"{username}.db"):
            db = models.Database0x(username)
            return db,username,pin
            ch=0
        else:
            choice = Prompt.ask("Username Invalid! [bold]Signup : S or Retry : R[/bold]",choices=["s","r"],default="r")
            if choice == "s":
               db = signup()
               return db,username,pin
            else:
                ch=1

def addpasswd(username,pin,db,check:bool=True):
    if check:
        __sno = db.returnsno()
        rich.print(__sno)
    else:
        __sno = 0
    _sno = __sno + 1
    website = Prompt.ask("Enter website name")
    password = Prompt.ask("Enter password")
    _init_crypto = cryptograph.Cryptograph(username,pin)
    _key = _init_crypto.makekey()
    _xor_passwd= _init_crypto.xorthese(password,_key)
    db.intovalue(_sno,website,_xor_passwd)

def showpasswd(db,username,pin):
    _init_crypto = cryptograph.Cryptograph(username, pin)
    table = Table(title="List of your password")
    table.add_column("S.no",style="cyan")
    table.add_column("Website",style="magenta")
    table.add_column("Passwords",style="green")
    i = db.returnsno()
    for x in range(i):
        s,w,p = db.returnvalue(x)
        _p = _init_crypto.binxor(p,_init_crypto.makekey(username,pin))
        _p = _init_crypto.charthis(_p)
        table.add_row(s,w,_p)
        console = Console()
        console.print(table)
        


if __name__ == "__main__":
    rich.print(Panel("[bold white]Welcome to Trident Password Manager",subtitle="TPM version 0.0.1"))
    choice = Prompt.ask("Choose Signup : u or Signin : i",choices=["u","i"], default="u")
    if choice == "u": #this is sign up section
        db,username,pin = signup()
        sno = 0
        ch = 1
        db.createtable()
        addpasswd(username,pin,db,check=False)
        while ch!=0:
            choice = Prompt.ask("add more : a or Save and exit : s",choices=['a','s'],default='s')
            if choice == 'a':
                addpasswd(username, pin, db)
            else:
                ch=0

    else: #this is sign in section
        ch=1
        while ch!=0:
                db,username,pin = signin()
                ech=1
                while ech!=0:
                    addpasswd(username,pin,db)
                    choice = Prompt.ask("add more : a or Save and exit : s",choices=['a','s'],default='s')
                    if choice == 'a':
                        pass
                    else:
                        ech=0    
                ch=0