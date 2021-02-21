from django.urls import path

from beats.views import BeatDetailView

app_name = "beats"

urlpatterns = [
    path('<int:pk>/<slug:slug>', BeatDetailView.as_view(), name='beat_detail'),
]