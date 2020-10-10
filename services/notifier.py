from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
to_phone = os.getenv('TWILIO_PERSONAL_PHONE_NUMBER')
from_phone = os.getenv('TWILIO_ACCOUNT_PHONE_NUMBER')
url = 'http://demo.twilio.com/docs/voice.xml'


def notify_by_phone():
    client = Client(account_sid, auth_token)
    call = client.calls.create(
        url=url,
        to=to_phone,
        from_=from_phone
    )


def notify_by_sms(product, products):
    client = Client(account_sid, auth_token)
    body = product + " - Product in stock! " + products[product]['url']
    message = client.messages.create(
        body=body,
        to=to_phone,
        from_=from_phone,
    )
