from hitcount.views import HitCountDetailView

from users.models import Profile


class ProfileDetailView(HitCountDetailView):
    model = Profile
    template_name = "profile/profile.html"
    count_hit = True
