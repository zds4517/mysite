from django.db import models
from django.db.models.fields import exceptions
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod,ReadDetail
from django.urls import reverse




class BlogType(models.Model):
    type_name = models.CharField(max_length=15, verbose_name='类别名称')
    def __str__(self):
        return self.type_name

class Blog(models.Model,ReadNumExpandMethod):
    title = models.CharField(verbose_name='标题',max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=models.CASCADE,verbose_name='类别')
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者')
    read_details = GenericRelation(ReadDetail)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    last_updated_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    def get_url(self):
        return reverse('blog_detail',kwargs={'blog_pk':self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<博客： %s>" % self.title
    class Meta:
        ordering = ['-created_time']
