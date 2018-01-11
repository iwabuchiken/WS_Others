# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\fx\82_\1_
82_1.py

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

from libs import cons

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

def exec_prog(): # upto : 20180109_161654
     
    '''######################################
        get data : raw csv rows
    ######################################'''
    #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
    #ref https://docs.python.org/3.5/library/enum.html
    fname_In = cons.FPath.dpath_In_CSV.value \
            + "/" \
            + cons.FPath.fname_In_CSV.value
#     fname_In = cons.FPath.fpath_In_CSV.value
#     fname_In = cons.FPath.fname_In_CSV.value
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=>
    '''### ###''' 
    header_Length   = 2
#     header_Length   = 3
#     skip_Header     = True
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
        get : high-lows        
    ###################'''
    id_Start = cons.BarData.HighLowDiff_ID_Start.value
    id_End = cons.BarData.HighLowDiff_ID_End.value
    
#     typeOf_Data = cons.typeOf_Data_OPENCLOSE
#     typeOf_Data = "OpenClose"
    
    result_HighLowDiffs = libfx.get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
#     result = libfx.get_HighLowDiffs(aryOf_BarDatas, typeOf_Data, id_Start, id_End)
    
    print ("[%s:%d] result => %s" % \
            (libs.thisfile(), libs.linenum(), result_HighLowDiffs))
    
