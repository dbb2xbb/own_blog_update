from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 分类标签设计成如下模式：
# 分类id   分类名
# 1       django
# 2       python
class Category(models.Model):
    cate_name = models.CharField(max_length=20)



# 标签id   标签名
# 1       django学习
# 2       python学习
class Tag(models.Model):
    tag_name = models.CharField(max_length=20)


# 标题、
# 正文、
# 摘要、
# 创建时间、
# 最后修改时间、
# 文章作者
class post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    excerpt = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    lastchg_time = models.DateTimeField()
    author = models.CharField(max_length=20)

    # 一个正文（博文）只有一个分类，但一个分类下可以有多个相同类型的博文。
    # 这种一对多的关系，使用外键ForeignKey
    cate = models.ForeignKey(Category)

    # 对于描述文章的标签来说，一个文章可有多个标签描述，同时一个标签也可以对应多个文章。
    # 故使用ManyToManyField的方式,同时文章可以没有标签，因此blank=True
    tag = models.ManyToManyField(Tag,blank=True)

    # User是已经Django已经实现的内置应用，专门处理网站用户的注册、登录等流程。这里用户和博文的关系依然是一对多，
    # 因此使用外键。
    user = models.ForeignKey(User)
