from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from rest_framework.permissions import( 
     AllowAny,
     IsAuthenticated
)
from rest_framework.parsers import (
     JSONParser,
     FileUploadParser,
     FormParser,
     MultiPartParser
)
from .models import Profile
from django.http import HttpRequest
from django.contrib.auth import authenticate
from .validation import (
     ValidateRegistration,
     Register
)
from rest_framework import status


'''
-----------------------------------------------------------------------------------------Authentication-View-------------------------------------------------------------------------------------------------
**URL["/server/user/auth/"] => returns the authentication token and credentials if valid 
     :request:{
          "username":... ,
          "password":...
     }(POST)
     :response:
          {"auth_status":"success","auth_data":{"auth_token":"Token ..."}}} -> authentication status successfull
          {"auth_status":"exception""info":{...}}} -> database integrity error / other exceptions
          {"auth_status":"denied"} -> authentication failed, onvalid credentials provided
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

class AuthenticationView(APIView):
     permission_classes=[
          AllowAny
     ]
     
     def post(self, request:HttpRequest, *args, **kwargs):
          
          # extracting the request data
          try:
               username = request.data.get("username")
               password = request.data.get("password")
          except Exception as e:
               return Response(
                    {
                         "auth_status":"exception",
                         "info":{
                              str(e)
                         }
                    }
               )
               
          print(request)
               
          
          # deletion of pre-authenticated user
          if(request.user.is_authenticated):
               print("entered if")
               try:
                    user = request.user
                    print(user)
                    token = Token.objects.get(user__username = str(user))
                    token.delete()
               except Exception as e:
                    pass
               
          
          # authentication of user
          user_authenticated = authenticate(username = username, password=password)
          
          # response after authnetication
          if(user_authenticated is not None):
               # generating authentication token for authentciated user
               try:
                    auth_token = Token.objects.create(user = user_authenticated)
               except IntegrityError as e:
                    # cathing IntegrityError if the token already exists in the database
                    token = Token.objects.get(user = user_authenticated)
                    token.delete()
                    auth_token = Token.objects.create(user = user_authenticated)
               return Response(
                    {
                         "auth_status":"success",
                         "auth_data":{
                              "auth_token":f"Token {auth_token}"
                         }
                    }
               )
               
          return Response({"auth_status":"denied"})
     
     
     def get(self, request:HttpRequest,*args, **kwargs):
          # to be implement
          return Response(status=status.HTTP_200_OK)
          
     


'''
-----------------------------------------------------------------------------------------RegistrationView-View-------------------------------------------------------------------------------------------------
**URL["/server/user/register/"] => registers user to the database 
     :request:{
          "username":... ,
          "password":...,
          "email":...,
          "first_name":...,
          "last_name":...,
          "telephone":...,  
     }(POST)
     :response:
          {"status":"success"} -> registration status successfull
          {"status":"exception","info":{...}}} -> database integrity error / other exceptions
          {"status":"denied","validation_data":{..."valid"/"invalid"}} ->  invalid user credentials, returns validation data whcih indicates the validity of the credentials
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''     
class RegistrationView(APIView):
     permission_classes = [
          AllowAny
     ]
     
     def post(self, request:HttpRequest, *args, **kwargs):
          # extracting request data
          try:
               username = request.data.get("username")
               password = request.data.get("password")
               email = request.data.get("email")
               first_name = request.data.get("first_name")
               last_name = request.data.get("last_name")
               telephone = request.data.get("telephone")
          except Exception as e:
               return Response(
                    {
                         "status":"exception",
                         "info":{
                              str(e)
                         }
                    }
               )
               
          user_instance, validation_data = ValidateRegistration.validate(
               username = username,
               password = password,
               email = email,
               first_name = first_name,
               last_name = last_name,
               telephone = telephone
          )
          
          try:
               registration_status = Register.commit_registration(user_instance)
          except Exception as e:
               return Response({"status":"exception", "info":{str(e)}})
          
          if(registration_status is True):
               return Response({"status":"success"})
          return Response({"status": "denied","validation_data":validation_data})


'''
-----------------------------------------------------------------------------------------ProfileManager-View-------------------------------------------------------------------------------------------------
**URL["/server/user/register/"](POST) => sets the user profile and account data
     :request:{
          "img_file":...(File),
          "first_name":...,
          "last_name"...,
          "telephone"...(str)
     }
     :response:
          {"status":"success"} -> registration status successfull
          {"status":"exception","info":{...}}} -> database integrity error / other exceptions
          {"status":"denied","validation_data":{..."valid"/"invalid"}} ->  invalid user credentials, returns validation data which indicates the validity of the credentials
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
class ProfileManagerView(APIView):
     permission_classes = [
          IsAuthenticated
     ]
     
     parser_classes = [
          FormParser,
          MultiPartParser
     ]
     
     def post(self, request:HttpRequest, *args, **kwargs):
          # extracting request data and files 
          try:
               user = request.user
               img_file = request.FILES.get("profile-img")
               first_name = request.data.get("first_name")
               last_name = request.data.get("last_name")
               telephone = request.data.get("telephone")
          except Exception as e:
               return Response({"status":"exception", "info":{str(e)}})
     
          user_profile_object = Profile.objects.get(user = user)
     
          # editing user data in the database
          if(
               not str(first_name).strip() == '' or
               first_name is not None or
               str(first_name).str()!=user.first_name
          ):
               user.first_name = first_name
               user.save()
               
          if(
               not str(last_name).strip() == '' or
               last_name is not None or
               str(last_name).strip()!=user.last_name
          ):
               user.last_name = last_name
               user.save()
               
          if(
               not str(telephone).strip() == '' or
               telephone is not None or
               str(telephone).strip()!=str(user_profile_object.telephone)
          ):
               user_profile_object.telephone = int(telephone)
               user_profile_object.save()
          
          
          
          return Response({"data":{str(type(request.FILES.get("img")))}})
          
          
     
class FriendShipManager(APIView):
     pass