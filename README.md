# Trident Password Manager (TPM)
We use a serverless database to store your passwords and then we secure them using Xor encryption.
***
## Important instructions
> 1. Please note your pin and username after signup.
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
>Username and pin are combined and converted into hash which is stored in the masterpassword table of database, this is later used for the authentication purposes.
