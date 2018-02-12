from django.http import HttpResponse

from django.shortcuts import render

import datetime
from django import template

import os, sys
from sympy.physics.units.dimensions import action

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

from libs import libs
from libs_31 import test_31

from im.libs_im import cons_im

import subprocess

import copy

import re

import clipboard

import time

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
    
#     ### test
#     test_Request(request)
#     test_Request()
    
    action = "action"
    message = "message"
    
    #ref sorted https://www.pythoncentral.io/how-to-sort-python-dictionaries-by-key-or-value/
#     lo_Commands = cons_im.ImOp.lo_Commands
#     lo_Commands = sorted(cons_im.ImOp.lo_Commands.value)
    lo_Commands = cons_im.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
#     lo_Commands = cons_im.ImOp.lo_Commands.value
    
#     lo_Commands = {}
    
#     for item in sorted(cons_im.ImOp.lo_Commands.value) :
#         
#         lo_Commands[item] = cons_im.ImOp.lo_Commands.value[item]
    
    
    
#     sorted(lo_Commands)
#     lo_Commands = sorted(lo_Commands)
    
#     lo_Commands = cons_im.ImOp.lo_Commands
#     lo_Commands = [
#         
#             cons_im.ImOp.OP_0_1.value,
#             cons_im.ImOp.OP_2_0.value,
#             
#             cons_im.ImOp.OP_4.value,
#             cons_im.ImOp.OP_5.value,
#             
#             cons_im.ImOp.OP_7.value,
#             cons_im.ImOp.OP_8.value,
#         
#         ]
    
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
#     dic = {message : _message}
    
    return render(request, 'im/index.html', dic)

#     return HttpResponse(html)
# #     return HttpResponse("Hello Django (new urls.py file)")

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

def _im_actions__Ops_13(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_13()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        build : command string        
    ###################'''
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)

#     print()
#     print("[%s:%d] _im_actions__Ops_13()" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
    
    '''###################
        subprocess        
    ###################'''
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_2_0(action)

def _im_actions__Ops_12(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_12()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        build : command string        
    ###################'''
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)

    print()
    print("[%s:%d] _im_actions__Ops_11_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
    
    '''###################
        subprocess        
    ###################'''
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_2_0(action)

def _im_actions__Ops_11_1(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_11_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        build : command string        
    ###################'''
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)

    print()
    print("[%s:%d] _im_actions__Ops_11_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
    
    '''###################
        subprocess        
    ###################'''
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_2_0(action)

def _im_actions__Ops_11_0(action, request): # /im/im_action
# def _im_actions__Ops_11_0(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_11_0()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "C:\\WORKS_2\\Programs\\sakura\\sakura.exe"
#     command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
                # OSError: [WinError 193] %1 は有効な Win32 アプリケーションではありません。
#     command = action
    arg1 = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
    
    '''###################
        file : read        
    ###################'''
    fin = open(arg1, "r")
    
    content = fin.read()
    
#     print()
#     print("[%s:%d] content[:100] => '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , content[:100]
#             ), file=sys.stderr)
#     print()
    
    
#     C:\WORKS_2\t c2 
    
    fin.close()
    
    '''###################
        time label        
    ###################'''
    #2018-02-01_16-39-38_000.jpg
    time_Label_Orig = request.GET.get('update', False)
    
    print()
    print("[%s:%d] time_Label_Orig => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , time_Label_Orig
        ), file=sys.stderr)
    print()
    
    '''###################
        validate        
    ###################'''
    ### match
    pat = "\d\d\d\d-\d\d-\d\d_\d\d-\d\d-\d\d_\d\d\d.jpg"
    
    comp = re.compile(pat)
    
    res = comp.match(time_Label_Orig)
    
    if res == None : #if res == None
     
        return "No match"
         
    #/if res == None

    '''###################
        build label        
    ###################'''
    #2018-02-01_16-39-38_000.jpg
    #2018/02/05 12:06:15.000
    tokens = time_Label_Orig.split(".") # 2018-02-01_16-39-38_000 jpg
    
    tokens2 = tokens[0].split("_") # 2018-02-01 16-39-38 000
#     tokens2 = tokens[0].split("_") # 2018-02-01 16-39-38_000
    
#     print()
#     print("[%s:%d] tokens2 => '%s'" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , tokens2
#         ), file=sys.stderr)
    
    # dates
    dates = tokens2[0].split('-') # 2018 02 01
    
    label_Dates = "/".join(dates)
#     label_Dates = dates.join("/")
    
    # time
    times = tokens2[1].split("-") # 16 39 38
#     times = tokens2[1].split("_") # 16-39-38 000
    
    print()
    print("[%s:%d] times => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , times
        ), file=sys.stderr)
    
