from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from beats.models import Beat, BeatLike


def like_beat(request):
    user = request.user
    if request.method == "POST":
        beat_id = request.POST.get("beat_id")
        beat_obj = Beat.objects.get(id=beat_id)
        if user not in beat_obj.likes.all():
            BeatLike.objects.get_or_create(like_from=user, like_to=beat_obj)
        else:
            BeatLike.objects.filter(like_from=user, like_to=beat_obj).delete()
    return JsonResponse({"status": "ok", "likes_number": beat_obj.likes.count()})


class BeatDetailView(DetailView):
    model = Beat
    template_name = "beats/beat_detail.html"

    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs["slug"]
        return reverse_lazy("beats:beat_detail", kwargs={"pk": pk, "slug": slug})


# todo: this will be waiting room for beats like 'wykopalisko'
class AllBeatsList(ListView):
    model = Beat
    template_name = 'beats/all_beats_list.html'
    context_object_name = 'all_beats'
    paginate_by = 2

    def get_queryset(self):
        return self.model.objects.all().order_by('-pk')
