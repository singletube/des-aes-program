
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = "Sixteen byte key"

def Encrypt(key, text_to_encrypt):
    if(len(key) > 16):
        assert("Ключ больше 16 байт")

    if(len(key) < 16):
        assert("Ключ меньше 16 байт")

    cipher = AES.new(key.encode(), AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(text_to_encrypt.encode(), 32))
    return ciphertext

def Decrypt(key, ciphertext):
    if(len(key) > 16):
        return("Ключ больше 16 байт")

    if(len(key) < 16):
        return("Ключ меньше 16 байт")

    cipher = AES.new(key.encode(), AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext, 32)