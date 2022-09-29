from django.shortcuts import render
from twilio.rest import Client
import random

# Create your views here.

def send_otp():
    account_ssid = 'ACe6367b4e0523f007dac124700c291ac2'
    auth_token = '7ae99459651b4a1c3fd981bc7c6d092a'
    target_number = '+919656101429'
    twilio_number = '+19035679739'
    otp = random.randint(1000, 9999)
    msg = 'GADstore account verification otp is '+str(otp)
    client = Client(account_ssid, auth_token)

    message = client.messages.create(
        body=msg,
        from_=twilio_number,
        to=target_number
    )
    print(message.body)
