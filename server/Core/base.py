from rest_framework.authentication import TokenAuthentication

class TokenAuth(TokenAuthentication):
     keyword = 'Token'

class BaseConfiguration:
     REST_FRAMEWORK_CONFIGURATION = {
          'DEFAULT_PERMISSION_CLASSES': [
               'rest_framework.permissions.AllowAny'
          ],
          'DEFAULT_AUTHENTICATION_CLASSES': [
               'Core.base.TokenAuth',
          ]
     }
     
