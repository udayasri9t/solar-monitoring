from dotenv import load_dotenv
load_dotenv()

import os
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
FROM_PHONE = os.getenv("TWILIO_FROM")
TO_PHONE = os.getenv("TWILIO_TO")

def send_sms_alert(message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=FROM_PHONE,
        to=TO_PHONE
    )


