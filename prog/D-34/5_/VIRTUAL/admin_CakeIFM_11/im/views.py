from django.http import HttpResponse

import datetime
from django import template


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    
#     t = template.Template("<html><body>Current date and time {{ now }}</body></html>")
    t = template.loader.get_template('im/datetime.html')
    
    c = template.Context({'now': now})
    html = t.render(c)
    return HttpResponse(html)
#     return HttpResponse("Hello Django (new urls.py file)")
