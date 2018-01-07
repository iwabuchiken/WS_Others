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
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_/libs')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_/libs/')

# import libfx
# import libs
# from libs.libfx import *
# from libs.libfx import *
from libs import libs
# from libs.libs import *
# from libs.libs import *
# from libs import *
from libs import libfx


import getopt
import os
import inspect

import math as math

# import wave
import struct
# import numpy as np
# from pylab import *

# from matplotlib import pylab as plt

import random as rnd

###############################################

def exec_prog():
    
    '''###################
        get data        
    ###################'''
    fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=>

    id_Start    = 195
    id_End      = 202

    header_Length = 3
    skip_Header=True

    result = libfx.get_ChartData_CSV_Between(\
                    fname_In, id_Start, id_End, header_Length, skip_Header)
#     result = libfx.get_ChartData_CSV_Between(fname_In, id_Start, id_End)
    
    print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result)
    
    
    print "[%s:%d] exec_prog => done" % (libs.thisfile(), libs.linenum())

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

    print
#     msg = "[%s:%d] done" % (___FILE, ___FILE)
#     msg = "[%s:%d] done" % (thisfile(), linenum())
    msg = "[%s:%d] get_ChartData_Between(fname, id_Start, id_End) => done" % (libs.thisfile(), libs.linenum())
    print (msg)
