import random

def encode(message:str,key:int):
    message_encoded = ""
    for l in message:
        message_encoded += chr(((ord(l)-ord("A"))+ key%26 + ord("A")))
    return message_encoded

