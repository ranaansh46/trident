from rich.prompt import Prompt
from rich import print
import typer

#variables
key = "key"
username = "username"
pin = 1234

#Functions
def keymake():
    key = username + str(pin)
    print(key)
    temp_key = ""
    for i in key:
        temp_key = temp_key + str(ord(i))

    key = temp_key
    key = bin(int(key))
    print(key)

if __name__=="main":
    username = Prompt.ask("[bold white]Enter username")
    pin = int(Prompt.ask("[bold white]Enter Pin"))
    keymake()