from channels.middleware import BaseMiddleware
from rest_framework.authtoken.models import Token
from asgiref.sync import sync_to_async

'''
Authentication middleware for web scoket protocol
'''
class WebsocketAuthenticationMiddleware(BaseMiddleware):
     def __init__(self, inner):
          self.inner = inner

     async def __call__(self, scope, receive, send):
          # extracting authorization key from request header
          try:auth_key = str(dict(scope["headers"])[b"authorization"])
          except KeyError:
               scope["user"] = "anonymous"
               return await self.inner(scope, receive, send)
          # getting auth value
          auth_token = auth_key.strip().removeprefix("b'Token ").removesuffix("'")
          user = await self.query_user_from_token(str(auth_token))
          if(user is None):
               scope["user"] = "anonymous"
               return await self.inner(scope, receive, send)
          scope["user"] = user 
          return await self.inner(scope, receive, send)
     
     @sync_to_async
     def query_user_from_token(self, token:str):
          if (Token.objects.filter(key = token).exists()):
               return Token.objects.get(key = token).user
          return None
