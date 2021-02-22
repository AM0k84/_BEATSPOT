from django.urls import path

from beats.views import BeatDetailView, like_beat, AllBeatsList

app_name = "beats"

urlpatterns = [
    path("likes/", like_beat, name="like_beat"),

    path('all/', AllBeatsList.as_view(), name='all_beats_list'), #todo: change this url to waiting-room for beats
    path("<int:pk>/<slug:slug>", BeatDetailView.as_view(), name="beat_detail"),
]
