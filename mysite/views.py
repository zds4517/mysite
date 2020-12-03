import datetime
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
from read_statistics.utils import get_seven_days_read_data,get_today_hot_data,get_yesterday_hot_data
from django.core.cache import cache
from django.contrib.contenttypes.models import ContentType
from blog.models import Blog


def get_7_days_hot_blogs():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    blogs = Blog.objects.filter(read_details__date__lt=today,read_details__date__gte=date).values('id','title').annotate(read_num_sum = Sum('read_details__read_num')).order_by('-read_num_sum')
    return blogs[:7]

def home_page(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    read_nums,dates = get_seven_days_read_data(blog_content_type)
    #获取七天热门博客的缓存数据
    hot_blogs_for_7_data = cache.get('hot_blogs_for_7_data')
    if hot_blogs_for_7_data is None:
        hot_blogs_for_7_data = get_7_days_hot_blogs()
        cache.set('hot_blogs_for_7_data',hot_blogs_for_7_data,3600)

    context = {}
    context['dates'] = dates
    context['read_nums'] = read_nums
    context['today_hot_data'] = get_today_hot_data(blog_content_type)
    context['yesterday_hot_data'] = get_yesterday_hot_data(blog_content_type)
    context['hot_blogs_for_7_data'] = get_7_days_hot_blogs()
    return render(request,'home.html',context)

