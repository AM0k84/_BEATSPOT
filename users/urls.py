from django.urls import path
from .views import follow_user_ajax
# from users.views import follow_user

app_name = "users"

urlpatterns = [
    #     path("followers/", follow_user, name="follow_user"),
    path("ajax/followers/", follow_user_ajax, name="follow_user_ajax"),
]
