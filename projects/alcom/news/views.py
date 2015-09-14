from django.shortcuts import render
from news.models import News

def list_news(request):
	newss = News.objects.all().order_by('date')
	return render(request, 'news_list.html', locals())
