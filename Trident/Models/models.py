import sqlite3
import string
class Database0x:
    def __init__(self,datadb:string = "username"):
        self.conn = sqlite3.connect(datadb)
        
    def createdb(self):
        pass