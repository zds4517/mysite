from django import template
from django.contrib.contenttypes.models import ContentType
from ..forms import CommentForm
from ..models import Comment
register = template.Library()

#评论数整理
@register.simple_tag
def get_comment_count(obj):
    content_type = ContentType.objects.get_for_model(obj)
    return Comment.objects.filter(content_type=content_type, object_id=obj.pk).count()
#评论提交表单单独在这里设置
@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    data = {}
    data['content_type'] = content_type.model
    data['object_id'] = obj.pk
    data['reply_comment_id'] = 0
    form = CommentForm(initial=data)
    return form

@register.simple_tag
def get_comment_list(obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments = Comment.objects.filter(content_type=content_type, object_id=obj.pk, parent=None)
    return comments.order_by('-comment_time')