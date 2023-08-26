from django.urls import path
from. import views

urlpatterns = [
    path("register/", views.RoomRegistrationView.as_view()),
    path("<str:room_id>/", views.RoomManagerView.as_view())
]