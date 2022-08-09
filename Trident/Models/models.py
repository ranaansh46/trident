import sqlite3

class Database0x:
    def __init__(self,datadb="username"):
        self.conn = sqlite3.connect(f"{datadb}.db")
        self.cur = self.conn.cursor()
        
    def createtable(self):
        self.cur.execute('CREATE TABLE "user" ("Sno" int PRIMARY KEY,"website_name" text,"username" text, "password" text)')

    def intovalue(self,sno,websitename,_username,password):
        self.cur.execute(f'INSERT INTO "user" VALUES({sno},"{websitename}","{_username}","{password}")')
        self.conn.commit()

    def deletevalue(self,id:int):
        self.cur.execute(f'DELETE FROM "user" WHERE "Sno" = {id}')
        _id =id
        for i in range(id,Database0x.returnsno(self)):
            self.cur.execute(f'UPDATE "user" SET "Sno"= {i} WHERE "Sno" = {_id+1}')
            _id+=1
        self.conn.commit()

    def returnvalue(self,sno:int):
        self.cur.execute(f'SELECT * FROM "user" WHERE "Sno" ={sno}')
        _sno ,_websitename ,_username, _xorp = self.cur.fetchone()
        return _sno , _websitename ,_username, _xorp

    def returnsno(self):
        self.cur.execute('SELECT * FROM  "user" ORDER BY "Sno" DESC LIMIT 1')
        _sno,_,_,_ = self.cur.fetchone()
        return _sno
    
    # for master password
    
    def createmasterpwd(self,_hash):
        self.cur.execute('CREATE TABLE "masterpass" ("Sno" int PRIMARY KEY,"password" text)') 
        self.cur.execute(f'INSERT INTO "masterpass" VALUES(0,"{_hash}")')
    
    def returnhash(self):
        self.cur.execute('SELECT * FROM  "masterpass"')
        _,_hash = self.cur.fetchone()
        return _hash
    
    def __exit__(self):
        self.conn.close()
    