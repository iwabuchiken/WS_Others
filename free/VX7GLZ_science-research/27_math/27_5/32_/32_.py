# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_5\32_
32_.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

[logging]
32_.py > tmp.log
python C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\cp_log.py -lmatrix

32_.py > tmp.log && python C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\cp_log.py -lmatrix

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
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_/libs')

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

def test_3_N_Multiply():
    
    #ref http://docs.sympy.org/latest/tutorial/matrices.html
    init_printing(use_unicode=True)
    
    '''###################
        vars        
    ###################'''
    var("a:z")
    
    aryOf_Coordinates = []
    
    '''###################
        ops        
    ###################'''
#     x = 2
#     y = 1
#     x = 2
    x = 2
    y = 2
#     x = 1
#     y = 1
    
    init = [x, y]
    
    print()
    print ("[%s:%d] init => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), init))

    
    a = Matrix(init)
#     a = Matrix([x,y])

    ### append
    aryOf_Coordinates.append([expand(a[0]), expand(a[1])])
#     aryOf_Coordinates.append(a)
    
    p = 2; q = -1; r = 1; s = 0
    
    m = Matrix([[p, q], [r, s]])
#     m = Matrix([[2,-1], [1,0]])

    #ref dot https://stackoverflow.com/questions/47839177/sympy-dot-product-results-in-a-list
#     prod = a.dot(m) #=> Matrix size mismatch: (2, 1) * (2, 2).
    prod = m.dot(a) #=> [2*x - y, x]
#     prod = a * m
     
    print()
    print ("[%s:%d] prod => \n%s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), prod))

#     print(prod)
    
    #ref expand https://stackoverflow.com/questions/34616170/how-to-expand-matrix-expression-in-sympy
    print(expand(prod[0]))
    print(expand(prod[0]) * 3)
    print(type(expand(prod[0])))
    print(expand(prod[1]))
    
    ### append
    aryOf_Coordinates.append([expand(prod[0]), expand(prod[1])])
    
    
    ### report
    print()
    print ("[%s:%d] aryOf_Coordinates => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), aryOf_Coordinates))
    
    
    for i in range(5):
         
        prod = m.dot(prod)
         
        ### append
        aryOf_Coordinates.append([expand(prod[0]), expand(prod[1])])
            
    
#     a = Matrix([1,2,3])
#     
#     a
#     print(a)
    
    ### report
    print()
    print ("[%s:%d] aryOf_Coordinates => \n%s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), aryOf_Coordinates))
    
    
    cross_X = [x[0] for x in aryOf_Coordinates]
    cross_Y = [x[1] for x in aryOf_Coordinates]
    
    print()
    print(cross_X)
    print(cross_Y)
    
    ### plot
    plt.plot(cross_X, cross_Y, 'ro')
    plt.show()
    
    '''###################
        message        
    ###################'''
    print()
    print ("[%s:%d] test_3_N_Multiply => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
    
    
#/test_1():

def test_2_Calc():
    
    #ref http://docs.sympy.org/latest/tutorial/matrices.html
    init_printing(use_unicode=True)
    
    '''###################
        vars        
    ###################'''
    var("a:z")
    
    '''###################
        ops        
    ###################'''
#     x = 2
#     y = 1
    
    a = Matrix([x,y])
    
    m = Matrix([[n + 1, -n], [n, -n + 1]])
#     m = Matrix([[2,-1], [1,0]])

    #ref dot https://stackoverflow.com/questions/47839177/sympy-dot-product-results-in-a-list
#     prod = a.dot(m) #=> Matrix size mismatch: (2, 1) * (2, 2).
    prod = m.dot(a) #=> [2*x - y, x]
#     prod = a * m
     
    print(prod)
    
    #ref expand https://stackoverflow.com/questions/34616170/how-to-expand-matrix-expression-in-sympy
    print(expand(prod[0]))
    print(expand(prod[1]))
    
    for i in range(5):
        
        prod = m.dot(prod)
        
        print()
#         print ("[%s:%d] n = %d\nprod = %s\nprod[0] = '%s'" % \
#                (os.path.basename(libs.thisfile()), libs.linenum()
#                 , i + 2
#                 , prod
#                 , prod[0]
#                 ))
#         print ("[%s:%d] n = %d\nexpand(prod[0]) => %s\nexpand(prod[1]) => %s" % \
        print ("[%s:%d] m = %d\nexpand(prod[0]) => %s\nexpand(prod[1]) => %s" % \
               (os.path.basename(libs.thisfile()), libs.linenum()
                , i + 2
                , expand(prod[0])
                , expand(prod[1])
                
                ))

        
    
#     a = Matrix([1,2,3])
#     
#     a
#     print(a)
    
    '''###################
        message        
    ###################'''
    print()
    print ("[%s:%d] test_1 => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
    
    
#/def test_3_N_Multiply():

def test_1_Init():
    
    #ref http://docs.sympy.org/latest/tutorial/matrices.html
    init_printing(use_unicode=True)
    
    '''###################
        vars        
    ###################'''
    var("a:z")
    
    '''###################
        ops        
    ###################'''
    a = Matrix([x,y])
    
    m = Matrix([[2,-1], [1,0]])

    #ref dot https://stackoverflow.com/questions/47839177/sympy-dot-product-results-in-a-list
#     prod = a.dot(m) #=> Matrix size mismatch: (2, 1) * (2, 2).
    prod = m.dot(a) #=> [2*x - y, x]
#     prod = a * m
     
    print(prod)
    
    for i in range(5):
        
        prod = m.dot(prod)
        
        print()
        print ("[%s:%d] n = %d\nprod = %s\nprod[0] = '%s'" % \
               (os.path.basename(libs.thisfile()), libs.linenum()
                , i + 2
                , prod
                , prod[0]
                ))
        
    
#     a = Matrix([1,2,3])
#     
#     a
#     print(a)
    
    '''###################
        message        
    ###################'''
    print()
    print ("[%s:%d] test_1 => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
    
    
#/test_1():

def exec_prog(): # from : 20180116_103908
     
    ### test 2
    test_3_N_Multiply()
#     test_2_Calc()
#     test_1_Init()
     
    
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