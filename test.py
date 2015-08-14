from pyDes import *
data = "421181198411021316"
k = des("q3b59Gk7N1SO9517z1B153JN5xy9c31A",ECB, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)
d = k.encrypt(data)
print "Encrypted: %r" % d
print "Decrypted: %r" % k.decrypt(d)
