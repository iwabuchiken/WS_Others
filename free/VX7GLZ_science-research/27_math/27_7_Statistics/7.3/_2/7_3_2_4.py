# coding: utf-8

# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_7_Statistics\7.3\_2\
7_3_2_4.py

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
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/27_math/27_5')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs

from libs import cons

import getopt
import os
import inspect

import math as math

import struct

import numpy as np

import numpy.linalg as la

from sympy import *
# import sympy as sp
import matplotlib.pyplot as plt

#ref https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
from scipy import stats

import copy

###############################################
def test_1():
    
    '''###################
        ops        
    ###################'''
    #ref https://nknon.blogspot.jp/2008/02/blog-post_12.html
    F = np.array([[1,1],[2,1],[3,1],[4,1],[5,1]])
    y = np.array([[8.1],[2.5],[2.1],[3.4],[9.8]])
    
    tF = np.transpose(F)
    tFF = np.dot(tF, F)
    tFF_inv = la.inv(tFF) #tFFの逆行列
#     tFF_inv = la.inverse(tFF) #tFFの逆行列
    tFy = np.dot(tF, y)
    a = np.dot(tFF_inv, tFy)
    
    print(a)
    
    '''###################
        plot        
    ###################'''
    y_ = [x[0] for x in y]
    
    x2 = range(5)
    
    y2_ = [item * a[0] + a[1] for item in x2]
#     y2_ = [item * a[0] for item in x2]
    
    print()
    print("[%s:%d] a[0][1] = %.4f" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , a[0]
#             , a[0][1]
            ), file=sys.stderr)
    print()
#     y2_ = 
    
    print()
    print(y_)
    
    plt.plot(y_, 'b^')
    plt.plot(y2_, 'r*')
#     plt.plot(y2_, 'r-')
#     plt.plot(y_)
    
    ax = plt.gca()
    
    #ref grid https://stackoverflow.com/questions/16074392/getting-vertical-gridlines-to-appear-in-line-plot-in-matplotlib
#     ax.grid(True)
    ax.grid(True, which='both')
#     ax.grid(which='major', axis='both', linestyle='--')
#     ax.grid(which='minor', axis='both', linestyle='--')
    
    plt.show()
    
    '''###################
        return        
    ###################'''
    return None
    
#/test_1():

def exec_prog(): # from : 20180116_103908
     
    ### tests
    test_1()
     
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
if __name__ == "__main__" :
# if __name__ == "__main__


    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))


#####################################/EOF