#     print "[%s:%d] result[%s] => %s" % \
#             (libs.thisfile(), libs.linenum(), cons.LABEL_OC, result_HighLowDiffs[cons.LABEL_OC])
#     print "[%s:%d] result[%s] => %s" % \
#             (libs.thisfile(), libs.linenum(), cons.LABEL_HL, result_HighLowDiffs[cons.LABEL_HL])
    print()
    
    '''###################
        add : data        
    ###################'''
    whole_Data = {}
    
    whole_Data['data'] = result_HighLowDiffs
    
    print()
    print ("[%s:%d] whole data =>" % (os.path.basename(libs.thisfile()), libs.linenum()))
    print (whole_Data)
    
    '''###################
        build : meta info        
    ###################'''
    
    dictOf_MetaInfo = libfx.get_BarData_MetaInfo(fname_In, header_Length)

    print()
    print ("[%s:%d] dictOf_MetaInfo => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), dictOf_MetaInfo))
    print()

    ### add : meta info
    whole_Data['meta'] = dictOf_MetaInfo
    
    '''###################
        write to file        
    ###################'''
        #     [82_1.py:163] dictOf_MetaInfo => {'PAIR': 'USDJPY', 'PERIOD': 'H1', 'DAYS': '720
        #     ', 'SHIFT': '1'}
#     fname_Out_HighLowDiffs =  \
    fpath_Out_HighLowDiffs =  \
            cons.FPath.fpath_Out_HighLowDiff.value \
            + "/" \
            + "_HighLowDiff_." \
            + cons.Label_ColNames.PAIR.value + "-" \
                 + dictOf_MetaInfo[cons.Label_ColNames.PAIR.value] \
            + "." \
            + cons.Label_ColNames.PERIOD.value + "-" \
                 + dictOf_MetaInfo[cons.Label_ColNames.PERIOD.value] \
            + "." \
            + cons.Label_ColNames.DAYS.value + "-" \
                 + dictOf_MetaInfo[cons.Label_ColNames.DAYS.value] \
            + "." \
            + cons.Label_ColNames.SHIFT.value + "-" \
                 + dictOf_MetaInfo[cons.Label_ColNames.SHIFT.value] \
            + "." \
            + libs.get_TimeLabel_Now() \
            + ".csv"
#             + ".txt"
    
    print ("[%s:%d] fname out => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), fpath_Out_HighLowDiffs))
    
    ### write to file
    f_Out = open(fpath_Out_HighLowDiffs, "w")
    
    '''###################
        meta info        
    ###################'''
    f_Out.write(
         
        '\t'.join(
                [cons.Label_ColNames.PAIR.value, \
                 cons.Label_ColNames.PERIOD.value, \
                 cons.Label_ColNames.DAYS.value, \
                 cons.Label_ColNames.SHIFT.value, \
                 
                 "id_Start", \
                 "id_End", \
                 
                 "source csv"
                 ])

        )
    
    f_Out.write('\n')

    f_Out.write(

        '\t'.join(
                [
                dictOf_MetaInfo[cons.Label_ColNames.PAIR.value], \
                 dictOf_MetaInfo[cons.Label_ColNames.PERIOD.value], \
                 dictOf_MetaInfo[cons.Label_ColNames.DAYS.value], \
                 dictOf_MetaInfo[cons.Label_ColNames.SHIFT.value], \
                 
                 str(id_Start), \
                 str(id_End), \
                 
                 cons.FPath.fname_In_CSV.value
                 ])
        )
    
    f_Out.write('\n')
    
    f_Out.write("\t\t\t\t" \
                + aryOf_BarDatas[id_Start - 1].dateTime_Local \
                + '\t' \
                + aryOf_BarDatas[id_End - 1].dateTime_Local
                )
    f_Out.write('\n')
    
    '''###################
        High, low, diff        
    ###################'''
#     f_Out.write('\t'.join([cons.BarData.LABEL_OC.value].extend(result_HighLowDiffs[cons.BarData.LABEL_OC.value])))
#     tmp = [cons.BarData.LABEL_OC.value]
#     tmp = result_HighLowDiffs[cons.BarData.LABEL_OC.value]
#     tmp = [cons.BarData.LABEL_OC.value].extend(['aaa'])
#     tmp = [cons.BarData.LABEL_OC.value] \
#                 .extend(result_HighLowDiffs[cons.BarData.LABEL_OC.value])

    ### OC
    tmp = [cons.BarData.LABEL_OC.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_OC.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')

    ### HL
    tmp = [cons.BarData.LABEL_HL.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_HL.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### RSI
    tmp = [cons.BarData.LABEL_RSI.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_RSI.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### MFI
    tmp = [cons.BarData.LABEL_MFI.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_MFI.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### BB_MAIN
    tmp = [cons.BarData.LABEL_BB_MAIN.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_BB_MAIN.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### BB_1S
    tmp = [cons.BarData.LABEL_BB_1S.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_BB_1S.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### BB_2S
    tmp = [cons.BarData.LABEL_BB_2S.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_BB_2S.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### BB_M1S
    tmp = [cons.BarData.LABEL_BB_M1S.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_BB_M1S.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
    ### BB_M2S
    tmp = [cons.BarData.LABEL_BB_M2S.value]
    tmp.extend(result_HighLowDiffs[cons.BarData.LABEL_BB_M2S.value])
    f_Out.write('\t'.join([str(x) for x in tmp]))
#     f_Out.write('\t'.join(tmp))
    f_Out.write('\n')
    
#     print()
#     print ("[%s:%d] OC data => " % (os.path.basename(libs.thisfile()), libs.linenum()))
#     print(tmp)
#     print()
    
    '''###################
        file : close        
    ###################'''
    f_Out.close()
    
    print()
    print ("[%s:%d] file closed => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), fpath_Out_HighLowDiffs))
    print()
    
    
#     #test
#     print()
#     print ("[%s:%d] aryOf_BarDatas[id_Start(%d)] => %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum(), 
#                 id_Start, aryOf_BarDatas[id_Start]))
#     
#     print(aryOf_BarDatas[id_Start].dateTime_Local)
# #     print(aryOf_BarDatas[id_Start])
#     
#     print()
    
    '''###################
        Report        
    ###################'''
    print ("[%s:%d] exec_prog => done" % (os.path.basename(libs.thisfile()), libs.linenum()))
 
#/def exec_prog()

# def exec_prog(): # upto : 20180108_122418
#     
#     '''###################
#         get data        
#     ###################'''
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=>
# 
#     id_Start    = 195
#     id_End      = 202
# 
#     header_Length = 3
#     skip_Header=True
# 
#     result = libfx.get_ChartData_CSV_Between(\
#                     fname_In, id_Start, id_End, header_Length, skip_Header)
# #     result = libfx.get_ChartData_CSV_Between(fname_In, id_Start, id_End)
#     
#     print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result)
#     
#     
#     print "[%s:%d] exec_prog => done" % (libs.thisfile(), libs.linenum())
# 
# #def exec_prog()

# def exec_prog(): # upto : 20180108_122418
#      
#     '''######################################
#         get data : raw csv rows
#     ######################################'''
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=>
#  
#     header_Length   = 2
# #     header_Length   = 3
# #     skip_Header     = True
#     skip_Header     = False
#  
#     result = libfx.get_ChartData_CSV(\
#                     fname_In, header_Length, skip_Header)
#     
#     ### Validate
#     if result == None : #if result == None
#     
#         print "[%s:%d] get_ChartData_CSV => Returned 'None'" % \
#                     (libs.thisfile(), libs.linenum())
#         
#         return
#         
#     #/if result == None
#     
#     ### report
#     print
#     print ("[%s:%d] CSV rows => %d" % (libs.thisfile(), libs.linenum(), len(result)))
#     print
#     
#     print ("[%s:%d] row[%d] => %s" % (libs.thisfile(), libs.linenum(), 0, result[0]))
#     print
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
#         print "[%s:%d] aryOf_BarDatas => None" % (libs.thisfile(), libs.linenum())
#         print
#         
#         return
#     #/if aryOf_BarDatas == None
#     
#     '''###################
#         get : high-lows        
#     ###################'''
#     id_Start = cons.HighLowDiff_ID_Start
#     id_End = cons.HighLowDiff_ID_End
#     
# #     typeOf_Data = cons.typeOf_Data_OPENCLOSE
# #     typeOf_Data = "OpenClose"
#     
#     result_HighLowDiffs = libfx.get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
# #     result = libfx.get_HighLowDiffs(aryOf_BarDatas, typeOf_Data, id_Start, id_End)
#     
#     print "[%s:%d] result => %s" % \
#             (libs.thisfile(), libs.linenum(), result_HighLowDiffs)
#     
# #     print "[%s:%d] result[%s] => %s" % \
# #             (libs.thisfile(), libs.linenum(), cons.LABEL_OC, result_HighLowDiffs[cons.LABEL_OC])
# #     print "[%s:%d] result[%s] => %s" % \
# #             (libs.thisfile(), libs.linenum(), cons.LABEL_HL, result_HighLowDiffs[cons.LABEL_HL])
#     print
#     
#     '''###################
#         Report        
#     ###################'''
#     print "[%s:%d] exec_prog => done" % (libs.thisfile(), libs.linenum())
#  
# #/def exec_prog()
 
# def exec_prog(): # upto : 20180108_122418
#     
#     '''###################
#         get data        
#     ###################'''
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=>
# 
#     id_Start    = 195
#     id_End      = 202
# 
#     header_Length = 3
#     skip_Header=True
# 
#     result = libfx.get_ChartData_CSV_Between(\
#                     fname_In, id_Start, id_End, header_Length, skip_Header)
# #     result = libfx.get_ChartData_CSV_Between(fname_In, id_Start, id_End)
#     
#     print "[%s:%d] result => %s" % (libs.thisfile(), libs.linenum(), result)
#     
#     
#     print "[%s:%d] exec_prog => done" % (libs.thisfile(), libs.linenum())
# 
# #def exec_prog()
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

    print()
#     msg = "[%s:%d] done" % (___FILE, ___FILE)
#     msg = "[%s:%d] done" % (thisfile(), linenum())
#     msg = "[%s:%d] get_ChartData_Between(fname, id_Start, id_End) => done" % \
#                 (libs.thisfile(), libs.linenum())
                
#     print (msg)
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))
#     print ("[%s:%d] all done" % (libs.thisfile(), libs.linenum()))
        
    



#####################################/EOF