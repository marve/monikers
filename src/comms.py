from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)
from_num = os.environ['TWILIO_NUMBER']

def send_mms(to_num, msg, url):
  client.messages \
        .create(
          body=msg,
          from_=from_num,
          to=to_num,
          media_url=[url]
        )