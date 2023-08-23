from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.http import HttpRequest
from django.contrib.auth import authenticate


'''
-----------------------------------------------------------------------------------------Authentication-View-------------------------------------------------------------------------------------------------
**URL["/user/auth/"] => returns the authentication token and credentials if valid 
     :request:{"username":... , "password":...}(POST)
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
               return Response({"auth_status":"exception", "info":{str(e)}})
          
          # deletion of pre-authenticated user
          if(request.user.is_authenticated):
               try:
                    user = request.user
                    token = Token.objects.get(user = user)
                    token.delete()
               except Exception as e:
                    pass
               
          
          # authentication of user
          user_authenticated = authenticate(username = username, password=password)
          
          # response after authnetication
          if(user_authenticated is not None):
               # generatin authentication token for authentciated user
               auth_token = Token.objects.create(user = user_authenticated)
               return Response({"auth_status":"success", "auth_data":{"auth_token":f"Token {auth_token}"}})
          return Response({"auth_status":"denied"})
     


'''
-----------------------------------------------------------------------------------------RegistrationView-View-------------------------------------------------------------------------------------------------
**URL["/user/register/"] => registers user to the database 
     :request:{"username":... , "password":..., "email":..., "first_name":..., "last_name":..., }(POST)
     :response:
          {"auth_status":"success","auth_data":{"auth_token":"Token ..."}}} -> authentication status successfull
          {"auth_status":"exception""info":{...}}} -> database integrity error / other exceptions
          {"auth_status":"denied"} -> authentication failed, onvalid credentials provided
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''     
class RegistrationView(APIView):
     permission_classes = [
          AllowAny
     ]
     
     def post(self, request, *args, **kwargs):
          pass

          
     