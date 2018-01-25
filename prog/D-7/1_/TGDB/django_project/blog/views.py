from django.http import HttpResponse


def index(request):
    
#     return HttpResponse("<a href='https://overiq.com/django/1.10/views-and-urlconfs-in-django/#creating-the-first-view'>click</a>")
    return HttpResponse("Hello Django")

