# Trident Password Manager (TPM)
TPM is a tool to store your password by securing it through cryptography
***
## Important instructions
> 1. Please note your pin, masterpassword and username after signup.
> 1. Do not share your pin / password with anyone.
> 1. Install all the required modules in ***requirments.txt*** for hasle free experience.
> 1. To run the program use ***main.py*** .
> 1. Have fun and give us your valuable feedback for improvement.
## How this works?
### 1. Generating key and encrypting passwords
```py 
def makekey(self): 
    key =str(self.pin) + self.username 
    _key = Cryptograph.binthis(self,tri=key)
    return _key
```
> We take two inputs from user that is username and pin then we join them and make a single string as shown in the above funtion.
```py 
def binthis(self,tri): 
    return "".join(f"{ord(i):08b}" for i in tri)
```
>Character string of the key is then converted into a binary string using ```binthis()``` function

```py
    def xorthese(self,password,key):
        result = ""
        password = Cryptograph.binthis(self,tri=password)
        if len(password) > len(key):
            lenfor0 = len(password) - len(key)
            key +='0'*lenfor0
            for i in range(len(key)):
                if key[i]==password[i]:
                    result += "0"
                else:
                    result += "1"
        elif len(password)<len(key):
            lenfor0 = len(key)-len(password)
            password += '0'*lenfor0
            for i in range(len(key)-1):
                if key[i]==password[i]:
                    result += "0"
                else:
                    result += "1"
        return result
```
>Finally the password entered by user is encrypted using XOR encryption by ```xorthese()```
### 2. Saving your passwords.
```py
def createtable(self):
        self.cur.execute('CREATE TABLE "user" ("Sno" int PRIMARY KEY,"website_name" text,"username" text, "password" text)')
```

> When user creates their account a database file is created for the user using ```createtable()``` from models class and after each successful save the passwords are written into the user table of database using  ```intovalue()``` function of models class
```py 
    def intovalue(self,sno,websitename,_username,password):
        self.cur.execute(f'INSERT INTO "user" VALUES({sno},"{websitename}","{_username}","{password}")')
        self.conn.commit()
```
### 3. Master password 
```py 
masterpassword = Prompt.ask("[bold]Enter master password[/bold]")
       
if len(masterpassword)<8:
    print("Master password must have atleast 8 characters!")
    continue
else:
    _hash = sha256(masterpassword.encode('utf-8')).hexdigest()
    db.createmasterpwd(_hash)
    break
```
>To add some security to the password manager we ask user to add a **Master Password** this password is stored as a hash in the database, this password is required at every signin later.