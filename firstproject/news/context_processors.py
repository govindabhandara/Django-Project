from .models import News

def all_news(request):
    return {
        'all_news': News.objects.all()
    }
