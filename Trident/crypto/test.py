# from rich import print
# import binascii

# def binthis(tri): #this function takes a string and returns a binary string
#         temp_key = "" 
#         for i in tri:
#             temp_key = temp_key + str(ord(i))
            
#         tri = temp_key        
#         tri = bin(int(tri))
#         return tri


# def charthis(dent):
#     temp_string = bytes(dent[2:],"ascii")
#     print(len(temp_string))
#     return binascii.b2a_base64(temp_string)

# tri = input("enter password :")
# password = binthis(tri)
# print("before charthis :")
# password = charthis(password)
# print("after charthis :")
# print(password)