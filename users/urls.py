from django.urls import path

from users.views import follow_user

app_name = "users"

urlpatterns = [

    path("followers/", follow_user, name="follow_user"),
]
