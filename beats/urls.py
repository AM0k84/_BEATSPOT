from django.urls import path

from beats.views import AllBeatsList

app_name = "beats"

urlpatterns = [
    path("all/", AllBeatsList.as_view(), name="all_beats_list"),
]