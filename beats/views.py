from django.views.generic import ListView

from beats.models import Beat


class AllBeatsList(ListView):
    model = Beat
    template_name = "beats/all_beats_list.html"
    paginate_by = 5
    # context_object_name = "all_posts"
    queryset = Beat.objects.order_by('-pk')
    ordering = ("-pk",)
