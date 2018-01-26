from django.http import HttpResponse
import datetime
from django import template
# from django.shortcuts import render_to_response
from django.shortcuts import render

import os

import sys
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

from libs import libs
from libs_31 import test_31

import numpy as np
from sympy import *
# import sympy as sp

import matplotlib.pyplot as plt

import subprocess

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

def exec_Numbering__Test_1(request):
    
    #ref https://stackoverflow.com/questions/204017/how-do-i-execute-a-program-from-python-os-system-fails-due-to-spaces-in-path answered Oct 15 '08 at 8:37
    command = "C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe"  #=>

    arg1 = "C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials/1_/1_1.3.py"
#     arg2 = "numbering"
     
    cmd_Full = [command, arg1]  #=> 
#     cmd_Full = [command, arg1, arg2]  #=> 
    
    res = test_31.test_1()
#     res = subprocess.call(cmd_Full)
     
    #debug
    #ref https://stackoverflow.com/questions/4558879/python-django-log-to-console-under-runserver-log-to-file-under-apache cardamom Jul 7 '17 at 11:25
#     print >>sys.stderr, 'Goodbye, cruel world!'
#     dbg = "[%s:%d] messsage" % (os.path.basename(libs.thisfile()), libs.linenum())
#     
#     print(dbg, file=sys.stderr)
#     print("Goodbye cruel world!", file=sys.stderr)
#     print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , "this is.")
#         , file=sys.stderr)
    msg = "However there are other options"
#     print("[%s:%d] %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , msg
#          )
#         
#         , file=sys.stderr)

    print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , msg
        ), file=sys.stderr)
     
    return HttpResponse(res, content_type='text/plain')
    
#/def exec_Numbering__Test_1(request):

def exec_Numbering(request):
    
    #ref https://stackoverflow.com/questions/14503062/how-do-i-serve-a-text-file-from-django
#     content = "abc"
    
    '''###################
        exec : numbering        
    ###################'''
    return exec_Numbering__Test_1(request)
    
    
#     res = sys.exec()
#     res = sys.exec()
#     
#     #ref https://stackoverflow.com/questions/204017/how-do-i-execute-a-program-from-python-os-system-fails-due-to-spaces-in-path answered Oct 15 '08 at 8:37
#     command = "C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe"  #=>
# #     command = "C:/WORKS_2/Programs/Python/Python_3.5.1/python.exe"  #=>
# #     command = "C:\WORKS_2\g.bat"  #=>
# #     arg1 = "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_\test.py"
# #     arg1 = "C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials/1_/test.py"
# #     arg2 = "> abc.txt"
# #     arg1 = "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_python 1_1.3.py"
#     arg1 = "C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials/1_/1_1.3.py"
#     arg2 = "numbering"
# #     arg1 = "C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials/1_/test.py >"
# #     arg2 = "abc.txt"
# #     arg2 = "abcde"
# #     arg1 = "s"
#     
#     cmd_Full = [command, arg1, arg2]  #=> 
# #     cmd_Full = [command, arg1]  #=> see email
# #     cmd_Full = [command]  #=>    #=> output done
# #     cmd_Full = [command, arg1]  #=> no output
# #     command = "C:\WORKS_2\g.bat s"  #=> FileNotFoundError at /blog/exec_Numbering/
# #     command = "C:\WORKS_2\g.bat s"  #=> FileNotFoundError at /blog/exec_Numbering/
# #     command = "C:\WORKS_2\g.bat"    #=> works
# #     command = "C:\WORKS_2\g.bat s > tmp.log"
#     res = subprocess.call(cmd_Full)
# #     res = subprocess.call([command])
# #     res = subprocess.call(['echo yes'])    #=> FileNotFoundError at /blog/exec_Numbering/
# #     res = subprocess.call(['C:\\WORKS_2\\r.bat'])
#     
#     return HttpResponse(res, content_type='text/plain')
#     return HttpResponse(content, content_type='text/plain')
    
#/def exec_Numbering(request):

def mindmap_ops(request):
    
    '''###################
        data        
    ###################'''
    now = datetime.datetime.now()
    
    
    '''###################
        render        
    ###################'''
    return render(request, 'blog/mindmap_ops.html', {'now': now })
    
#     return
    
#/def mindmap_ops():