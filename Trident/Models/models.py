import sqlite3
import string
class Database0x:
    def __init__(self,username,xorpass,datadb:string = "database.db"):
        conn = sqlite3.connect(datadb)
        self.cur = conn.cursor()
        self.user = username
        self.passwd = xorpass
    def createdb(self):
        self.cur.execute("CREATE TABLE user (username TEXT,xorpass INT)")
    
    def intodb(self):
        self.cur.execute(f"INSERT INTO user VAlUES({self.user},{self.passwd})")