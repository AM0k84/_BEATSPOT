
from django.urls import path

from posts.models import Post
from posts.views import AllPostsList
# from el_pagination.views import AjaxListView

urlpatterns = [
    # path('all/', AjaxListView.as_view(model=Post), name='all_posts_list'),
    path('all/', AllPostsList.as_view(), name='all_posts_list'),
]
