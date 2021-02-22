from django.http import JsonResponse
from django.views.generic import ListView
from hitcount.views import HitCountDetailView

from users.models import Profile, UserFollowing

class ProfileDetailView(HitCountDetailView):
    model = Profile
    template_name = "users/profile.html"
    count_hit = True


def follow_user(request):
    user = request.user
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        user_obj = Profile.objects.get(id=user_id)

        if user not in user_obj.followers.all():
            UserFollowing.objects.get_or_create(following_from=user, follow_to=user_obj)
        else:
            UserFollowing.objects.filter(following_from=user, follow_to=user_obj).delete()
    return JsonResponse({"status": "ok", "followers_number": user_obj.followers.count()})


class FollowersList(ListView):
    """All users who follow User"""
    template_name = "users/followers_list.html"
    model = Profile

    def get_queryset(self):
        queryset = Profile.objects.get(slug=self.kwargs["slug"]).follow_to.all()
        return queryset


class FollowedList(ListView):
    """All users who User follow"""
    template_name = "users/followed_list.html"
    model = Profile

    def get_queryset(self):
        queryset = Profile.objects.get(slug=self.kwargs["slug"]).following_from.all()
        return queryset
