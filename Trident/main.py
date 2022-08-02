from rich.prompt import Prompt
from rich.panel import Panel
from rich import print
from crypto import cryptograph 

username = Prompt.ask("Enter your username")
pin = int(Prompt.ask("Enter your pin"))
password = "defaultpassword"
key = "00111"


key = cryptograph.Cryptography(username,pin,password).makekey()
print(key[2:])
password = "hello1234"
password = cryptograph.Cryptography(username,pin,password).xorthese(password)