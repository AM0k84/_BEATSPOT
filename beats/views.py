from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.http import JsonResponse


from beats.models import Beat


class BeatDetailView(DetailView):
    model = Beat
    template_name = 'beats/beat_detail.html'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs['slug']
        return reverse_lazy('beats:beat_detail', kwargs={'pk': pk, 'slug': slug})


def like_beat(request):
    user = request.user
    if request.method == "POST":
        beat_id = request.POST.get("beat_id")
        beat_obj = Beat.objects.get(id=beat_id)
        if user not in beat_obj.likes.all():
            beat_obj.likes.add(user)
        else:
            beat_obj.likes.remove(user)
    return JsonResponse({"status": "ok", "likes_number": beat_obj.likes.count()})