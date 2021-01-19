from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from hitcount.views import HitCountDetailView

from users.models import Profile, UserFollowing





class ProfileDetailView(HitCountDetailView):
    model = Profile
    template_name = "profile/profile.html"
    count_hit = True

@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = Profile.objects.get(id=user_id)
            if action == 'follow':
                UserFollowing.objects.get_or_create(
                    following_from=request.user,
                    follow_to=user
                )
            else:
                UserFollowing.objects.filter(
                    following_from=request.user,
                    follow_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except Profile.DoesNotExist:
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'ok'})
