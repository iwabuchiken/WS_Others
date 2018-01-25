from django.http import HttpResponse
import datetime

import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
from libs import libs

def index(request):
    
    '''###################
        experi        
    ###################'''
    fname_Out = "./test.txt"
    
    f = open(fname_Out, "w")
#     f = open("test.txt", "w")
    
    f.write("yes\n")
    
    f.close()
    
    
    
    
#     return HttpResponse("<a href='https://overiq.com/django/1.10/views-and-urlconfs-in-django/#creating-the-first-view'>click</a>")
    msg = "Hello Django : %s" % (fname_Out)
    
    return HttpResponse(msg)
#     return HttpResponse("Hello Django")

def today_is(request):
    now = datetime.datetime.now()
    html = "<html><body>Current date and time: {0}</body></html>".format(now)
    return HttpResponse(html)

