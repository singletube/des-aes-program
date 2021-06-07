from des import DesKey
from Crypto.Util.Padding import pad, unpad

def Encrypt(key, text):
    if(len(key) > 8):
        return("Ключ больше 8 байт")

    if(len(key) < 8):
        return("Ключ меньше 8 байт")

    des_key = DesKey(bytes(key, encoding = "utf8"))
    crypted_text = des_key.encrypt(text, padding=True)
    return crypted_text

def Decrypt(key, encrypted_text):
    des_key = DesKey(bytes(key, encoding = "utf8"))
    return des_key.decrypt(encrypted_text, padding=True)
