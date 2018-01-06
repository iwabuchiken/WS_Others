# -*- coding: utf-8 -*-
'''
C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py

'''

import inspect
import os

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
from __builtin__ import str
from sympy.physics.vector.printing import params

def linenum(depth=0):
#     print "line"
     
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno
 
def thisfile(depth=0):
# def _file(depth=0):
#     print "line"
     
    frame = inspect.currentframe(depth+1)
     
    return os.path.basename(frame.f_code.co_filename)
#     return frame.f_code.co_filename


def test_func():
    
    print "[%s:%d] test_func()" % (thisfile(), linenum())
    