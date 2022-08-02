from rich.prompt import Prompt
from rich import print
import typer
key = "key"
username = "username"
pin = 1234
username = Prompt.ask("[bold white]Enter username")
pin = int(Prompt.ask("[bold white]Enter Pin"))
key = username + str(pin)
print(key)
temp_key = ""
for i in key:
    temp_key = temp_key + str(ord(i))

key = temp_key
print(key)