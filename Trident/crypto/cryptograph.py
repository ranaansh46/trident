class abc:
    def __init__(self,username,pin) -> None:
        self.username = username
        self.pin = pin
    def keymake(self):
        key = self.username + str(self.pin)
        print(key)
        temp_key = ""
        for i in key:
            temp_key = temp_key + str(ord(i))

        key = temp_key
        key = bin(int(key))
        print(key)