#     times2 = times[0].split("-") # 16 39 38
#     times2 = times.split("-") # 16 39 38
    
    label_Times = ":".join(times) + "." + tokens2[2] # 16:39:38.000
#     label_Times = ":".join(times2) + "." + times[1]
    
    label_All = "%s %s" % (label_Dates, label_Times)
    
    print()
    print("[%s:%d] label_All => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , label_All
        ), file=sys.stderr)

    '''###################
        file : write        
    ###################'''
    fout = open(arg1, "w")
    
#     content = "C:\\WORKS_2\\t c2 %s\n\n%s\n\n%s" % \
    content = "C:\\WORKS_2\\t c2 %s\n%s\n\n%s" % \
                    (time_Label_Orig, label_All, content)
#     content = "C:\\WORKS_2\\t c2 %s\n\n%s" % (time_Label_Orig, content)
    
    fout.write(content)
    
    fout.close()
    
    print()
    print("[%s:%d] file ==> written : '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , arg1
        ), file=sys.stderr)
    print()
    
    
    '''###################
        clipboard
    ###################'''
    clipboard.copy(label_All)
    
    print()
    print("[%s:%d] clipboard ==> copied" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
#     '''###################
#         open file        
#     ###################'''
# #     cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
#   
#     #debug
#     print()
#     print("[%s:%d] cmd_Full =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#               
#             ), file=sys.stderr)
#     print(cmd_Full)
#       
#     res = subprocess.call(cmd_Full)
#   
#     print("[%s:%d] result (subprocess) =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#               
#             ), file=sys.stderr)
#       
# #     print(res)
     
    return "Updated => %s" % (label_All)
#     return "OK"
#     return None
    
#/def _im_actions__Ops_7(do_Commands[action])

def _im_actions__Ops_11(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_11()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])


def _im_actions__Ops_10_1__TEST(action, request): # /im/im_action

    print("[%s:%d] _im_actions__Ops_10_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    arg1 = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
    
    '''###################
        file : read        
    ###################'''
    fin = open(arg1, "r")
    
    content = fin.read()
    
    fin.close()
    
    '''###################
        time label        
    ###################'''
    #2018-02-01_16-39-38_000.jpg
    str_AddData = request.GET.get('update', False)
    
    print()
    print("[%s:%d] add data => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , str_AddData
        ), file=sys.stderr)
    print()
    
    '''###################
        validate        
    ###################'''
    ### match
    res = str_AddData.startswith("\t'total_data'")
     
    if res == False : #if res == None
        
        print()
        print("[%s:%d] Input ==> doesn't start with \"\t'total_data'\" => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , str_AddData
            ), file=sys.stderr)
      
        return "Input ==> doesn't start with \"\t'total_data'\""
          
    #/if res == None

    '''###################
        build content
    ###################'''
    str_AddData = str_AddData.replace(',', ',\n')
            

    '''###################
        time label
    ###################'''
    time_Label = libs.get_TimeLabel_Now(string_type = "formatted")
    
    '''###################
        file : write        
    ###################'''
    fout = open(arg1, "w")
    
#     content = "### %s\n%s\n%s\n" % \
#     content = "### %s\n%s\n%s\n\n" % \
    content = "### %s\n%s\n\n%s" % \
                    (time_Label, str_AddData, content)
#     content = "C:\\WORKS_2\\t c2 %s\n%s\n\n%s" % \
#                     (time_Label_Orig, label_All, content)
#     content = "C:\\WORKS_2\\t c2 %s\n\n%s\n\n%s" % \
#     content = "C:\\WORKS_2\\t c2 %s\n\n%s" % (time_Label_Orig, content)
    
    fout.write(content)
    fout.write("\n")
    #test
    fout.write("done\n")
    
    fout.close()
    
    print()
    print("[%s:%d] file ==> written : '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , arg1
        ), file=sys.stderr)
    print()
    
    return "Done"

#/def _im_actions__Ops_10_1__TEST(action): # /im/im_action
    
