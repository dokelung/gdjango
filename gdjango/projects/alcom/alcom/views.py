from django.shortcuts import render
from news.models import News

def home(request):
	newss = News.objects.order_by('date')[:5]
	return render(request, 'index.html', locals())