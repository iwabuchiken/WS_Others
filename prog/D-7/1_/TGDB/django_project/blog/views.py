from django.http import HttpResponse
import datetime
from django import template
# from django.shortcuts import render_to_response
from django.shortcuts import render

import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
from libs import libs

import numpy as np
from sympy import *
# import sympy as sp

import matplotlib.pyplot as plt


def test_1__Plot():
    
#     print ("[%s:%d] messsage" % (os.path.basename(libs.thisfile()), libs.linenum()))
    
    cross_X = [x for x in range(100)]
    cross_Y = [y for y in range(100)]

    plt.plot(cross_X, cross_Y, 'ro')
    plt.show()

    
    return None
    
#/def test_1__Plot():

def test_2__WriteFile():
    
        ### write file
    dpath = "./blog/data"
#     dpath = "./blog"
    fname_Out = "test.%s.txt" % (libs.get_TimeLabel_Now())
#     fname_Out = "./test.%s.txt" % (libs.get_TimeLabel_Now())
    
    fpath = "%s/%s" % (dpath, fname_Out)
    
    f = open(fpath, "w")
#     f = open(fname_Out, "w")
#     f = open("test.txt", "w")
    
    f.write("yes\n")
    
    f.close()
    
    return fpath
    
#/def test_2__WriteFile():

def index(request):
    
    '''###################
        experi        
    ###################'''
    ### plot
#     test_1__Plot()
    msg = test_2__WriteFile()
    
#     return HttpResponse("<a href='https://overiq.com/django/1.10/views-and-urlconfs-in-django/#creating-the-first-view'>click</a>")
#     msg = "Hello Django"
#     msg = "Hello Django : %s" % (fpath)
#     msg = "Hello Django : %s" % (fname_Out)
    
    return HttpResponse(msg)
#     return HttpResponse("Hello Django")

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

    return render(request, 'blog/datetime2.html', {'now': now })
#     return render('blog/datetime2.html', {'now': now })
#     return render_to_response('blog/datetime2.html', {'now': now })
#     return render_to_response('blog/datetime.html', {'now': now })

