import sqlite3
import string
class Database0x:
    def __init__(self,datadb:string = "username"):
        conn = sqlite3.connect(datadb)
        self.cur = conn.cursor()
        
    def createdb(self):
        self.cur.execute("CREATE TABLE user (username TEXT)")
    
    def intodb(self):
        self.cur.execute(f"INSERT INTO TBALE VAlUES")