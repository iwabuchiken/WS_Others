# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_5\31_
31_.py

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
sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/27_math/27_5')

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


###############################################

def test_2():
    
    #ref http://programming.blogo.jp/python/sympy/%E9%96%A2%E6%95%B0%E3%81%AB%E4%BB%A3%E5%85%A5
    #ref search https://duckduckgo.com/?q=python+sympy+%E5%A4%89%E6%95%B0+%E4%BB%A3%E5%85%A5&atb=v84-1__&ia=web
    
    var("a:z")
    var("y_")
    
    y = log(b) * b ** 2 / (b - 2)
    
    y_ = diff(y, b)
    
    print ("[%s:%d] y diff" % (os.path.basename(libs.thisfile()), libs.linenum()))
    
    print(y_)
    
    print()
    
    ### insert val to 'b'
    print()
    print(y_.subs([(b, 3)]))
    #ref http://docs.sympy.org/latest/modules/evalf.html numerical
    print(N(y_.subs([(b, 3)])))
    print()
    
#/test_2():

def exec_prog(): # from : 20180116_103908
     
    ### test 2
    test_2()
     
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
 
# def exec_prog(): # upto : 
#      
#     '''######################################
#         get data : raw csv rows
#     ######################################'''
#     #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
#     #ref https://docs.python.org/3.5/library/enum.html
#     fname_In = cons.FPath.dpath_In_CSV.value \
#             + "/" \
#             + cons.FPath.fname_In_CSV.value
# 
#     header_Length   = 2
#     
#     skip_Header     = False
#  
#     result = libfx.get_ChartData_CSV(\
#                     fname_In, header_Length, skip_Header)
#     
#     ### Validate
#     if result == None : #if result == None
#     
#         print ("[%s:%d] get_ChartData_CSV => Returned 'None'" % \
#                     (libs.thisfile(), libs.linenum()))
# #         print "[%s:%d] get_ChartData_CSV => Returned 'None'" % \
# #                     (libs.thisfile(), libs.linenum())
#         
#         return
#         
#     #/if result == None
#     
#     ### report
#     print()
#     print ("[%s:%d] CSV rows => %d" % (os.path.basename(libs.thisfile()), libs.linenum(), len(result)))
#     print()
#     
#     print ("[%s:%d] row[%d] => %s" % (os.path.basename(libs.thisfile()), libs.linenum(), 0, result[0]))
#     print()
#     
#     '''######################################
#         Conv : CSV rows ---> array of BarData class instances        
#     ######################################'''
# #     aryOf_BarDatas = libfx.conv_CSVRows_2_BarDatas(result)
#     aryOf_BarDatas = libfx.conv_CSVRows_2_BarDatas(result[header_Length:])
#     
#     ### Validate
#     if aryOf_BarDatas == None : #if aryOf_BarDatas == None
#     
#         print ("[%s:%d] aryOf_BarDatas => None" % (os.path.basename(libs.thisfile()), libs.linenum()))
#         print()
#         
#         return
#     #/if aryOf_BarDatas == None
#     
#     '''###################
#         Build data        
#     ###################'''
#     numOf_Sequence = cons.PatternMatch.PATTERNMATCH_NUMOFSEQUENCE_RSI.value
#     
#     rangeOf_Flat    = cons.PatternMatch.RANGE_FLAT_RSI.value
#     
#     flag_UpDown     = cons.PatternMatch.FLAG_UPDOWN_UP.value
#     
#     aryOf_PatternMatched_Nos = libfx.get_AryOf_BarDatas_PatternMatched__RSI(
#                     aryOf_BarDatas, 
#                     numOf_Sequence, 
#                     rangeOf_Flat, 
#                     flag_UpDown)
#     
#     '''###################
#         Report        
#     ###################'''
#     print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
#  
'''
<usage>
'''
if __name__ == "__main__" :
# if __name__ == "__main__


    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))


#####################################/EOF