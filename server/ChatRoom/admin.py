from django.contrib import admin
from . models import (
     Room,
     RoomMembership,
     Message,
)

# model registration
admin.site.register(
     [
          Room,
          RoomMembership,
          Message
     ]
)
