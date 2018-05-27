from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-create_time')[:num]

@register.simple_tag()
def archives():
    # dates函数返回的是一个列表，列表的每个元素都是一篇文章的创建时间，精确到月份
    return Post.objects.all().dates('create_time','day', order='DESC')


@register.simple_tag()
def get_category():
    return Category.objects.all()