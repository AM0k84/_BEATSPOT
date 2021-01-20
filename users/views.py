from django.http import JsonResponse
from django.shortcuts import redirect
from hitcount.views import HitCountDetailView

from users.models import Profile, UserFollowing


class ProfileDetailView(HitCountDetailView):
    model = Profile
    template_name = "profile/profile.html"
    count_hit = True


# def follow_user(request):
#     user = request.user
#     if request.method == 'POST':
#         user_id = request.POST.get('user_id')
#         user_obj = Profile.objects.get(id=user_id)
#         if user not in user_obj.followers.all():
#             UserFollowing.objects.get_or_create(following_from=user, follow_to=user_obj)
#         else:
#             UserFollowing.objects.filter(following_from=user, follow_to=user_obj).delete()
#         return redirect('profile', slug=user_obj.slug)


def follow_user_ajax(request):
    user = request.user
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_obj = Profile.objects.get(id=user_id)

        if user not in user_obj.followers.all():
            UserFollowing.objects.get_or_create(following_from=user, follow_to=user_obj)
        else:
            UserFollowing.objects.filter(following_from=user, follow_to=user_obj).delete()
    return JsonResponse({'status': 'ok', 'number': user_obj.followers.count()})
