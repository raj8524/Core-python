import http.client as ht
conn=ht.HTTPConnection("api.msg91.com")
payload="""
{"sender":"PUMAOF",
"route":"4",
"country":"91",
"sms":[{
"message":"hello, u have won i crore",
"to":["8867779863"]}]}

"""
headers={
    'authkey':"",
    'content-type':"application/json"
}
conn.request("POST","/api/v2/sendsms?campaign=&response",payload,headers)
res=conn.getresponse()
data=res.read() #byte
print(data.decode("utf-8"))