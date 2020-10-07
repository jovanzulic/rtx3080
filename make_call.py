from twilio.rest import Client
import os
from dotenv import load_dotenv


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
to_phone = os.getenv('TWILIO_PERSONAL_PHONE_NUMBER')
from_phone = os.getenv('TWILIO_ACCOUNT_PHONE_NUMBER')
url = 'http://demo.twilio.com/docs/voice.xml'


def make_call():
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        url=url,
        to=to_phone,
        from_=from_phone
    )
