from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
import markdown
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-lastchg_time')
    # all方法的返回值为QuerySet类型（可以想象成类似列表一样的数据结构）
    print(post_list)
    context = {
        'post_list':post_list
    }
    return render(request,'blog/index.html',context)


def detail(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    # 使用markdown修饰文章主体部分
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    context = {
        'post':post,
    }
    return render(request,"blog/detail.html",context)