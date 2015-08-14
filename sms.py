#-*- coding:utf-8 -*-
import urllib2
import urllib
import hashlib
import random
m = hashlib.md5()
m.update("cs20150727")
code = random.randint(100000,999999)
content="您的验证码是：%s，有效期为五分钟。如非本人操作，可以不用理会"%code


data = """
<Group Login_Name ="%s" Login_Pwd="%s" OpKind="0" InterFaceID="" SerType="xxxx">
<E_Time></E_Time>
<Item>
<Task>
<Recive_Phone_Number>15721448969</Recive_Phone_Number>
<Content><![CDATA[%s]]></Content>
<Search_ID>111</Search_ID>
</Task>
</Item>
</Group>
""" % ("cs20150727",m.hexdigest().upper(),content.decode("utf-8").encode("GBK"))
print m.hexdigest().upper()
account_Balance = """
<Root Service_Type = "0">
<Item>
<Account_Name>cs20150727</Account_Name>
</Item>
</Root>
"""

cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)


request = urllib2.Request(
    url = r'http://userinterface.vcomcn.com/Opration.aspx',
    headers= {'Content-Type':'text/xml'},
    data = data
)

print opener.open(request).read()

request = urllib2.Request(
    url = r'http://userinterface.vcomcn.com/GetResult.aspx',
    headers= {'Content-Type':'text/xml'},
    data = account_Balance
)

print opener.open(request).read()

data = """
<Group Login_Name ="%s" Login_Pwd="%s" OpKind="51" InterFaceID="" SerType="xxxx">
<E_Time></E_Time>
<Mobile>18602181871</Mobile>
<Content><![CDATA[%s]]></Content>
<ClientID>111</ClientID>
</Group>
""" % ("cs20150727",m.hexdigest().upper(),content.decode("utf-8").encode("GBK"))
"""
request = urllib2.Request(
    url = r'http://userinterface.vcomcn.com/Opration.aspx',
    headers= {'Content-Type':'text/xml'},
    data = data
)
"""
print opener.open(request).read()
