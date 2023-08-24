from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpRequest

'''
-----------------------------------------------------------------------------------------RegistrationView-View-------------------------------------------------------------------------------------------------
**URL["/server/room/register/"] => registers the created room and its users to the database
     :request:{"username":... , "password":..., "email":..., "first_name":..., "last_name":...,"telephone":...,  }(POST)
     :response:
          {"status":"success"} -> registration status successfull
          {"status":"exception","info":{...}}} -> database integrity error / other exceptions
          {"status":"denied","validation_data":{..."valid"/"invalid"}} ->  invalid user credentials, returns validation data whcih indicates the validity of the credentials
          
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
''' 
class RoomRegistration(APIView):
     permission_classes = [
          IsAuthenticated,
     ]
     
     def post(self, request:HttpRequest, *args, **kwargs):          
          user = request.user
          room_name = request.data.get("name")
          room_description = request.data.get("description")
          participant_list = request.data.get("users")
          
          return Response({"data":str(request.data)})
          
          
     
     