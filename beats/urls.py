from django.urls import path

from beats.views import BeatDetailView, like_beat
from users.views import follow_user

app_name = "beats"

urlpatterns = [
    path("like/", like_beat, name="like_beat"),
    path('<int:pk>/<slug:slug>', BeatDetailView.as_view(), name='beat_detail'),

]