from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.http import JsonResponse
import json
from django.core.mail import send_mail
from django.conf import settings
from random import randint

from .models import CustomUser, Otp
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


def signup_view(request):
    return render(request,'signup.html')

def login_view(request):
    return render(request,'login.html')


@login_required(login_url='/users/login/')
def dashboard(request):
    return render(request,'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect(login_view)


@csrf_exempt
def signup_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            obj             = CustomUser()
            obj.email       = data['email']
            obj.phone       = data['phone']
            obj.first_name  = data['first_name']
            obj.last_name   = data['last_name']
            obj.gender      = data['gender']
            obj.save()

            return JsonResponse({
                'status': 'success', 
                'message': 'Signup successfull Please go to login'})

        except IntegrityError as e:
            return JsonResponse({
                'status': 'failed', 
                'message': 'Email or phone number is Alredy exist'})
    else:
        return not_implimented


@csrf_exempt
def login_api(request):
    if request.method == "POST":
        data    = json.loads(request.body)
        email   = data['email']
        try:
            user = CustomUser.objects.get(email = email)
        # User not found
        except CustomUser.DoesNotExist:
            return JsonResponse({
                    'status': 'failed', 
                    'message': 'User not found'})
        if not user:
            return JsonResponse({
                'status': 'failed', 
                'message': 'User not found'})
        # Sending OTP email
        otp = randint(100000, 999999)
        otp_obj = Otp()
        otp_obj.email = email
        otp_obj.otp = otp
        otp_obj.save()
        subject = 'OTP For Login'
        message = 'This is a login otp main your otp is ' + str(otp)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        try:
            send_mail( subject, message, email_from, recipient_list, fail_silently=False)
        except:
            print(message)
        return JsonResponse({
                'status': 'success', 
                'message': 'Otp Sent to your E-mail '+email})
    else:
        return not_implimented

@csrf_exempt
def validate_otp_api(request):
    if request.method == "POST":
        data    = json.loads(request.body)
        email   = data['email']
        otp = Otp.objects.filter(email=email).order_by('-id')[0]
        if otp:
            if str(otp.otp) == str(data['otp']):
                user = CustomUser.objects.get(email=email)
                login(request, user)
                return JsonResponse({
                        'status': 'success', 
                        'message': 'OTP Verification successfull'})
            else:
                email=request.POST.get('email')
                return JsonResponse({
                        'status': 'failed', 
                        'message': 'OTP Expired'})
        else:
            JsonResponse({
                    'status': 'failed', 
                    'message': 'OTP Not Found Please generate OTP'})
    else:
        return not_implimented


def not_implimented():
    return JsonResponse({
                'status': 'failed', 
                'message': 'This method not implimented yet'})