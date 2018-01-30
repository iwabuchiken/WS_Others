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

from mm.libs_mm import cons_mm
# from im.libs_mm import cons_mm

import subprocess

import copy


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