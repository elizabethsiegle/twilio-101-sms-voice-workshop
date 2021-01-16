import os
from twilio.rest import Client
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to=os.environ['MY_PHONE_NUMBER'], 
                        from_='+14045864101'
                    )

print(call.sid)