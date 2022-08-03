class Cryptography:
    def __init__(self,username,pin) -> None:
        self.username = username
        self.pin = pin
        self.tri = "key"
        self.key = "key"

    def binthis(tri): #this function takes a string and returns a binary string
        temp_key = "" 
        for i in tri:
            temp_key = temp_key + str(ord(i))
            
        tri = temp_key        
        tri = bin(int(tri))
        return tri

    def makekey(self): #this function makes binary key using two arguments
        # 1st = username which is a string argument  
        # 2nd = Pin which is an integer argument and makes a binary key using both of these
        key = self.username + str(self.pin)
        key = Cryptography.binthis(tri=key)
        return key
    
    def xorthese(self,password,key):
        result = ""
        self.key = key[2:]
        password = Cryptography.binthis(tri=password)
        password = password[2:]
        for i in range(len(key)-2):
            if(self.key[i]==password[i]):
                result += "0"
            else:
                result += "1"
        return result