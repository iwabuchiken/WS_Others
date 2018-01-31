'''###################
    file : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\views.py

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL
env\Scripts\activate.bat

pushd C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects
python manage.py runserver

###################'''

from django.http import HttpResponse, HttpRequest
# from django.http import HttpResponse

from django.shortcuts import render

import datetime
from django import template

import os, sys
from sympy.physics.units.dimensions import action
from pip._vendor.requests.api import request

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

from libs import libs
from libs_31 import test_31

from mm.libs_mm import cons_mm
# from im.libs_mm import cons_mm

import subprocess

import copy

#ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join

#ref https://stackoverflow.com/questions/29304845/how-to-disable-cache-in-django-view
from django.views.decorators.cache import never_cache

from pathlib import Path

################################## FUNCS
def exec_Numbering(request):
    
    '''###################
        requests        
    ###################'''
    dpath = request.GET.get('dpath', False)
    fname = request.GET.get('fname', False)
    
    '''###################
        data        
    ###################'''
    if not dpath == False and not fname == False :
#     if dpath == True or fname == True :
#     if dpath == False or fname == False :
        
        msg = "params obtained"
        
    else :

        msg = "params NOT enough"
        
        
        dic = {
            cons_mm.ExecNumbering.DICKEY_MSG.value : msg,
            cons_mm.ExecNumbering.DICKEY_DPATH.value : dpath, 
            cons_mm.ExecNumbering.DICKEY_FNAME.value : fname,
                }
#         dic = {"msg" : msg, "dpath" : dpath, "fname" : fname}

        print()
        print("[%s:%d] dic => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , dic
            ), file=sys.stderr)
        print()
        
        '''###################
            render : params not sufficient        
        ###################'''
        return render(request, 'mm/exec_Numbering.html', dic)
        
#     msg = None if dpath == False or fname == False else "params obtained"
    
#     print()
#     print("[%s:%d] msg => '%s'" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , msg
#         ), file=sys.stderr)
#     print()


    
    dic = {"msg" : msg, "dpath" : dpath, "fname" : fname}

    print()
    print("[%s:%d] dic => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dic
        ), file=sys.stderr)
    print()

    
    '''###################
        exec numbering        
    ###################'''
    '''###################
        validate : file exists        
    ###################'''
    fpath = os.path.join(dpath, fname)
    
    #ref https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-using-python answered Sep 17 '08 at 12:57
    my_file = Path(fpath)
    
    if not my_file.is_file():

        print()
        print("[%s:%d] file NOT exists : '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath
            ), file=sys.stderr)
        print()
        
        dic[cons_mm.ExecNumbering.DICKEY_MSG.value] = \
                    "File does NOT exist : %s" % (fpath)
        
        '''###################
            render : params not sufficient        
        ###################'''
        
        return render(request, 'mm/exec_Numbering.html', dic)
    
#     '''###################
#         validate : file not used        
#     ###################'''
#    #ref https://stackoverflow.com/questions/7132861/building-full-path-filename-in-python answered Aug 20 '11 at 16:49
#     fpath = os.path.join(dpath, fname)
#     
#     res = libs.is_Open(fpath)
# 
#     print()
#     print("[%s:%d] file opened => '%s'" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , res
#         ), file=sys.stderr)
#     print()
        
    '''###################
        render : params not sufficient        
    ###################'''
    
    return render(request, 'mm/exec_Numbering.html', dic)
    
#/def exec_Numbering(request):
    

    
@never_cache
def numbering(request):
    
    '''###################
        test        
    ###################'''
    ### referer
#     req = HttpRequest()
    
#     print()
#     print("[%s:%d] req.META.get('REQUEST_METHOD ') => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          #ref referer https://stackoverflow.com/questions/40627149/dict-object-has-no-attribute-http-referer answered Nov 16 '16 at 8:32
#         , req.META.get('REQUEST_METHOD ')
#         ), file=sys.stderr)
#     print("[%s:%d] req.META.get('HTTP_REFERER') => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          #ref referer https://stackoverflow.com/questions/40627149/dict-object-has-no-attribute-http-referer answered Nov 16 '16 at 8:32
#         , req.META.get('HTTP_REFERER')
#         ), file=sys.stderr)
#     print("[%s:%d] req.META.get('HTTP_USER_AGENT') => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          #ref referer https://stackoverflow.com/questions/40627149/dict-object-has-no-attribute-http-referer answered Nov 16 '16 at 8:32
#         , req.META.get('HTTP_USER_AGENT')
#         ), file=sys.stderr)
#     print()
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/mm/"
    
    referer_Current = request.META.get('HTTP_REFERER')
#     referer_Current = req.META.get('HTTP_REFERER')
    
    '''###################
        var : list of files        
    ###################'''
    MAIN_DIR = cons_mm.FPath.DPATH_MM_PROJECTS.value
    
    mypath = MAIN_DIR
    
    #ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory answered Jul 8 '10 at 21:01
    lo_Files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    
    print()
    print("[%s:%d] files => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , lo_Files
            ), file=sys.stderr)
    print()
    
    '''###################
        sort list        
    ###################'''
    #ref sort https://stackoverflow.com/questions/4183506/python-list-sort-in-descending-order answered Nov 15 '10 at 10:42
    lo_Files.sort(reverse=False)
#     sorted(lo_Files, reverse = True)

    print()
    print("sorting...")
    print("[%s:%d] files => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , lo_Files
            ), file=sys.stderr)
    print()
    
    '''###################
        dict        
    ###################'''
    msg = "Where to store Django Templates?"
    
    dic = {
        
        "msg" : msg,
        
        "MAIN_DIR" : cons_mm.FPath.DPATH_MM_PROJECTS.value,
        
        "lo_Files" : lo_Files,
        
        }
    
    '''###################
        render        
    ###################'''
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        return render(request, 'mm/numbering.html', dic)
    
    else : #if referer_Current == referer_MM
    
        return render(request, 'mm/numbering_full.html', dic)
    
    #/if referer_Current == referer_MM
    
    
    
#     return render(request, 'mm/numbering.html', dic)
#     return render(request, 'mm/numbering_full.html', dic)
    
#/def numbering(request):

def index(request):

    now = datetime.datetime.now()
    
#     t = template.Template("<html><body>Current date and time {{ now }}</body></html>")
    t = template.loader.get_template('mm/index.html')
    
    c = template.Context({'now': now})
    html = t.render(c)
    
    action = "action"
    message = "message"
    
    #ref sorted https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
    lo_Commands = cons_mm.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
    return render(request, 'mm/index.html', dic)

    
#     return HttpResponse("Hello Django")