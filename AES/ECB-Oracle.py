import requests as req
import json as js

url = 'http://aes.cryptohack.org/ecb_oracle/encrypt/'
index = 31
text = ''

for char in range(25):
	templateCipher = js.loads(req.get(url + ('x' * index).encode('hex') + '/').text)['ciphertext'][:64]
	for i in range(126, 31, -1):
		templateText = 'x' * index + text + chr(i)
		res = js.loads(req.get(url + templateText.encode('hex') + '/').text)['ciphertext'][:64]
		if res == templateCipher:
			text += chr(i)
			index -= 1
			break

print text
