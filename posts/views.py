from django.views.generic import ListView

from posts.models import Post


class AllPostsList(ListView):
    model = Post
    template_name = 'posts/all_posts_list.html'
    paginate_by = 5
    context_object_name = 'all_posts'
    ordering = ('-pk',)
