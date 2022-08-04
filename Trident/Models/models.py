import sqlite3
class Database0x:
    def __init__(self,datadb="username"):
        self.conn = sqlite3.connect(f"{datadb}.db")
        self.cur = self.conn.cursor()
        
    def createtable(self):
        self.cur.execute('CREATE TABLE "user" ("Sno" int PRIMARY KEY,"website_name" text,"password" text)')

    def intovalue(self,sno,websitename,password):
        self.cur.execute(f'INSERT INTO "user" VALUES({sno},"{websitename}","{password}")')
        self.conn.commit()

    def deletevalue(self,id:int):
        self.cur.execute(f'DELETE FROM "user" WHERE "Sno" = {id}')
        self.conn.commit()

    def returnvalue(self,sno:int):
        self.cur.execute(f'SELECT * FROM "user" WHERE "Sno" ={sno}')
        _sno ,_websitename ,_xorp = self.cur.fetchone()
        return _sno , _websitename , _xorp
    def __exit__(self):
        self.conn.close()
    