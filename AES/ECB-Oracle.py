import requests as req
import sys

url = 'http://125.235.240.166:20104/encrypt'
index = 47
text = b''

for char in range(36):
    templateCipher = req.post(url, data = {"input": (b'x' * index).hex()}).text[:96]
    for i in range(126, 31, -1):
        templateText = b'x' * index + text + bytes([i])
        res = req.post(url, data = {"input": templateText.hex()}).text[:96]
        if res == templateCipher:
            text += bytes([i])
            index -= 1
            print(text)
            break
