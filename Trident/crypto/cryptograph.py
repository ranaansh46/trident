from operator import xor
class Cryptograph:
    def __init__(self,username,pin) -> None:
        self.username = username
        self.pin = pin
        self.tri = "key"
        self.key = "key"

    def binthis(self,tri): #this function takes a string and returns a binary string
        return "".join(f"{ord(i):08b}" for i in tri)
    def makekey(self): #this function makes binary key using two arguments
        # 1st = username which is a string argument  
        # 2nd = Pin which is an integer argument and makes a binary key using both of these
        key = self.username + str(self.pin)
        _key = Cryptograph.binthis(self,tri=key)
        return _key
    
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
        
        # print(len(password),password)
        # print(len(self.key),self.key)

        
        # print(self.key)
        # print(password)
        return result

    def charthis(self,_bytes):
        charac = ""
        for i in range(len(_bytes)//8):
            _ext_bytes = _bytes[i*8:(i+1)*8]
            charac += chr(int(_ext_bytes,base=2))
        return charac
            
    def binxor(self,_xorpas,_key):
        extchar = ''
        _xorpas = str(_xorpas)
        if len(_xorpas)> len(_key):
            lenforA = len(_xorpas)- len(_key)
            _key += "0"*lenforA

            # for i in range(len(_xorpas)):
            #     if _xorpas[i]==_key[i]:
            #         extchar += "0"
            #     else:
            #         extchar += "1"
        elif len(_xorpas) < len(_key):
            lenforB = len(_key)-len(_xorpas)
            _xorpas += "0"*lenforB
            # for i in range(len(_xorpas)):
            #     if _xorpas[i]==_key[i]:
            #         extchar += "0"
            #     else:
            #         extchar += "1"
        
        for i in range(len(_xorpas)):
            if _xorpas[i]==_key[i]:
                extchar += "0"
            else:
                extchar += "1"
        return extchar