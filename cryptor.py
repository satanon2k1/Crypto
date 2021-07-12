from hashlib import md5
from base64 import b64decode, b64encode
from Crypto.Cipher import AES


# Padding for the input string --not
# related to encryption itself.
BLOCK_SIZE = 16  # Bytes
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def caesar(input, n):
    result = b""
    for i in input:
        result += bytes([(i + n) % 0xff])
    return result

def de_caesar(input, n):
    result = b""
    for i in input:
        result += bytes([(i - n) % 0xff])
    return result


class AESCipher:
    """
    Usage:
        c = AESCipher('password').encrypt('message')
        m = AESCipher('password').decrypt(c)
    Tested under Python 3 and PyCrypto 2.6.1.
    """

    def __init__(self, key):
        self.pkey = key
        self.key = md5(key.encode('utf8')).hexdigest()

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        enc = cipher.encrypt(raw.encode("utf8"))
        enc = caesar(enc, len(self.pkey))
        return b64encode(enc)

    def decrypt(self, enc):
        enc = b64decode(enc)
        dec = de_caesar(enc, len(self.pkey))
        cipher = AES.new(self.key.encode("utf8"), AES.MODE_ECB)
        return unpad(cipher.decrypt(dec)).decode('utf8')


##
# MAIN
# Just a test.
msg = input('Message...: ')
pwd = input('Password..: ')

print('Ciphertext:', AESCipher(pwd).encrypt(msg))
