def decode(message:str,key:int):
    message_decoded = ""
    for l in message:
        message_decoded += chr(((ord(l)-ord("A"))- key%26 + ord("A")))
    return message_decoded

