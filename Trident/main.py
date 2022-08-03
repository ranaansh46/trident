from rich.prompt import Prompt
from rich.panel import Panel
from rich import print
from crypto import cryptograph 

username = Prompt.ask("Enter your username")
pin = int(Prompt.ask("Enter your pin"))
password = "defaultpassword"
key = "00111"


# key = cryptograph.Cryptography(username,pin,password).makekey()
# print(key[2:])
# password = "hello1234"
# passwd = cryptograph.Cryptography(username)
# key = passwd.makekey()

_init_crypto = cryptograph.Cryptography(username,pin)

_key = _init_crypto.makekey()

_xor_passwd = _init_crypto.xorthese(password,_key)

print(_xor_passwd)