import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
leng = raw_input('pswd length')
leng = int(leng)
password = ''
for p in range(leng):
    password += random.choice(chars)
print password