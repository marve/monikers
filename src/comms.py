from twilio.rest import Client
import os

account_sid = os.environ['TWILIO_SID']
auth_token = os.environ['TWILIO_TOKEN']
client = Client(account_sid, auth_token)
from_num = '+12058435812'

def send_mms(to_num, msg, url):
  client.messages \
        .create(
          body=msg,
          from_=from_num,
          to=to_num,
          media_url=[url]
        )