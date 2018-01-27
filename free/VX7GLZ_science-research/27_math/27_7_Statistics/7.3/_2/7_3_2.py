# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_7_Statistics\7.3\_2
7_3_2.py

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
from sympy import *
# import sympy as sp
import matplotlib.pyplot as plt

#ref https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.pearsonr.html
from scipy import stats

import copy

###############################################

def test_1_2(fout, a, b):

    '''###################
        prep
    ###################'''
#     lo_Tmp = []
    lo_Final = []
    
    for i in range(10):
        # tmp list
        lo_Tmp = []
        
        ### copy a
        #ref copy https://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list answered Apr 10 '10 at 8:55
        a_ = copy.copy(a)
    
        lo_Tmp.append(i)
        
        a1 = stats.pearsonr(a_, b)
        
        a_[i] /= 2.0
        
        a2 = stats.pearsonr(a_, b)
        
        a_[i] = 0
        
        a3 = stats.pearsonr(a_, b)
        
        ### append
        lo_Tmp.append(a1)
        lo_Tmp.append(a2)
        lo_Tmp.append(a3)
        
        ### append
        lo_Final.append(lo_Tmp)
        
    #/for i in range(9):

    #debug
    print()
    print("[%s:%d] lo_Final\n" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    print(len(lo_Final))
    print()
    
    '''###################
        write        
    ###################'''
    fout.write("index\t=1.0\t/2.0\t=0")
    fout.write("\n")

    
    for item in lo_Final:
    
#         print(item[0])
#         print('\t')
#         print('\n')
        
        fout.write("%d\t%.4f\t%.4f\t%.4f" % \
              (
                  item[0], item[1][0], item[2][0], item[3][0]
              )
              )
#         print("%.4f %.4f %.4f" % (item[1][0], item[2][0], item[3][0]))
        
        fout.write('\n')
#         print()
        
    #/for item in lo_Final:

    
#     print(lo_Final)

    '''###################
        write        
    ###################'''
#     msg = "[%s:%d] \na[%d]\tcorrel" % \
#                 (
#                     os.path.basename(libs.thisfile()), libs.linenum()
#                     , index_a
#                 )
#     fout.write(msg)
#     
#     fout.write('\n')
#     fout.write('\n')
    
    return None
#/def test_1_1():    
    
def test_1_1(fout, a, b, index_a):
# def test_1_1(fout, a, b):

    '''###################
        correl : a[-1] ---> changes
    ###################'''
    
#     index_a = -2
    
    msg = "[%s:%d] a[%d] ---> changes" % \
                (
                    os.path.basename(libs.thisfile()), libs.linenum()
                    , index_a
                 )
#     msg = "[%s:%d] a[-1] ---> changes" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum())
                
    fout.write(msg)
    
    fout.write('\n')
    
#     msg = "[%s:%d] \na[-1]\tcorrel" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum())
    msg = "[%s:%d] \na[%d]\tcorrel" % \
                (
                    os.path.basename(libs.thisfile()), libs.linenum()
                    , index_a
                )
    fout.write(msg)
    
    fout.write('\n')
    fout.write('\n')
    
    ### array ---> hold correl values
    listOf_Correls = []
    listOf_Alast = []
    
    for i in range(1,11):
#     for i in range(1,11):

        correl = stats.pearsonr(a, b)
        
        ### append
        listOf_Alast.append(a[-1])
        listOf_Alast.append(correl)
        
#         msg = "[%s:%d] %s\t%.4f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
        msg = "%s\t%.4f" % \
                (
                 str(a[index_a])
#                  str(a[-1])
#                  ",".join([str(x) for x in a])
                 , correl[0]
                )
        fout.write(msg)
        
#         fout.write('\n')
        fout.write('\n')
        
        ### decrement
        a[index_a] -= 1
#         a[-1] -= 1
        
    #/for i in range(1,11):

    
    fout.write('\n')
    fout.write('\n')
    
    '''###################
        plot        
    ###################'''
    plt.plot(listOf_Correls)
#     plt.plot(listOf_Alast, listOf_Correls)
    
    plt.show()
    
    
    return None
#/def test_1_1():    
    
def test_1():
    
    '''###################
        ops        
    ###################'''
    a = np.arange(1,11)
    b = np.arange(1,11)
    
    pval = stats.pearsonr(a, b)
    
    print(a)
    
    '''###################
        write file        
    ###################'''
    index_a = -2
    
    fname_Out = "data/pval.a[%d].%s.txt" % \
                    (
                        index_a
                        , libs.get_TimeLabel_Now()
                     
                     )
#     fname_Out = "/data/pval.%s.txt" % (libs.get_TimeLabel_Now())
    
    fout = open(fname_Out, "w")
    
    '''###################
        correl : basic        
    ###################'''
    msg = "[%s:%d] a=\n" % (os.path.basename(libs.thisfile()), libs.linenum())
    fout.write(msg)
#     fout.write("a=\n")
    fout.write(','.join([str(x) for x in a]))
#     fout.write(','.join(a))
    fout.write('\n')
    fout.write('\n')
    
    msg = "[%s:%d] b=\n" % (os.path.basename(libs.thisfile()), libs.linenum())
    fout.write(msg)
#     fout.write("b=\n")
    fout.write(','.join([str(x) for x in b]))
#     fout.write(','.join(b))
    fout.write('\n')
    fout.write('\n')
    
    
    correl = stats.pearsonr(a,b)
    msg = "[%s:%d] correl=%.4f\n" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                 , correl[0]
                 )
    fout.write(msg)
    
    fout.write('\n')
    fout.write('\n')
    
    
    '''###################
        correl : basic        
    ###################'''
#     index_a = -2
    test_1_2(fout, a, b)
#     test_1_1(fout, a, b, index_a)
#     test_1_1(fout, a, b)
    
    
    '''###################
        file : close        
    ###################'''
    fout.close()
    
    return None
    
#/test_1():

def exec_prog(): # from : 20180116_103908
     
    ### test 2
    test_1()
     
#     x = Symbol('x')
#     y = Symbol('y')
#     z = Symbol('z')
#     y_ = Symbol('y_')
#     b = Symbol('b')
#     
#     y = log(b) * b ** 2 / (b - 2)
#     
#     y_ = diff(y, b)
#     
#     print ("[%s:%d] y =>" % (os.path.basename(libs.thisfile()), libs.linenum()))
#     print(y)
#     
#     print ("[%s:%d] y diff =>" % (os.path.basename(libs.thisfile()), libs.linenum()))
#     print(y_)
#     
# #     print ("[%s:%d] solve y diff =>" % (os.path.basename(libs.thisfile()), libs.linenum()))
# #     print(solve(y_, b))
#             #     NotImplementedError: multiple generators [b, log(b)]
#     print()
#     
#     b = 2
#     
#     print ("[%s:%d] b = 2" % (os.path.basename(libs.thisfile()), libs.linenum()))
#     
#     print(y_)
#     
#     print()
#     
#     print ("[%s:%d] use 'subs'" % (os.path.basename(libs.thisfile()), libs.linenum()))
#     
#     print(y_.subs([(b,1)]))
#     
#     print()
    
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