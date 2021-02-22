from django.urls import path

from beats.views import BeatDetailView, like_beat

app_name = "beats"

urlpatterns = [
    path("likes/", like_beat, name="like_beat"),
    path("<int:pk>/<slug:slug>", BeatDetailView.as_view(), name="beat_detail"),
]
