from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse

from django.db import models


# Create your models here.

# class BlogPost(models.Model):
#     title = models.CharField(max_length = 100)
#     author = models.CharField(max_length = 50, blank = True)
#     num = models.IntegerField(auto_created=True)
#     create_time = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(blank=True, null=True)
#     article_catagory = models.CharField(max_length = 50)
#
#     # def get_absolute_urls(self):
#     #     path = reverse('detail', kwargs={'id': self.id})
#     #     return "http://127.0.0.1:8000%s" % path
#
#     def __unicode__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['-create_time']

class BlogPost(models.Model):
    title = models.CharField('标题', max_length=50)
    content = models.TextField(help_text='博客内容')
    pub = models.DateTimeField('发布时间')

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name
        ordering = ["-pub"]

    def __str__(self):
        return self.title
# 管理员操作
class BlogPostAdmin(admin.ModelAdmin):
     list_display = ('title','pub')

admin.site.register(BlogPost,BlogPostAdmin)
# admin.site.register(Article)


class Category(models.Model):
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name=models.CharField('名称',max_length=16)

    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name
    def __unicode__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField('标题',max_length=32)
    author=models.CharField('作者',max_length=16)
    content=models.TextField('内容')
    pub=models.DateField('发布时间',auto_now_add=True)
    category=models.ForeignKey(Category,verbose_name='分类')#多对一（博客--类别）
    tag=models.ManyToManyField(Tag,verbose_name='标签')#(多对多）
    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    blog=models.ForeignKey(Blog,verbose_name='博客')#(博客--评论:一对多)
    name=models.CharField('称呼',max_length=16)
    email=models.EmailField('邮箱')
    content=models.CharField('内容',max_length=240)
    pub=models.DateField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"
    def __unicode__(self):
        return self.content