def _im_actions__Ops_10_1(action, request): # /im/im_action
# def _im_actions__Ops_10_1(action): # /im/im_action
    
    alert = _im_actions__Ops_10_1__TEST(action, request)
    
#     print("[%s:%d] _im_actions__Ops_10_1()" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
#     
#     #debug
#     print()
#     print("[%s:%d] action => '%s'" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , action
#             ), file=sys.stderr)
#     
#     command = "C:\\WORKS_2\\Programs\\sakura\\sakura.exe"
# #     command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
#                 # OSError: [WinError 193] %1 は有効な Win32 アプリケーションではありません。
# #     command = action
#     arg1 = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
#     
# #     cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
# 
#     #debug
#     print()
#     print("[%s:%d] cmd_Full =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     print(cmd_Full)
#     
#     res = subprocess.call(cmd_Full)
# 
#     print("[%s:%d] result (subprocess) =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print(res)
    
    return alert
#     return "Done"
#     return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])


def _im_actions__Ops_10(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_10()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])


def _im_actions__Ops_9_1(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_9_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "C:\\WORKS_2\\Programs\\sakura\\sakura.exe"
#     command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
                # OSError: [WinError 193] %1 は有効な Win32 アプリケーションではありません。
#     command = action
    arg1 = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
    
#     cmd_Full = [command]  #=> 
    cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
#     print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])

def _im_actions__Ops_9(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_8()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])

def _im_actions__Ops_8(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_8()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])

