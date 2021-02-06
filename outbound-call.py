import os
from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
    twiml='<Response><Say>AUTO WARRANTY INSURANCE</Say></Response>',
    to=os.environ['MY_PHONE_NUMBER'], 
    from_='+12672042695'
    )

print(call.sid)
