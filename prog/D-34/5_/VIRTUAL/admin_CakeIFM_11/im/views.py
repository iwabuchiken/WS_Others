from django.http import HttpResponse

from django.shortcuts import render

import datetime
from django import template

import os, sys

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

from libs import libs
from libs_31 import test_31

######################################## FUNCS
# def test_Request():
def test_Request(request):
    
    print("[%s:%d] %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
             , "=================== @ test_Request")
            , file=sys.stderr)

    print(request, file=sys.stderr)
    
    '''###################
        get params        
    ###################'''
    params = request.GET
    
    print("[%s:%d] params =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(params)
    

#/def test_Request():

# Create your views here.
#ref get request https://django.cowhite.com/blog/working-with-url-get-post-parameters-in-django/
def index(request):
    now = datetime.datetime.now()
    
#     t = template.Template("<html><body>Current date and time {{ now }}</body></html>")
    t = template.loader.get_template('im/index.html')
    
    c = template.Context({'now': now})
    html = t.render(c)
    
    ### test
    test_Request(request)
#     test_Request()
    
    return HttpResponse(html)
#     return HttpResponse("Hello Django (new urls.py file)")

def today_is(request):
    
#     now = datetime.datetime.now()
#     html = "<html><body>Current date and time: {0}</body></html>".format(now)
    now = datetime.datetime.now()
    
# #     t = template.loader.get_template('blog/datetimeeeee.html')
#     t = template.loader.get_template('blog/datetime.html')
# #     t = template.Template("<html><body>Current date and time {{ now }}</body></html>")
#     
#     c = template.Context({'now': now})
#     html = t.render(c)
    
#     return HttpResponse(html)

    return render(request, 'im/datetime2.html', {'now': now })
#     return render(request, 'blog/datetime2.html', {'now': now })
#     return render('blog/datetime2.html', {'now': now })
#     return render_to_response('blog/datetime2.html', {'now': now })
#     return render_to_response('blog/datetime.html', {'now': now })