def _im_actions__Ops_7(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_5()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_7(do_Commands[action])

def _im_actions__Ops_5(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_5()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_OTHERS.value, action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/_im_actions__Ops_5()

def _im_actions__Ops_4(): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_4()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    command = "C:\\WORKS_2\\WS\\Eclipse_Luna\\Cake_IFM11\\lib\\others\\edit_memos.8.open-csv-file.bat"
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_2_0(action)

# def _im_actions__Ops_2_0(): # /im/im_action
def _im_actions__Ops_2_0(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_2_0()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    '''###################
        build : command string        
    ###################'''
    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
#     command = "C:\\WORKS_2\\Programs\\sakura\\sakura.exe"
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
#     command = "C:\\WORKS_2\\Programs\\sakura\\sakura.exe"
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\\"3-1) add memo.txt\""
#     command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\\"3-1) add memo.txt\""
#     command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\'3-1) add memo.txt'"
#     command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
#     command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\test.bat"
#     command = "'C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\test.bat'"
#     command = "'C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\2-0) edit_memos.9-0.bat'"

    print()
    print("[%s:%d] _im_actions__Ops_2_0()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
    
    '''###################
        subprocess        
    ###################'''
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_2_0(action)

def _im_actions__Ops_1_2(action): # /im/im_action

    print("[%s:%d] _im_actions__Ops_1_2()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\%s" % (action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/_im_actions__Ops_1()

def _im_actions__Ops_1(action): # /im/im_action

    print("[%s:%d] _im_actions__Ops_2_0()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
    
    #debug
    print()
    print("[%s:%d] action => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , action
            ), file=sys.stderr)
    
    command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\%s" % (action)
#     command = action
#     arg1 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\3-1) add memo.txt"
    
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 

    #debug
    print()
    print("[%s:%d] cmd_Full =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    print(cmd_Full)
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/_im_actions__Ops_1()

# def _im_actions__Ops_0_1(): # /im/im_action
def _im_actions__Ops_0_1(action): # /im/im_action
    
    print("[%s:%d] _im_actions__Ops_0_1()" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    command = "%s\\%s" % (cons_im.FPath.DPATH_CMD_LIB_WS_CAKE_IFM11.value, action)
#     command = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands\\0-1) start xampp, filezilla, open folder, open files.bat"
    cmd_Full = [command]  #=> 
#     cmd_Full = [command, arg1]  #=> 
    
    res = subprocess.call(cmd_Full)

    print("[%s:%d] result (subprocess) =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(res)
    
    return None
    
#     None
    
#/def _im_actions__Ops_2_0(action)

# def _im_actions__Ops(action): # /im/im_action
def _im_actions__Ops(action, request): # /im/im_action
    
    '''###################
        build : dict        
    ###################'''
    do_Commands = {}
#     cons_im.ImOp.lo_Commands.value
    
    lo_Tmp = copy.deepcopy(cons_im.ImOp.lo_Commands.value)
    
    # alert
    alert = None
    
    for item in lo_Tmp :
        
        do_Commands[item[0]] = item[1]
    
    '''###################
        dispatch        
    ###################'''
    if action == cons_im.ImOp.OP_0_1.value : #if action == "2-0"
#     if action == "2-0" : #if action == "2-0"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_0_1(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_1.value : #if action == "2-0"
#     if action == "2-0" : #if action == "2-0"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        
        ## execute
        _im_actions__Ops_1(do_Commands[action])
#         _im_actions__Ops_1(lo_Tmp[int(action)])
#         _im_actions__Ops_1(lo_Tmp[action])
#         _im_actions__Ops_1(action)
        
    elif action == cons_im.ImOp.OP_1_2.value : #if action == "2-0"
#     if action == "2-0" : #if action == "2-0"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        
        ## execute
        _im_actions__Ops_1_2(do_Commands[action])
#         _im_actions__Ops_1(lo_Tmp[int(action)])
#         _im_actions__Ops_1(lo_Tmp[action])
#         _im_actions__Ops_1(action)
        
    elif action == cons_im.ImOp.OP_2_0.value : #if action == "2-0"
#     if action == "2-0" : #if action == "2-0"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_2_0(do_Commands[action])
#         _im_actions__Ops_2_0(action)
#         _im_actions__Ops_2_0()
        
    elif action == cons_im.ImOp.OP_4.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_4()
        
    elif action == cons_im.ImOp.OP_5.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_5(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_7.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_7(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_8.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_8(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_9.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_9(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_9_1.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_9_1(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_10.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_10(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_10_1.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        alert = _im_actions__Ops_10_1(do_Commands[action], request)
#         _im_actions__Ops_10_1(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_11.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_11(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_11_0.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        alert = _im_actions__Ops_11_0(do_Commands[action], request)
#         _im_actions__Ops_11_0(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_11_1.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_11_1(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_12.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_12(do_Commands[action])
        
    elif action == cons_im.ImOp.OP_13.value : #if action == "4"
             
        print("[%s:%d] executing => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
        ## execute
        _im_actions__Ops_13(do_Commands[action])
        
    else : #if action == "2-0"

        print("[%s:%d] Unknown action => %s" % \
                     (os.path.basename(libs.thisfile()), libs.linenum()
                     , action
                     ), file=sys.stderr)
        
    #/if action == "2-0"
    
    return alert
#     return None
    
#/def _im_actions__Ops(request)
    
def im_actions(request): # /im/im_action
    
    time_Start = time.time()
    
    '''###################
        get : params        
    ###################'''
    params = request.GET
    
    print("[%s:%d] params =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(params)
    
    #ref get https://stackoverflow.com/questions/5895588/django-multivaluedictkeyerror-error-how-do-i-deal-with-it answered May 5 '11 at 9:47
    action = request.GET.get('action', False)
#     action = request.GET['action']
    
    print("[%s:%d] action =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    print(action)
    
    now = datetime.datetime.now()
    
    ### message
#     message = ""
    
    ### alert message
    alert = ""
    
    if action == False : #if action == False
    
        message = "no action param"
    
    else : #if action == False
        
        message = "action is => %s" % (action)
        
        print()
        print("[%s:%d] %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
         , message
        ), file=sys.stderr)

        
        ### operations
#         if action == cons_im.ImOp.ACTION_UPDATE_DATE.value : #if action ==
#              

#             _im_actions__Ops(action, request)
#         
#         else : #if action == 
        
        alert = _im_actions__Ops(action, request)
#         _im_actions__Ops(action)
        
        #/if action == 

#         _im_actions__Ops(action)
    
    #/if action == False
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start

    alert = "%s (time : %02.3f sec)" % (alert, time_Elapsed)
#     alert = alert + " (time : %02.3f sec)" % (time_Elapsed)
    
    #debug
    print("[%s:%d] message => '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , message
            ), file=sys.stderr)
    
#     dic = {'action' : action, "message" : message}
    dic = {'action' : action, "message" : message, "alert" : alert}
    
#     dic = {message : _message}
    
    return render(request, 'im/im_actions.html', dic)
#     return render(request, 'im/im_actions.html', {'now': now })
#     return render(request, 'im/im_action.html')
    
#Q/def im_action(request):
    