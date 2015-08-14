#-*- coding:utf-8 -*-
from descript import DES
from des import desencode
import urllib2,urllib,hashlib,time
from urllib import quote,urlencode
import sys,datetime
reload(sys)
sys.setdefaultencoding( "utf-8" )

userId = 100173
auName = "杨锋"
auId = '421181198411021316'
ts = int(time.time())
md5key="3d19bfgU9y33cOF5g11b131kc3IjJi7g"

d = DES()
d.input_key('q3b59Gk7N1SO9517z1B153JN5xy9c31A')

aun = d.encode(auName)
print aun
aun = desencode('杨锋','q3b59Gk7N1SO9517z1B153JN5xy9c31A')
print aun
aui = d.encode(auId)
print aui
ani = desencode('421181198411021316','q3b59Gk7N1SO9517z1B153JN5xy9c31A')
print aui
parm={
        'userId': 100173,
        'auName' : aun,
        'auId' : aui,
        'reqDate' : datetime.datetime.now(),
        'ts' : int(time.time()),
}

s = urlencode(sorted(parm.iteritems(),key=lambda a:a[0],reverse=False))
m = hashlib.md5()
m.update("userId"+str(userId)+"auName"+auName+"auId"+str(auId)+"ts"+str(ts)+md5key)
sign = m.hexdigest().upper()

cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)

url = "http://121.40.136.150:8080/IdInDataAu/api/spAuthenInfoApi.htm?"

u = url+s+'&'+'sign='+sign
print u
request = urllib2.Request(
    url = u,
    headers= {'Content-Type':'text/xml'},
)

t=opener.open(request).read()

print t.decode("gb2312")

