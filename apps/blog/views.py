from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from apps.blog.models import MyBlog
from utils.mixin import LoginRequiredMixin as loMxi
import markdown


# Create your views here.
# class blog_list(loMxi, View):
class blog_list(View):
    def get(self, request):
        context = {
            'all_blog_list': MyBlog.objects.all(),
            'page': 'blog_list',
        }
        return render(request, 'blog_list.html', context)

    def post(self, request):
        return render(request, '404.html')


# class blog_details(loMxi, View):
def blog_details(request, blog_id):
    # context = {'blog_details': get_object_or_404(MyBlog, id=blog_id)}
    context = MyBlog.objects.get(id=int(blog_id))
    context.content = markdown.markdown(context.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    context = {'blog_details': context}
    return render(request, 'blog_details.html', context)


    # def post(self, request):
    #     return render(request, '404.html')



