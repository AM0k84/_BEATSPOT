from django.urls import path

from users.views import user_follow

app_name = "users"

urlpatterns = [
    path("/follow/", user_follow, name='user_following'),
]
