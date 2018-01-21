# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\fx\82_\82_10
82_10.py

82_6.py > tmp.log
cp_log.py

82_6.py > tmp.log && cp_log.py

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
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs
from libs import libfx

from libs import cons

import getopt
import os
import inspect

import math as math

import struct

from shutil import copyfile

###############################################

def exec_prog__PatternMatch_Body_UpDown(): # from : 20180120_130551
     
    '''######################################
        get data : raw csv rows
    ######################################'''
    #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
    #ref https://docs.python.org/3.5/library/enum.html
    fname_In = cons.FPath.dpath_In_CSV.value \
            + "/" \
            + cons.FPath.fname_In_CSV.value

    header_Length   = 2
    
    skip_Header     = False
 
    result = libfx.get_ChartData_CSV(\
                    fname_In, header_Length, skip_Header)
    
    ### Validate
    if result == None : #if result == None
    
        print ("[%s:%d] get_ChartData_CSV => Returned 'None'" % \
                    (libs.thisfile(), libs.linenum()))
#         print "[%s:%d] get_ChartData_CSV => Returned 'None'" % \
#                     (libs.thisfile(), libs.linenum())
        
        return
        
    #/if result == None
    
    ### report
    print()
    print ("[%s:%d] CSV rows => %d" % (os.path.basename(libs.thisfile()), libs.linenum(), len(result)))
    print()
    
    print ("[%s:%d] row[%d] => %s" % (os.path.basename(libs.thisfile()), libs.linenum(), 0, result[0]))
    print()
    
    '''######################################
        Conv : CSV rows ---> array of BarData class instances        
    ######################################'''
#     aryOf_BarDatas = libfx.conv_CSVRows_2_BarDatas(result)
    aryOf_BarDatas = libfx.conv_CSVRows_2_BarDatas(result[header_Length:])
    
    ### Validate
    if aryOf_BarDatas == None : #if aryOf_BarDatas == None
    
        print ("[%s:%d] aryOf_BarDatas => None" % (os.path.basename(libs.thisfile()), libs.linenum()))
        print()
        
        return
    #/if aryOf_BarDatas == None
    
    '''###################
        Build data        
    ###################'''
    volumeOf_Body = cons.PatternMatch.VOLUMEOF_BODY.value
    
    aryOf_UpDownPattern = [1,1,1,0]
    
    ### pattern match
    aryOf_Matched_BarDatas = \
            libfx.get_AryOf_BarDatas_PatternMatched__Body_UpDown(
                        aryOf_BarDatas
                        , aryOf_UpDownPattern
                        , volumeOf_Body
                        )
    
    '''###################
        report        
    ###################'''
    print()
    print ("[%s:%d] aryOf_Matched_BarDatas => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), 
            aryOf_Matched_BarDatas))
    
    print()
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog(): # from : 20180116_103908





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
    exec_prog__PatternMatch_Body_UpDown()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))

