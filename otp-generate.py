#install twillio
import random
from twilio.rest import Client
otp=random.randint(1000,9999)
print(otp)
account_sid='Accccc45bb678'
auth_token="eghncn778721xyhj"
client=Client(account_sid,auth_token)
message=client.messages.create(
    body='Your OTP is' + str(otp),
    from='+239934190',
    to="+918867779863"
)
print(message.sid)