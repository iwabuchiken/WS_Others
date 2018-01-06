# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\fx\82_\1_
82_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''

import sys
from sympy.solvers.tests.test_constantsimp import C2

sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_/libs')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_/libs/')

import libfx
# import libs
# from libs.libfx import *
# from libs.libfx import *
# from libs import libs
# from libs.libs import *
# from libs import *


import getopt
import os
import inspect

import math as math

import wave
import struct
import numpy as np
from pylab import *

from matplotlib import pylab as plt

import random as rnd

###############################################
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

def exec_prog():
    
#     print "[%s:%d] exec_prog => done" % (__file__, linenum())

    msg = "[%s:%d] exec_prog => done" % (thisfile(), linenum())
#     print "[%s:%d] exec_prog => done" % (thisfile(), linenum())
#     print "[%s:%d] exec_prog => done" % (thisfile(), linenum())
#     print "[%s:%d] exec_prog => done" % (libs.libs.thisfile(), libs.libs.linenum())
#     print "[%s:%d] exec_prog => done" % (libs.thisfile(), libs.linenum())

#def exec_prog()

'''
<usage>
'''
if __name__ == "__main__" :

    '''###################
        validate : help option        
    ###################'''

    '''###################
        get options        
    ###################'''

    '''###################
        evecute        
    ###################'''
    exec_prog()

    #test
    libfx.test_func() # libfx.py
#     test_func() # libfx.py

    #test
#     print(os.environ['PYTHONPATH'].split(os.pathsep))
    print(sys.path)
    
    print
#     msg = "[%s:%d] done" % (___FILE, ___FILE)
    msg = "[%s:%d] done" % (thisfile(), linenum())
    print (msg)
