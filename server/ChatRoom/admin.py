from django.contrib import admin
from . models import (
     Room,
     RoomMembership,
     Message,
     MessageReference
)

# model registration
admin.site.register(
     [
          Room,
          RoomMembership,
          Message,
          MessageReference
     ]
)
