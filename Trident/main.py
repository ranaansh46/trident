from statistics import mode
from xml.parsers.expat import model
from rich.prompt import Prompt
from rich.panel import Panel
from rich import print
from crypto import cryptograph 
from Models import models
username = Prompt.ask("Enter your username")
pin = int(Prompt.ask("Enter your pin"))
password = Prompt.ask("Enter your password")

# key = cryptograph.Cryptography(username,pin,password).makekey()
# print(key[2:])
# password = "hello1234"
# passwd = cryptograph.Cryptography(username)
# key = passwd.makekey()

_init_crypto = cryptograph.Cryptograph(username,pin)

_key =_init_crypto.makekey()
_xor_passwd= _init_crypto.xorthese(password,_key)
print(_xor_passwd)
db = models.Database0x(username)
# db.createtable()
# db.intovalue(2,"gmail.com",str(_xor_passwd))
# db.deletevalue(2)
sno , websitname , xorp = db.returnvalue(1)

print(sno,websitname,xorp)

finalchar=_init_crypto.binxor(_key,xorp)
# print(finalchar)
paswd = _init_crypto.charthis(finalchar)
print(websitname,paswd)