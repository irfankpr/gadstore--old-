from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache
from twilio.rest import Client
import random


# Create your views here.
class otpgen():
    Otp ='0'
    def send_otp(phone):
        account_ssid = 'ACe6367b4e0523f007dac124700c291ac2'
        auth_token = '83ec83cf91e7746dccd3068371568689'
        target_number = phone
        print(phone)
        twilio_number = '+19035679739'
        otp = random.randint(1000, 9999)
        otpgen.Otp = str(otp)
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

obj=otpgen()
def loginotp(request):
    if request.method=="POST":
        Rotp = request.POST['otp']
        Gotp =obj.Otp
        if Rotp == Gotp:
            return redirect('/home')
        else:
            messages.error(request, 'Invalid otp, try again !')
            return redirect('/log')
    else:
        messages.error(request, 'Something went wrong, please try again')
        return redirect('/log')

