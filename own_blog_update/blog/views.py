from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
    post_list = Post.objects.all().order_by('-lastchg_time')
    # all方法的返回值为QuerySet类型（可以想象成类似列表一样的数据结构）
    print(post_list)
    context = {
        'post_list':post_list
    }
    return render(request,'blog/index.html',context)