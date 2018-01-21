# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\bk-\bk-285_Complex_Yasutomi
2_1.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''

'''
    Regex
print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^ +(print )(".+" %.+\(.+\).*)$
^( +)(print )(".+" %.+\(.+\).*)$
$1$2($3)

print "[%s:%d] result => %s" % \
        (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
^( +)(print )(".+" %) \\\r\n(.+)$
$1$2($3)$4$5
$1$2($3 \\\r\n$4)

print ("[%s:%d] all done" % (libs.thisfile(), libs.linenum()))
^( +)(print )(.+)(libs.+file\(\))(.+)
$1$2$3os.path.basename($4)$5
'''


import sys
from sympy.solvers.tests.test_constantsimp import C2

import os

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/bk-')

from libs import libs

from libs import cons

import getopt
import os
import inspect

import math as math

import struct

import numpy as np
from sympy import *
# import sympy as sp

import matplotlib.pyplot as plt

###############################################

def test_2():
    
    print("test_2 =========================")
    
    print()

    ### gen : data
    data = []
    data2 = []
    
    a = 3.00000001
    a2 = 3.0
#     a = 2.00000001
#     a2 = 2.0
#     a = 2.0
    x = 0.2
    x2 = 0.2
    
    ### report
    print()
    print ("[%s:%d] x = %.5f / x2 = %.5f / a = %.9f / a2 = %.9f" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), x, x2, a, a2)
           )

    print()
    
    # initial val
    data.append(x)
    data2.append(x2)
    
    # additions
#     for i in range(1000):
    for i in range(100):

        x = a * (1 - x)
        x2 = a2 * (1 - x2)
        
        print("%d : x = %.5f | x2 = %.5f | x-x2 = %.5f | x/(x - x2) = %.5f | x2/(x - x2) = %.5f" % \
              (i, x, x2, (x - x2), (x / (x - x2)), (x2 / (x - x2))))
        
        data.append(x)
        data2.append(x2)
        
    #/for i in range(100):

    
    ### plotting
    
    # red dashes, blue squares and green triangles
    plt.plot(data, 'ro', label="data")
    plt.plot(data2, 'b^', label="data2")
#     plt.plot(data, label="data")
#     plt.plot(data2, label="data2")
    
    plt.legend()
    
    ax = plt.gca()
    
    #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
#     ax.grid(True)
#     ax.grid(True, which='both')
    ax.grid(which='major', axis='both', linestyle='--')
    ax.grid(which='minor', axis='both', linestyle='--')
    
    plt.show()
    
#/test_2():

def test_1():
    
    print("test_1")
    
    print()
    
    ### plotting
    #ref https://matplotlib.org/users/pyplot_tutorial.html
#     plt.plot([1,2,3,4])
#     plt.ylabel('some numbers')
#     plt.show()
    
#     plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#     plt.axis([0, 6, 0, 20])
#     plt.show()
    
#     plt.plot([x for x in range(10)])
#     plt.ylabel("yes")
#     plt.axis([0, 6, 0, 20])
    
    t = np.arange(0., 2., 0.1)
#     t = np.arange(0., 5., 0.2)
    
    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    
    ax = plt.gca()
    
    #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
#     ax.grid(True)
#     ax.grid(True, which='both')
    ax.grid(which='major', axis='both', linestyle='--')
    ax.grid(which='minor', axis='both', linestyle='--')
    
    plt.show()
    
#/test_2():

def exec_prog(): # from : 
     
    ### test 2
    test_2()
#     test_1()
     
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
'''
<usage>
'''
if __name__ == "__main__" :
# if __name__ == "__main__


    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))


#####################################/EOF