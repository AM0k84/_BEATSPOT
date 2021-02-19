from django.urls import path

from posts.views import AllPostsList

app_name = "posts"

urlpatterns = [
    path("all/", AllPostsList.as_view(), name="all_posts_list"),
]
