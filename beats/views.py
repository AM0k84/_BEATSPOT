from django.views.generic import DetailView
from django.urls import reverse_lazy

from beats.models import Beat


class BeatDetailView(DetailView):
    model = Beat
    template_name = 'beats/beat_detail.html'

    def get_success_url(self):
        pk = self.kwargs["pk"]
        slug = self.kwargs['slug']
        return reverse_lazy('beats:beat_detail', kwargs={'pk': pk, 'slug': slug})
