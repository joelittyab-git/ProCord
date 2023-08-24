from django.contrib.auth.models import User
from . models import Profile
from .exceptions import DatabaseOperationException

'''
Instance of a user which is used for validating registration
'''
class UserInstance(object):
     
     admin = False
     
     def __init__(
          self,
          username:str,
          email:str,
          password:str,
          telephone:str,
          first_name:str,
          last_name:str,
          validation_data:dict
     ) -> None:
          self.username = username
          self.email = email
          self.password = password
          self.telephone = telephone
          self.first_name = first_name
          self.last_name = last_name
          self.validation_data = validation_data
          self.__check_validation(validation_data)
          

     '''
     Checks if all the fields are valid in the validation dictionary
     '''
     def __check_validation(self,val:dict):
          for status in val:
               if(val[status] != "valid"):
                    self.is_valid = False
                    return
               self.is_valid = True
          
          
          

class ValidateRegistration():
     
     '''
     Method to validate user credentials on request to register to the database
     '''
     def validate(**kwargs) ->(UserInstance,dict):
          username = kwargs["username"]
          password = kwargs["password"]
          email = kwargs["email"]
          first_name = kwargs["first_name"]
          last_name = kwargs["last_name"]
          telephone = kwargs["telephone"]
          
          val_dict = {
               username : "valid",
               email:"valid",
               password:"valid"
          }
          
          # validating email and username to be unique
          if(User.objects.filter(username=username).exists()):val_dict[username] = "invalid"
          if(User.objects.filter(email = email).exists()):val_dict[email] = 'invalid'
          
          # returning user instance
          return (
               UserInstance(
                    username=username,
                    password=password,
                    email=email,
                    telephone=telephone,
                    first_name=first_name,
                    last_name=last_name,
                    validation_data=val_dict
               ),
               val_dict
          )
          
          
class Register:
     
     '''
     A method to commit the passed user instance to the database after checking validity status stored in the user instance
     '''
     @staticmethod
     def commit_registration(user:UserInstance) -> bool:
          
          if(user.is_valid==False):
               return False 
          
          # extracting user data from instance
          username = user.username
          email = user.email
          password = user.password
          first_name = user.first_name
          last_name = user.last_name
          telephone = user.telephone
          
          
          # creating user model
          try:               
               user_model = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name = first_name,
                    last_name = last_name 
               )
               user_model.save()
               
               # creating a prfoile for user
               user_profile = Profile.objects.create(
                    user = user_model,
                    telephone = telephone
               )
               user_profile.save()
          except Exception as e:
               raise DatabaseOperationException(f"User.validation.Register -> {e}")
          return True
          

