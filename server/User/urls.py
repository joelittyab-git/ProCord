from django.urls import path
from . import views

'''
     -Authentication:
          [DESCRIPTION]:URL endpoints to authenticate user according to the credentials provided
          [POST]:{username:..., password:...} -> returns 
               :response:
                    {"auth_status":"success","auth_data":{"auth_token":"Token ..."}}} -> authentication status successfull
                    {"auth_status":"exception""info":{...}}} -> database integrity error / other exceptions
                    {"auth_status":"denied"} -> authentication failed, onvalid credentials provided
'''
urlpatterns = [
    path("auth/", views.AuthenticationView.as_view())   
]