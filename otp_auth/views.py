from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.contrib.auth import login

# Create your views here.


class LoginNumberOtpAPIView(APIView):
    
    def post(self,request):
        otp = 000000
        ph_no = request.data['ph_no']    
        try:
            user = User.objects.get(username=str(ph_no))
            print(request.user)
            login(request, user)
            print(request.user)
            return Response(otp)
        except:
            return Response('Mobile Not found! Please Signup...',404)
        
     
class RegNumberOtpAPIView(APIView):
    
    def post(self,request):
        otp = 000000
        ph_no = request.data['ph_no']
        
        try:
            user = User.objects.get(username=ph_no)
            login(request, user)    
            return Response('',400)
        except:
            return Response(otp)
        
class CreateAPIView(APIView):   
    def post(self,request):
        ph_no = request.data['ph_no']
        name = request.data['name']
        try:
            user = User.objects.create_user(username = ph_no, password=ph_no[::-1],first_name=name)
        except:
            return Response(None,400)
        ## tokens
        login(request, user)
        return Response(None,200)        
    
    
    
    
    
    