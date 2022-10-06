from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from profiles.models import userprofiles
from twilio.rest import Client
import random

import profiles.models


# Create your views here.
class otpgen():
    Otp = None
    phone = None

    def send_otp(phone):
        account_ssid = 'ACe6367b4e0523f007dac124700c291ac2'
        auth_token = '8b90f9e0b0595cd3a02c021a8fdb5e7d'
        target_number = '+91' + phone
        print(phone)
        twilio_number = '+19035679739'
        otp = random.randint(1000, 9999)
        otpgen.Otp = str(otp)
        otpgen.phone = phone
        msg = 'GADstore account verification otp is ' + str(otp)
        client = Client(account_ssid, auth_token)
        message = client.messages.create(
            body=msg,
            from_=twilio_number,
            to=target_number,
        )
        print(message.body)
        return True


@never_cache
def otp(request):
    return render(request, 'otp.html')


def loginotp(request):
    obj = otpgen()
    if request.method == "POST":
        Rotp = request.POST['otp']
        Gotp = obj.Otp
        if Rotp == Gotp:
            user = userprofiles.objects.get(phone=obj.phone)
            login(request, user)
            return redirect('/home')
        else:
            messages.error(request, 'Invalid otp, try again !')
            return redirect('/log')
    else:
        messages.error(request, 'Something went wrong, please try again')
        return redirect('/log')
