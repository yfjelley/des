#coding:utf-8
import binascii
import base64
import pyDes
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
class DES:
    def __init__(self, iv, key):
        self.iv = iv
        self.key = key
        print self.key
    def encrypt(self, data):
        iv = binascii.unhexlify(self.iv)
        key = binascii.unhexlify(self.key)
        k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
        d = k.encrypt(data)
        d = base64.encodestring(d)
        return d
    def decrypt(self, data):
        iv = binascii.unhexlify(self.iv)
        key = binascii.unhexlify(self.key)
        k = pyDes.triple_des(key, pyDes.CBC, iv, pad=None, padmode=pyDes.PAD_PKCS5)
        try:
            data = base64.decodestring(data)
            d = k.decrypt(data)
        except:
            d = ''
        return d
if __name__ == '__main__':
    data = u"杨锋"
    des = DES('3132333435363738','q3b59Gk7N1SO9517z1B153JN5xy9c31A')

    print 'STR: %s' % (data,)
    encryptdata = des.encrypt(data.encode('utf-8'))
    print "ENCODE: %s" % encryptdata
    decryptdata = des.decrypt(encryptdata)
    print "STR: %s" % decryptdata.decode('utf-8')
