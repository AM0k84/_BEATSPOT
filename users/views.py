from users.models import Profile
from hitcount.views import HitCountDetailView


class ProfileDetailView(HitCountDetailView):
    model = Profile
    template_name = 'profile/profile.html'
    count_hit = True
