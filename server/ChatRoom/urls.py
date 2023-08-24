from django.urls import path
from. import views

urlpatterns = [
    path("register/", views.RoomRegistration.as_view())
]
