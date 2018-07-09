#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe

# -*- coding: utf-8 -*-
'''
copied from : C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py
at : 2018/02/13 09:03:41

C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py

<log file operation>
pushd C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6
cp_log.py

'''

import inspect
import os
import os.path
import sys

import copy

import numpy

import csv
import sys

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time

from pathlib import Path

#ref https://stackoverflow.com/questions/25389095/python-get-path-of-root-project-structure answered Aug 19 '14 at 17:42
from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR
# from definitions import ROOT_DIR


'''###################

###################'''
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/curr')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/curr/data')

from mm.libs_mm import cons_mm
from mm.libs_mm import cons_fx
from mm.libs_mm import libs
from mm.libs_mm import libfx

# from libs import cons

###############################################

def test_func():
    
    print ("[%s:%d] test_func()" % (thisfile(), linenum()))
    

# def get_ChartData_CSV_Between(fname_In, id_Start, id_End):

def get_ChartData_CSV_Between \
(fname_In, id_Start, id_End, header_Length, skip_Header=True):
    
    '''###################
        file : open
    ###################'''
#     fname_In = "data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> No such file or directory
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> 
    
    #ref csv open http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
    f = open(fname_In, 'rb')
#     fin = open(fname_In, 'r')
    
    print ("[%s:%d] file => opened : %s" % (libs.thisfile(), libs.linenum(), fname_In))
    
    '''###################
        file : read
    ###################'''
    '''###################
        skip header
    ###################'''
    print ("[%s:%d] skip headers => %d lines" % \
                    (libs.thisfile(), libs.linenum(), header_Length))
    
    #ref delimiter https://docs.python.org/3.5/library/csv.html
    delim = ';'
    reader = csv.reader(f, delimiter=delim)
#     reader = csv.reader(f)
    
#     for row in reader :
#         print row
    
    
#     #ref for https://www.tutorialspoint.com/python/python_for_loop.htm
#     for index in range(header_Length) :
#         
#         tmp_Str = fin.read()
#         
#         print tmp_Str
        
        
#     data_Csv = fin.readlines()
    
        
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print ("[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum()))
        
        return None
    else:
        
        '''###################
            skip header        
        ###################'''
        count = 0
        
        for row in reader : 
            print(row)
            
#             ['1', '112.679', '112.706', '112.646', '112.672', '44.91202147258796', '48.05020
#             210044262', '112.782302005599', '112.7065760027994', '112.6308499999999', '112.5
#             551239972003', '112.4793979944007', '-0.007000000000005002', '0.0600000000000022
#             7', '2017.12.29 23:00', '2017.12.30 06:00']

            count += 1
            
            if count >= 2 : break
        
        print
        print ("[%s:%d] row =>" % (libs.thisfile(), libs.linenum()))
        
        print
        for row in reader : 
            print(row)
            print
            break
        
        
#         print
#         print "[%s:%d] print row" % (libs.thisfile(), libs.linenum())
#         
#         for row in reader : 
#             print(row)
#             break
#         
#         print
#         print "[%s:%d] print row" % (libs.thisfile(), libs.linenum())
#         
#         for row in reader : 
#             print(row)
#             break
        
        #ref len https://duckduckgo.com/?q=python+array+length&atb=v84-1__&ia=qa
#         print "[%s:%d] lines => %d" % (libs.thisfile(), libs.linenum(), len(reader))
        
        #ref len of reader https://bytes.com/topic/python/answers/652839-csv-reader-length
#         reader_Listed = list(reader)
#         print "[%s:%d] lines => %d" % \
#                     (libs.thisfile(), libs.linenum(), len(reader_Listed))   #=> lines => 722
#                     (libs.thisfile(), libs.linenum(), len(list(reader)))
#         print "[%s:%d] lines => %d" % (libs.thisfile(), libs.linenum(), len(data_Csv))
        
#         print (reader_Listed[0])    #=> ['Pair=USDJPY;Period=H1;Days=720;Shift=1;Bars=17280;Time=20171231_233725']
#         print (reader_Listed[0][0]) #=> Pair=USDJPY;Period=H1;Days=720;Shift=1;Bars=17280;Time=20171231_233725
#         print (list(reader))
        
#         row_1 = reader_Listed[0]
#         
#         for col in row_1 :
#             
#             print (col)
#             
#             print
        
#         '''###################
#             first row        
#         ###################'''
#         print "[%s:%d] row '%d' => " % \
#                     (libs.thisfile(), libs.linenum(), header_Length + id_Start)
#         
#         print (list(reader)[header_Length + id_Start])
# #         print (reader[header_Length + id_Start])    #=> IndexError: list index out of range
#     
    '''###################
        file : close
    ###################'''
    f.close()
#     fin.close()
    
    print ("[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fname_In))

    #ref None https://stackoverflow.com/questions/3289601/null-object-in-python
    return None

'''###################
    func : def get_ChartData_CSV

    at : 2018/01/07 12:26:55

    @return: [[csv row], [csv row], ...]
            
###################'''
def get_ChartData_CSV \
(fname_In, header_Length, skip_Header=True, delim = ';'):
    
    '''###################
        vars
    ###################'''
    aryOf_CSV_Rows = []
    
    '''###################
        file : open
    ###################'''
#     fname_In = "data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> No such file or directory
#     fname_In = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"    #=> 
    
    #ref csv open http://www.pythonforbeginners.com/systems-programming/using-the-csv-module-in-python/
    f = open(fname_In, 'r')
#     f = open(fname_In, 'rb')
    
#     print ("[%s:%d] file => opened : %s" % (libs.thisfile(), libs.linenum(), fname_In))
    
    '''###################
        file : read
    ###################'''
    '''###################
        skip header
    ###################'''
#     print ("[%s:%d] skip headers => %d lines" % \
#                     (libs.thisfile(), libs.linenum(), header_Length))
    
    #ref delimiter https://docs.python.org/3.5/library/csv.html
#     delim = ';'
    reader = csv.reader(f, delimiter = delim)
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print ("[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum()))
        
        return None
    
    else:   # if reader is None:
        
        '''###################
            skip header        
        ###################'''
        if skip_Header == True : #if skip_Header == True

            count = 1
            
            for row in reader :
                
                count += 1
                
                if count >= header_Length : #if count >= header_Length
#                 if count > header_Length : #if count >= header_Length
                
                    break
                    
                #/if count >= header_Length
                
            #/for row in reader :
            
            print ("[%s:%d] header skipped => %d lines" % \
                        (libs.thisfile(), libs.linenum(), header_Length))
            
        #/if skip_Header == True


        
        '''###################
            read rows        
        ###################'''
        count = 0
        
        for row in reader : 
                        ### ERROR
                        # File "..\libs\libfx.py", line 261, in get_ChartData_CSV
                        #   for row in reader :
                        # _csv.Error: iterator should return strings, not bytes (did you open the file in
                        # text mode?)
#             print(row)
            
#             ['1', '112.679', '112.706', '112.646', '112.672', '44.91202147258796', '48.05020
#             210044262', '112.782302005599', '112.7065760027994', '112.6308499999999', '112.5
#             551239972003', '112.4793979944007', '-0.007000000000005002', '0.0600000000000022
#             7', '2017.12.29 23:00', '2017.12.30 06:00']

            count += 1
            
            
#             if count >= 2 : break

            aryOf_CSV_Rows.append(row)
        
        #/for row in reader :
        
#         #debug
#         print
#         print "[%s:%d] num of rows => %d" % (libs.thisfile(), libs.linenum(), count)
#         print
        
#         print
#         print "[%s:%d] row =>" % (libs.thisfile(), libs.linenum())
#         
#         print
#         for row in reader : 
#             print(row)
#             print
#             break
        
    #/if reader is None:
    
    '''###################
        file : close
    ###################'''
    f.close()
    
#     print ("[%s:%d] file => closed : %s" % \
#                 (libs.thisfile(), libs.linenum(), fname_In))

    #ref None https://stackoverflow.com/questions/3289601/null-object-in-python
#     return None
    
    return aryOf_CSV_Rows

'''###################
    conv_CSVRows_2_BarDatas(result)
    
    @param result: Array of CSV rows (Without header lines)
        [['1', '112.679', '112.706', ...], [...], ...]
    
    @return: Array of BarData class instances
        [barData, barData, ...]
    
###################'''
def conv_CSVRows_2_BarDatas(result) :
    
#     #debug
#     print
#     print ("[%s:%d] conv_CSVRows_2_BarDatas : result[0] => %s" % (libs.thisfile(), libs.linenum(), result[0]))
#     print
    
#     print "[%s:%d] result[0] => %s" % (libs.thisfile(), libs.linenum(), result[0])
#     print
    
#     #debug
#     print ("[%s:%d] len(result) => %d" % \
#                 (libs.thisfile(), libs.linenum(), len(result)))
#     print
    
    '''###################
        Vars        
    ###################'''
    aryOf_BarDatas = []
    
    '''###################
        Conversions        
    ###################'''
    for item in result :
        
        barData = BarData()
    
        # insert data
            # ['1',    no,
            # '112.679',    Open,
            # '112.706',    High,
            # '112.646',    Low,
            # '112.672',    Close,
            # '44.91202147258796',    RSI,
            # '48.05020210044262',    MFI,
            # '112.782302005599',    BB.2s,
            # '112.7065760027994',    BB.1s,
            # '112.6308499999999',    BB.main,
            # '112.5551239972003',    BB.-1s,
            # '112.4793979944007',    BB.-2s,
            # '-0.007000000000005002',    Diff,
            # '0.06000000000000227',    High/Low,
            # '2017.12.29 23:00',    datetime,
            # '2017.12.30 06:00']    
            
        barData.no            = int(item[0])
        
        barData.price_Open    = float(item[1])
        barData.price_High    = float(item[2])
        barData.price_Low     = float(item[3])
        barData.price_Close   = float(item[4])
        
        barData.rsi   = float(item[5])
        barData.mfi   = float(item[6])
        
        barData.bb_2S   = float(item[7])
        barData.bb_1S   = float(item[8])
        barData.bb_Main   = float(item[9])
        barData.bb_M1S   = float(item[10])
        barData.bb_M2S   = float(item[11])
        
        barData.diff_OC   = float(item[12])
        barData.diff_HL   = float(item[13])
        
        barData.dateTime        = item[14]
        barData.dateTime_Local  = item[15]
        
        
        # append
        aryOf_BarDatas.append(barData)
        
    #/for item in result :
    
#     #debug
#     print ("[%s:%d] len(aryOf_BarDatas) => %d" % \
#                 (libs.thisfile(), libs.linenum(), len(aryOf_BarDatas)))
#     print
    
#     #debug
#     print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
#                 (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].no)
#     print "[%s:%d] aryOf_BarDatas[%d].price_Open => %.3f" % \
#                 (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].price_Open)
#     print "[%s:%d] aryOf_BarDatas[%d].diff_OC => %.3f" % \
#                 (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].diff_OC)
#                 
#     print
#     print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
#                 (libs.thisfile(), libs.linenum(), 1, aryOf_BarDatas[1].no)
#     print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
#                 (libs.thisfile(), libs.linenum(), 2, aryOf_BarDatas[2].no)
#     print
    
    #test
#     barData_0 = BarData()
#     
#     # insert data
#     barData_0.id            = result[0][0]
#     barData_0.price_Open    = result[0][1]
#     barData_0.price_High    = result[0][2]
#     barData_0.price_Low     = result[0][3]
#     barData_0.price_Close   = result[0][4]
#     
#     print "[%s:%d] barData_0 => %s" % (libs.thisfile(), libs.linenum(), barData_0)
#     print
    
    return aryOf_BarDatas
#     return None

#/def conv_CSVRows_2_BarDatas(result) :

class BarData :
    
#     id = -1
    no = -1

    price_Open = -1.0
    price_High = -1.0
    price_Low = -1.0
    price_Close = -1.0
    
    rsi      = -1.0
    mfi      = -1.0
    
    bb_2S       = -1.0
    bb_1S       = -1.0
    bb_Main     = -1.0
    bb_M1S       = -1.0     # -1σ
    bb_M2S       = -1.0
    
    diff_OC       = -1.0
    diff_HL       = -1.0
    
    dateTime        = ""
    dateTime_Local  = ""
    
#/class BarData :


'''###################
    _get_HighLowDiffs__OC(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__OC(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff__OC = []

    aryOf_Price_OpenClose = [x.price_Open for x in target_Ary]

#     print "[%s:%d] price open => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_OpenClose)
#         
#     print "[%s:%d] price close => %s" % \
#                 (libs.thisfile(), libs.linenum(), [x.price_Close for x in target_Ary])
        
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
    aryOf_Price_OpenClose.extend([x.price_Close for x in target_Ary])
#     aryOf_Price_Close = [x.price_Close for x in target_Ary]
#     sum = [x for x.price_Open in target_Ary]
    
#     aryOf_Price_OpenClose = aryOf_Price_Open.extend(aryOf_Price_Close)
    
#     print "[%s:%d] aryOf_Price_OpenClose => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_OpenClose)
#     print "[%s:%d] sum => %s" % (libs.thisfile(), libs.linenum(), sum)

    '''###################
        Calc data        
    ###################'''
    max_Val = max(aryOf_Price_OpenClose)
    min_Val = min(aryOf_Price_OpenClose)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
#         max_OpenClose = max(aryOf_Price_OpenClose)
#         min_OpenClose = min(aryOf_Price_OpenClose)
#         diff_OpenClose = round(max_OpenClose - min_OpenClose, 3)
        
#     else : #/if typeOf_Data == "OpenClose"
#         
#         print "[%s:%d] Unknown data type => '%s'" % \
#                     (libs.thisfile(), libs.linenum(), typeOf_Data)
#                     
#         return None
                
    #/if typeOf_Data == "OpenClose"
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff__OC.append(max_Val)
    aryOf_HighLowDiff__OC.append(min_Val)
    aryOf_HighLowDiff__OC.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff__OC
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__HL(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff__HL = []

    aryOf_Price_HighLow = [x.price_High for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
    aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = max(aryOf_Price_HighLow)
    min_Val = min(aryOf_Price_HighLow)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff__HL.append(max_Val)
    aryOf_HighLowDiff__HL.append(min_Val)
    aryOf_HighLowDiff__HL.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff__HL
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__RSI(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.rsi for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_RSI.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_RSI.value)
#     max_Val = round(max(aryOf_Price_HighLow), cons.ROUND_RSI)
#     min_Val = round(min(aryOf_Price_HighLow), cons.ROUND_RSI)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__MFI(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.mfi for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_MFI.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_MFI.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_Main(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_Main for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
#     max_Val = max(aryOf_Price_HighLow)
#     min_Val = min(aryOf_Price_HighLow)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_1S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_1S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_M1S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_M1S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_2S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_2S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)

'''###################
    _get_HighLowDiffs__HL(target_Ary)
    
    Used by : get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param target_Ary: array of BarData instances
    
    @return: array of max, min and diff        
    
###################'''
def _get_HighLowDiffs__BB_M2S(target_Ary) :
    
    max_Val     = 0.0
    min_Val     = 0.0
    diff_Val    = 0.0
    
    aryOf_HighLowDiff = []

    aryOf_Price_HighLow = [x.bb_M2S for x in target_Ary]
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
#     aryOf_Price_HighLow.extend([x.price_Low for x in target_Ary])
    
#     print "[%s:%d] aryOf_Price_HighLow => %s" % \
#                 (libs.thisfile(), libs.linenum(), aryOf_Price_HighLow)

    '''###################
        Calc data        
    ###################'''
    max_Val = round(max(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    min_Val = round(min(aryOf_Price_HighLow), cons.BarData.ROUND_BB.value)
    
    #ref round https://stackoverflow.com/questions/17470883/rounding-to-two-decimal-places-in-python-2-7
    diff_Val = round(max_Val - min_Val, 3)
        
    
    '''###################
        build data        
    ###################'''
    aryOf_HighLowDiff.append(max_Val)
    aryOf_HighLowDiff.append(min_Val)
    aryOf_HighLowDiff.append(diff_Val)
    
    '''###################
        return        
    ###################'''
    return aryOf_HighLowDiff
    
#/_get_HighLowDiffs__OC(target_Ary)


'''###################
    get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
    
    @param typeOf_Data: type of data to obtain
            e.g. "OpenClose"
    @param id_Start: 'no' in csv file, starting from 1
    
    @return: dict of max, min and diff for each category
            e.g. {'OC' : [112.677, 112.57, 0.107], 'HL' : [...], ...}
            e.g.
            {'BB_M1S': [112.4789, 112.4699, 0.009],
            'BB_Main': [112.5733, 112.5437, 0.03],
            'RSI': [55.1223, 49.7157, 5.407],
            'HL': [112.664, 112.529, 0.135],
            'BB_2S': [112.7622, 112.6875, 0.075],
            'MFI': [50.0162, 35.5028, 14.513],
            'OC': [112.633, 112.544, 0.089],
            'BB_1S': [112.6677, 112.6156, 0.052],
            'BB_M2S': [112.3999, 112.3811, 0.019]}

###################'''
def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End) :
# def get_HighLowDiffs(aryOf_BarDatas, typeOf_Data, id_Start, id_End) :
    
    '''###################
        prep : target array
        
        if no.1 ~ 5
            => [0:5] ---> index 0 thru 4
    ###################'''
    
    #ref slice https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
    target_Ary = aryOf_BarDatas[id_Start - 1 : (id_End)]
#     target_Ary = aryOf_BarDatas[id_Start - 1 : (id_End + 1)]
#     target_Ary = aryOf_BarDatas[id_Start : (id_End + 1)]
    
#     #debug
#     print ("[%s:%d] target_Ary => %s" % (libs.thisfile(), libs.linenum(), target_Ary))

    
    '''###################
        Vars        
    ###################'''
#     max_Val     = 0.0
#     min_Val     = 0.0
#     diff_Val    = 0.0
#     
#     aryOf_HighLowDiff__OC = []
    
    '''######################################
        Dispatch
    ######################################'''
    '''###################
        open, close
    ###################'''
    aryOf_HighLowDiff__OC = _get_HighLowDiffs__OC(target_Ary)
    
    '''###################
        high, low
    ###################'''
    aryOf_HighLowDiff__HL = _get_HighLowDiffs__HL(target_Ary)
    
    '''###################
        rsi
    ###################'''
    aryOf_HighLowDiff__RSI = _get_HighLowDiffs__RSI(target_Ary)
    
    '''###################
        rsi
    ###################'''
    aryOf_HighLowDiff__MFI = _get_HighLowDiffs__MFI(target_Ary)
    
    '''###################
        BB : main
    ###################'''
    aryOf_HighLowDiff__BB_Main = _get_HighLowDiffs__BB_Main(target_Ary)
    
    '''###################
        BB : 1S
    ###################'''
    aryOf_HighLowDiff__BB_1S = _get_HighLowDiffs__BB_1S(target_Ary)
    
    '''###################
        BB : M1S
    ###################'''
    aryOf_HighLowDiff__BB_M1S = _get_HighLowDiffs__BB_M1S(target_Ary)
    
    '''###################
        BB : 2S
    ###################'''
    aryOf_HighLowDiff__BB_2S = _get_HighLowDiffs__BB_2S(target_Ary)
    
    '''###################
        BB : M2S
    ###################'''
    aryOf_HighLowDiff__BB_M2S = _get_HighLowDiffs__BB_M2S(target_Ary)
    
    '''######################################
        data : final product        
    ######################################'''
    #ref dictionary https://www.tutorialspoint.com/python/python_dictionary.htm
    dict = {
            cons.BarData.LABEL_OC.value : aryOf_HighLowDiff__OC,
            
            cons.BarData.LABEL_HL.value : aryOf_HighLowDiff__HL,
            
            cons.BarData.LABEL_RSI.value : aryOf_HighLowDiff__RSI,
            
            cons.BarData.LABEL_MFI.value : aryOf_HighLowDiff__MFI,
            
            cons.BarData.LABEL_BB_MAIN.value : aryOf_HighLowDiff__BB_Main,
            
            cons.BarData.LABEL_BB_1S.value : aryOf_HighLowDiff__BB_1S,
            
            cons.BarData.LABEL_BB_M1S.value : aryOf_HighLowDiff__BB_M1S,
            
            cons.BarData.LABEL_BB_2S.value : aryOf_HighLowDiff__BB_2S,
            
            cons.BarData.LABEL_BB_M2S.value : aryOf_HighLowDiff__BB_M2S,
            
            }
    
    return dict
#     return aryOf_HighLowDiff__OC
    
#/get_HighLowDiffs(aryOf_BarDatas)

def get_BarData_MetaInfo(fpath_In, header_Length) :
    
    f_in = open(fpath_In, 'r')
    
    delim = ';'
    
    reader = csv.reader(f_in, delimiter = delim)
#     reader = csv.reader(f, delimiter = delim)
    
    aryOf_HeaderRows = []
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print ("[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum()))
        
        return None
    
    else:   # if reader is None:
        
        '''###################
            read rows        
        ###################'''
        count = 0
        
        for row in reader : 

            aryOf_HeaderRows.append(row)
            
            count += 1
            
            ### break
            if count >= header_Length : break #if count >= header_Length

            #/if count >= header_Length
        
    #/if reader is None:
    
    '''###################
        file : close
    ###################'''
    f_in.close()
    
    print ("[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fpath_In))

    print()
    
    print(aryOf_HeaderRows)
            #     [['Pair=USDJPY', 'Period=H1', 'Days=720', 'Shift=1', 'Bars=17280', 'Time=2017123
            #     1_233725'], ['no', 'Open', 'High', 'Low', 'Close', 'RSI', 'MFI', 'BB.2s', 'BB.1s
            #     ', 'BB.main', 'BB.-1s', 'BB.-2s', 'Diff', 'High/Low', 'datetime']]
            
    '''###################
        metainfo : build        
    ###################'''
    dict = {}
    
    dict[cons.Label_ColNames.PAIR.value] = aryOf_HeaderRows[0][0].split("=")[1]
    dict[cons.Label_ColNames.PERIOD.value] = aryOf_HeaderRows[0][1].split("=")[1]
    dict[cons.Label_ColNames.DAYS.value] = aryOf_HeaderRows[0][2].split("=")[1]
    dict[cons.Label_ColNames.SHIFT.value] = aryOf_HeaderRows[0][3].split("=")[1]

    '''###################
        return        
    ###################'''
    return dict

#/get_BarData_MetaInfo(fname_In)

def get_AryOf_BarDatas_PatternMatched__RSI( # 20180113_175014
        aryOf_BarDatas, 
        numOf_Sequence, 
        rangeOf_Flat, 
        flag_UpDown) :
    
    '''###################
        reverse data        
    ###################'''
    ary_Tmp = copy.deepcopy(aryOf_BarDatas)
    
    ary_Tmp.reverse()
    
    d = ary_Tmp[0]
#     d = aryOf_BarDatas[0]
    
#     print()
#     print ("[%s:%d] aryOf_BarDatas[0] => %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum(), d))
#     
#     print("%s price=%.3f" % (d.dateTime_Local, d.price_Open))
#     
#     print()
    
    '''###################
        processing        
    ###################'''
    cnt_In = 0
    
    aryOf_Matched = []
    
    for item in ary_Tmp :
        
        ### :j1
        if cnt_In > (numOf_Sequence - 1) : #if cnt_In > numOf_Sequence
#         if cnt_In > numOf_Sequence : #if cnt_In > numOf_Sequence
    
            print()
            print ("[%s:%d] cnt_In => over numOf_Seg" % (os.path.basename(libs.thisfile()), libs.linenum()))
            print()
            
            return None
        
        else :
            
            ### :j2
            if cnt_In == 0 : #if cnt_In == 0
                
                print()
                print ("[%s:%d] cnt_In => is 0" % \
                       (os.path.basename(libs.thisfile()), libs.linenum()))
                print()
                
                ### put item to ary
                aryOf_Matched.append(item)
                
                print()
                print ("[%s:%d] item appended => %d" % \
                       (os.path.basename(libs.thisfile()), libs.linenum(), item.no))
        
                print()
                
                ### count
                cnt_In += 1
                
                ### next item
                continue
                
            else :
                
                d2 = aryOf_Matched[0]
                
                ### prep for if judgement
                r1 = d2.rsi
                
                r2 = item.rsi
                
                diff_r1_r2 = r1 - r2
                
                #debug
                print()
                print ("[%s:%d] j2 =>" % (os.path.basename(libs.thisfile()), libs.linenum()))
                
                print("r1 => %.3f" % (r1))
                print("r2 => %.3f" % (r2))
                print("rangeOf_Flat / 2 => %.3f" % (rangeOf_Flat / 2))
                print("numpy.absolute(diff_r1_r2) => %.3f" % (numpy.absolute(diff_r1_r2)))
                
                print()
                
                
                ### :j3
                if  numpy.absolute(diff_r1_r2) <= rangeOf_Flat / 2: #if math.
                
                   print() 
                   print ("[%s:%d] less than half of range : %d" % \
                          (os.path.basename(libs.thisfile()), libs.linenum(), 
                           item.no))
                    
                   print() 
                   
                   return None
                
                else :
                    
                   print() 
                   print ("[%s:%d] more than half of range : %d" % \
                          (os.path.basename(libs.thisfile()), libs.linenum(), 
                           item.no))
                    
                   print()
                   
                   return None
                #/if math.
                
                
            
            
                
            #/if cnt_In == 0
                    
                    
        
        
    #/if cnt_In > numOf_Sequence
    
    
        
    #/for item in ary_Tmp :
    '''###################
        return        
    ###################'''
    return None

#/get_AryOf_BarDatas_PatternMatched__RSI

'''###################
    get_AryOf_BarDatas_PatternMatched__RSI__V2( # 20180116_100610
    
    @param numOf_Sequence: number of bars in the flat range
    
    @param rangeOf_Flat: range of the flat period (in JPY; e.g. 0.16 ---> 0.16 yen)
    
    @return: [matched_up], [matched_down]
    
###################'''
def get_AryOf_BarDatas_PatternMatched__RSI__V2( # 20180116_100610
        aryOf_BarDatas, 
        numOf_Sequence, 
        rangeOf_Flat) :

    '''###################
        vars        
    ###################'''
#     ary_Tmp = []
    
    ary_Matched_D = []
    ary_Matched_U = []
    ary_Matched_ALL = []
    
    flag_ALLIN = False
    
    lenOf_Data = len(aryOf_BarDatas)
    
    lenOf_FlatBars  = 4
    
    '''###################
        reverse data        
    ###################'''
    ary_BarDatas_tmp = copy.deepcopy(aryOf_BarDatas)
    
    ary_BarDatas_tmp.reverse()
    
    '''######################################
        loop        
    ######################################'''
    #debug
    count = 0
    cnt_Max = 1000
#     cnt_Max = 8
    
    '''###################
        for : i        
    ###################'''
    for i in range(lenOf_Data - lenOf_FlatBars):
        
        #debug
        print()
        print ("[%s:%d] loop i : %d ==================" % \
               (os.path.basename(libs.thisfile()), libs.linenum(), i))
    
        print()
        
        #debug
        if count > cnt_Max : #if count > cnt_Max
            
            print()
            print ("[%s:%d] debug breaking ..." % (os.path.basename(libs.thisfile()), libs.linenum()))

            print()

            return None
            
        #/if count > cnt_Max
        
        count += 1

        ### get : base bar
        d1 = ary_BarDatas_tmp[i]
        
        ### temp array
        ary_Tmp = []
        
        '''###################
            for : j        
        ###################'''
        for j in range(lenOf_FlatBars): # range : 0 ~ 3

            d2 = ary_BarDatas_tmp[i + j]
#             d2 = ary_BarDatas_tmp[j]
            
            '''###################
                get : rsi values        
            ###################'''
            r1 = d1.rsi # 3
            r2 = d2.rsi # 3
            
            diff = r1 - r2  # j1

            '''###################
                j1        
            ###################'''
            if numpy.abs(diff) <= (rangeOf_Flat / 2.0) : #if math.abs(diff) <= (rangeOf_Flat / 2.0)
        
                #debug
                print()
                print ("[%s:%d] diff: %.3f / (rangeOf_Flat / 2.0) : %.3f" % 
                       (os.path.basename(libs.thisfile()), libs.linenum(), 
                        diff, (rangeOf_Flat / 2.0)))
            
                print()
                
                ### put the item to : ary_Tmp : 1-1
                ary_Tmp.append(d2)
                
                #debug
                print ("[%s:%d] ary_Tmp => %s" % \
                       (os.path.basename(libs.thisfile()), libs.linenum(), ary_Tmp))
        
                print()
                
                ### flag : up # 1-2
                flag_ALLIN = True
                
            else :  # j1.N
                
                #debug
                print()
                print ("[%s:%d] diff > (rangeOf_Flat / 2.0) *********" % 
                       (os.path.basename(libs.thisfile()), libs.linenum()))
            
                print()
            #/if math.abs(diff) <= (rangeOf_Flat / 2.0)
                
#                 ### clear : ary_Tmp
#                 #ref https://stackoverflow.com/questions/3499233/erase-whole-array-python "answered Aug 17 '10 at 4:03"
#                 ary_Tmp = []
                
                ### flag --> put down
                flag_ALLIN = False
                
                ### out : from for.j
                break
        
            ### j2 : next j?
        #/for j in range(lenOf_FlatBars:

        '''###################
            j3        
        ###################'''
        if flag_ALLIN == True : #if flag_ALLIN == True
        
            #debug
            print()
            print ("[%s:%d] (i = %d / '%s') flag_ALLIN => %s #################" % \
                   (os.path.basename(libs.thisfile()), libs.linenum(), \
                    i, d1.dateTime_Local, flag_ALLIN))

            print()
            
            ### flag ---> back to : False
            flag_ALLIN = False
        
        else : #if flag_ALLIN == True
        
            #debug
            print()
            print ("[%s:%d] (i = %d ) flag_ALLIN => %s ***************" % \
                   (os.path.basename(libs.thisfile()), libs.linenum(), \
                    i, flag_ALLIN))

            print()
            
#             ### flag ---> back to : False
#             flag_ALLIN = False
        
        #/if flag_ALLIN == True
        
        

        '''###################
            clear : ary_Tmp        
        ###################'''
        ### clear : ary_Tmp
        #ref https://stackoverflow.com/questions/3499233/erase-whole-array-python "answered Aug 17 '10 at 4:03"
        ary_Tmp = []
        
    #/for i in range(lenOf_Data - lenOf_FlatBars):

    
    '''###################
        return        
    ###################'''
    return None

#/get_AryOf_BarDatas_PatternMatched__RSI__V2

'''###################
    get_AryOf_BarDatas_PatternMatched__Body_UpDown
    
    @param aryOf_UpDownPattern: up for '1', down for '0'
        e.g. [1,1,1,0]
    
    @param volumeOf_Body: unit : yen, float
        e.g. 0.12 yen
            
###################'''
def get_AryOf_BarDatas_PatternMatched__Body_UpDown \
(aryOf_BarDatas, aryOf_UpDownPattern, volumeOf_Body) :
    
    ### report
    print()
    print ("[%s:%d] volumeOf_Body => %.3f | aryOf_UpDownPattern => %s" % \
           (os.path.basename(libs.thisfile()), libs.linenum()
            , volumeOf_Body, aryOf_UpDownPattern))
    
    print()
    
    '''###################
        step : 1        
    ###################'''
    len1 = len(aryOf_BarDatas)
    
    len2 = len(aryOf_UpDownPattern)
    
    UPDOWN = 0  # down
    
    flag_IN = False
    
    ### counter : 'IN' entries
    cntOf_IN = 0
    
    ### debug
    cnt = 0
    cnt_Max = 1000
    
    '''###################
        for : i        
    ###################'''
    for i in range(len1 - len2):
        
        ### debug
        if cnt > cnt_Max : break
            
        #/if cnt > cnt_Max
        
        '''###################
            prep : data        
        ###################'''
        d1 = aryOf_BarDatas[i]
        
        body = d1.price_Close - d1.price_Open
#         body = d1.price_High - d1.price_Low
        
        ### up, down
        if body >= 0 : UPDOWN = 1
        else : UPDOWN = 0
        
        '''###################
            j : 1        
        ###################'''
        #/if body >= 0
        if not (UPDOWN == aryOf_UpDownPattern[0]) \
            or not (body > volumeOf_Body)  : #if UPDOWN != aryOf_UpDownPattern[0] or body 

            #debug
            print()
            print ("[%s:%d] NOT match => %s ========= (diff = %.3f)" % \
                   (os.path.basename(libs.thisfile()), libs.linenum()
                    , d1.dateTime_Local
                    , (d1.price_Close - d1.price_Open)
                    ))
#             print ("[%s:%d] NOT match => %s =========" % \
#                    (os.path.basename(libs.thisfile()), libs.linenum(), d1.dateTime_Local))
            print()
            
            ### next i
            continue
        
        else : #if UPDOWN != aryOf_UpDownPattern[0] or body 
        
            ### step : 1-1
            flag_IN = True
            
            ### count
            cntOf_IN += 1
            
            #debug
            print()
            print ("[%s:%d] MATCH => %s ################# (diff = %.3f)" % \
                   (os.path.basename(libs.thisfile()), libs.linenum()
                    , d1.dateTime_Local
                    , (d1.price_Close - d1.price_Open)
                    ))
            print()
            
            '''###################
                for : j        
            ###################'''
            for j in range(len2):
            
                d2 = aryOf_BarDatas[i + j]
                
            #/for j in range(len2):

                
            
        #/if UPDOWN != aryOf_UpDownPattern[0] or body 
        
        
        
        
        '''###################
            step : j : 1        
        ###################'''

        
    #/for i in range(len1 - len2):
    
    '''###################
        report : count        
    ###################'''
    ratio = 1.0 * cntOf_IN / len1
    
    print()
    print ("[%s:%d] cntOf_IN => %d (total = %d / %.2f %%)" % \
           (os.path.basename(libs.thisfile()), libs.linenum()
            , cntOf_IN
            , len1
            , ratio * 100   # percentage
            
            ))

    print()
    
    
    
    return None
    
#/get_AryOf_BarDatas_PatternMatched__Body_UpDown(aryOf_BarDatas)

'''###################
    @param threshHold_Up: unit ---> JPY
                        e.g. 0.25
    @return: lo_Matched
            => list of matched BarData isntances
###################'''
def pattern_Match__Body_Updown \
(lo_BarDatas, lo_Updowns, threshHold_Up, threshHold_Down):
    
    len1 = len(lo_BarDatas)
    
    len2 = len(lo_Updowns)
    
#     lo_Temp = []
    
    lo_Matched = []
    
    cnt_Match_Start = 0
    cnt_Match_All = 0
    
    '''###################
        loop : for: i        
    ###################'''
    # body volume ---> more than threshHold
    # 1 : Up / 0 : Down / -1 : Other
    flag_UpDown = 0
    
    flag_In = False
    
    for i in range(len1 - len2):

        d1 = lo_BarDatas[i]
        
        d1b = d1.price_Close - d1.price_Open
        
        # up/down
        if d1b >= threshHold_Up : #if d1b >= threshHold
    
            flag_UpDown = 1
    
        elif d1b <= threshHold_Down : #if d1b >= threshHold
#         elif d1b =< threshHold_Down : #if d1b >= threshHold
    
            flag_UpDown = 0
    
        else : #if d1b >= threshHold
        
            flag_UpDown = -1
        
        #/if d1b >= threshHold
    
        '''###################
            judge : j1        
        ###################'''
        if flag_UpDown == lo_Updowns[0] : #if flag_UpDown == lo_Updowns[0]
            
            ### count
            cnt_Match_Start += 1
            
            ### flag ---> set
            
            flag_In = True
            
            #debug
            print()
            print("[%s:%d] !!!!!!!!!! flag_In ==> True (%s)" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , d1.dateTime_Local
                ), file=sys.stderr)
            
            '''###################
                loop : for : j        
            ###################'''
            for j in range(1, len2):
            
                ### get : the second data
                d2 = lo_BarDatas[i + j]
                
                ### get : body volume
                d2b = d2.price_Close - d2.price_Open
                
                ### set : updown flag
                if d2b >= threshHold_Up : #if d1b >= threshHold
            
                    flag_UpDown = 1
            
                elif d2b <= threshHold_Down : #if d1b >= threshHold
        #         elif d1b =< threshHold_Down : #if d1b >= threshHold
            
                    flag_UpDown = 0
            
                else : #if d1b >= threshHold
                
                    flag_UpDown = -1
                
                #/if d1b >= threshHold

                '''###################
                    judge : 2        
                ###################'''
                if flag_UpDown == lo_Updowns[j] : #if flag_UpDown == lo_Updowns[j]
                    
                    #ref pass https://stackoverflow.com/questions/690622/whats-a-standard-way-to-do-a-no-op-in-python answered Mar 27 '09 at 17:05
#                     pass
                    #debug
                    print()
                    print("[%s:%d] !!!!! flag_UpDown == lo_Updowns[%d] / d2 = %s" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , j, d2.dateTime_Local
                    ), file=sys.stderr)
                
                else : #if flag_UpDown == lo_Updowns[j]
                
                    ### reset : flag
                    flag_In = False
                    
                    ### loop j : exit
                    break
                
                #/if flag_UpDown == lo_Updowns[j]


                
            #/for j in range(1, len2):
            
            '''###################
                judge : 3        
            ###################'''
            if flag_In == True : #if flag_In == True

                '''###################
                    append : matched data        
                ###################'''
                '''###################
                    j3,y1
                ###################'''
                lo_Temp = []
                
                for index in range(len2):
                
                    lo_Temp.append(lo_BarDatas[i + index])
                    
                #/for index in range(len2):
                
                '''###################
                    j3,y2        
                ###################'''
                lo_Matched.append(lo_Temp)
                
                ### flag : reset
                flag_In = False
                
#                 ### clear : temp list
#                 lo_Temp.clear()
            
            else : #if flag_In == True
            
                pass
            
            #/if flag_In == True


        
        else : #if flag_UpDown == lo_Updowns[0]

            '''###################
                j1,n1        
            ###################'''

            ### reset flag
            flag_In = False
    
        #if flag_UpDown == lo_Updowns[0]
        
    #/for i in range(len1 - len2):

    '''###################
        report        
    ###################'''
    ### Start match
    print()
    print("[%s:%d] cnt_Match_Start => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , cnt_Match_Start
            ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return lo_Matched
#     return None
    
#/def pattern_Match__Body_Updown(lo_BarDatas, lo_Updowns, volumeOf_Body):

'''###################
    refer : C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6\82_6.py        
            exec_prog__PatternMatch_RSI()
    @return: 
        None    => libfx.get_ChartData_CSV returned None
        None    => libfx.conv_CSVRows_2_BarDatas returned None
###################'''
def get_Listof_BarDatas():
    
    '''######################################
        get data : raw csv rows
    ######################################'''
    #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
    #ref https://docs.python.org/3.5/library/enum.html
    fname_In = cons_fx.FPath.dpath_In_CSV.value \
            + "/" \
            + cons_fx.FPath.fname_In_CSV.value

    header_Length   = 2
    
    skip_Header     = False
    
    '''###################
        validate : file exists        
    ###################'''
    #ref https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists answered Sep 17 '08 at 12:57
    is_File = os.path.isfile(fname_In)
    
    if is_File == False : #if is_File == False
                    
        print()
        print("[%s:%d] is_File => False" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
        return None
        
    #/if is_File == False
    
#     #test
#     path = Path(sys.executable)
#     root_or_drive = path.root or path.drive
#     
#     print()
#     print("[%s:%d] root_or_drive => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 ,root_or_drive
#                 ), file=sys.stderr)
    
            #     [libfx.py:1760] root_or_drive => \
            # [C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\mm\libs_mm\libfx.py
            # :231] file => opened : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projec

    '''######################################
        get : list        
    ######################################'''
    '''###################
        get : csv data        
    ###################'''
    lo_CSVs = libfx.get_ChartData_CSV(\
                    fname_In, header_Length, skip_Header)
    
#     print()
#     print("[%s:%d] len(lo_CSVs) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_CSVs)
#                 ), file=sys.stderr)
    
    '''###################
        csv : convert to BarData
    ###################'''
    lo_BarDatas = libfx.conv_CSVRows_2_BarDatas(lo_CSVs[header_Length:])
    
    print()
    print("[%s:%d] len(lo_BarDatas) => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
        ### Validate
    if lo_BarDatas == None : #if aryOf_BarDatas == None
    
        print ("[%s:%d] aryOf_BarDatas => None" % (os.path.basename(libs.thisfile()), libs.linenum()))
        print()
        
        return None
    
    #/if lo_BarDatas == None

    '''###################
        return        
    ###################'''
#     return None
    return lo_BarDatas
    
#/def get_Listof_BarDatas():
    
'''###################
    refer : C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6\82_6.py        
            exec_prog__PatternMatch_RSI()
    @return: 
        None    => libfx.get_ChartData_CSV returned None
        None    => libfx.conv_CSVRows_2_BarDatas returned None
###################'''
def get_Listof_BarDatas_2(dpath, fname, header_Length = 2, skip_Header = False):
    
    '''######################################
        get data : raw csv rows
    ######################################'''
    #ref enum https://qiita.com/methane/items/8612bdefd8fa4238cc44
    #ref https://docs.python.org/3.5/library/enum.html
    fname_In = "%s/%s" % (dpath, fname)
#     fname_In = cons_fx.FPath.dpath_In_CSV.value \
#             + "/" \
#             + cons_fx.FPath.fname_In_CSV.value

#     header_Length   = 2
#     
#     skip_Header     = False
    
    #debug
#     print()
#     print("[%s:%d] fname_In => %s" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         , fname_In
#                         ), file=sys.stderr)

    msg = "fname_In => %s" % (fname_In)
    
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
    
    libs.write_Log(
                msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 2)
    
    '''###################
        validate : file exists        
    ###################'''
    #ref https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists answered Sep 17 '08 at 12:57
    is_File = os.path.isfile(fname_In)
    
    if is_File == False : #if is_File == False
                    
        print()
        print("[%s:%d] is_File => False" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
        return None
        
    #/if is_File == False
    
    '''######################################
        get : list        
    ######################################'''
    '''###################
        get : csv data        
    ###################'''
    lo_CSVs = libfx.get_ChartData_CSV(\
                    fname_In, header_Length, skip_Header)
    
#     print()
#     print("[%s:%d] len(lo_CSVs) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_CSVs)
#                 ), file=sys.stderr)
    
    '''###################
        csv : convert to BarData
    ###################'''
    lo_BarDatas = libfx.conv_CSVRows_2_BarDatas(lo_CSVs[header_Length:])
    
#     print()
#     print("[%s:%d] len(lo_BarDatas) => %d" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , len(lo_BarDatas)
#                 ), file=sys.stderr)
    
        ### Validate
    if lo_BarDatas == None : #if aryOf_BarDatas == None
    
        print ("[%s:%d] aryOf_BarDatas => None" % (os.path.basename(libs.thisfile()), libs.linenum()))
        print()
        
        return None
    
    #/if lo_BarDatas == None

    '''###################
        return        
    ###################'''
#     return None
    return lo_BarDatas, lo_CSVs[:header_Length]
#     return lo_BarDatas
    
#/def get_Listof_BarDatas():
    
'''###################
    get_LO_BarData___By_Datetime
    
    at : 2018/07/08 12:50:57
    
    <Meta data>
    @param time_Start: e.g. "2018.05.09"
    @param flag_Period_Open: when True, comarison of datetimes will be
                            based on the open period, i.e. those BarDatas
                            with either of the two datetimes won't be
                            in the resulting list; whe False, otherwise.
    
    @return: list of BarData instances matchig the filter values
    
    <What it does>
    filtering : time_Start < x < time_End
    
    <example>
    time_Start = "2018.05.09"
    time_End = "2018.05.11"
    
    ==> returns list of BarDatas whose "dateTime_Local" are
            between the two datetimes (open period i.e. those
            BarDatas with either of the two datetimes won't be
            in the resulting list.)
    
###################'''
def get_LO_BarData___By_Datetime(lo_BarData, time_Start, time_End, flag_Period_Open = True):
    
    '''###################
        vars
    ###################'''
    lo_BarDatas__By_Datetime = []
    
    '''###################
        ops        
    ###################'''
    lenOf_List = len(lo_BarData)
    
    for i in range(lenOf_List):

        bar_Data = lo_BarData[i]
        
        dateLocal = bar_Data.dateTime_Local
#         dateLocal = bar_Data.datetime_Local
        
        # compare
        # default : open period
        cmp_Period = (dateLocal > time_Start and dateLocal < time_End)
#         cmp_Period_Open = dateLocal > time_Start and dateLocal < time_End
        
        # closed period
        if flag_Period_Open == False : #if flag_Period_Open == False
                            
            cmp_Period = (dateLocal >= time_Start and dateLocal <= time_End)
            
        #/if flag_Period_Open == False
        
#         if dateLocal > time_Start \
#             and dateLocal < time_End : #if dateLocal > 
        if cmp_Period : #if dateLocal > 

            lo_BarDatas__By_Datetime.append(bar_Data)
            
        #/if dateLocal > 
        
    #/for i in range(lenOf_List):
    
    print()
    print("[%s:%d] len(lo_BarDatas__By_Datetime) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_BarDatas__By_Datetime)
            ), file=sys.stderr)
    
    '''###################
        return        
    ###################'''
    return lo_BarDatas__By_Datetime

#/ def get_LO_BarData___By_Datetime(lo_BarData, time_Start, time_End):
    
def BUSL_2(lo_BarData):
    
    print()
    print("[%s:%d] lo_BarData[0] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    print(lo_BarData[0].dateTime_Local)
    print("[%s:%d] lo_BarData[-1] =>" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    print(lo_BarData[-1].dateTime_Local)
#     print(lo_BarData[0])

    '''###################
        for-loop
    ###################'''
    # length
    lenOf_LO_BarData = len(lo_BarData)
    
    # number of bars to be referred
    numOf_BarDatas_Referred = 2
    
    # counter
    cntOf_Both2Bars_Up = 0
    
    # loop
    #ref range https://www.pythoncentral.io/pythons-range-function-explained/
    for i in range((numOf_BarDatas_Referred - 1), lenOf_LO_BarData):
#     for i in range(2, lenOf_LO_BarData):

        '''###################
            p1 : get BarData instances        
        ###################'''
        e_0 = lo_BarData[i - 1]
        e_1 = lo_BarData[i]
#         e_0 = lo_BarData[i - 1]
#         e_1 = lo_BarData[i - 2]
        
        '''###################
            p2 : get BarData body
        ###################'''
        diff_0 = e_0.diff_OC
        diff_1 = e_1.diff_OC
        
        #debug
#         print()
#         print("[%s:%d] e_0.dateTime_Local = %s, e_1.dateTime_Local = %s" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , e_0.dateTime_Local, e_1.dateTime_Local
#                     ), file=sys.stderr)
        
#         msg = "e_0.dateTime_Local = %s, e_1.dateTime_Local = %s" %\
#             (e_0.dateTime_Local, e_1.dateTime_Local)
#         msg_Log = "[%s / %s:%d] %s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg)
#         
#         libs.write_Log(msg_Log
#                     , cons_fx.FPath.dpath_LogFile.value
#                     , cons_fx.FPath.fname_LogFile.value
#                     , 1)

        
#         print("[%s:%d] diff_0 = %.03f, diff_1 = %.03f" % \
#                     (os.path.basename(libs.thisfile()), libs.linenum()
#                     , diff_0, diff_1
#                     ), file=sys.stderr)
#         msg = "diff_0 = %.03f, diff_1 = %.03f" %\
#             (diff_0, diff_1)
#         msg_Log = "[%s / %s:%d] %s" % \
#                 (
#                 libs.get_TimeLabel_Now()
#                 , os.path.basename(libs.thisfile()), libs.linenum()
#                 , msg)
#         
#         libs.write_Log(msg_Log
#                     , cons_fx.FPath.dpath_LogFile.value
#                     , cons_fx.FPath.fname_LogFile.value
#                     , 1)
        '''###################
            j1 : both bars are up        
        ###################'''
        if diff_0 > 0 and diff_1 > 0 : #if diff_0 > 0 and diff_1 > 0
            
            # count
            cntOf_Both2Bars_Up += 1
            
            # message
            
#             msg = "BOTH UP : diff_0 = %.03f, diff_1 = %.03f" %\
#             msg = "BOTH UP : diff_0 = %.03f, diff_1 = %.03f, e_0.dateTime_Local = %s, e_1.dateTime_Local = %s" %\
            msg = "BOTH UP : diff_0 = %.03f, diff_1 = %.03f, e_0.dateTime_Local = %s, e_1.dateTime_Local = %s diff from BB.Main = %.03f" %\
                        (diff_0, diff_1, e_0.dateTime_Local, e_1.dateTime_Local, (e_1.price_Close - e_1.bb_Main))
#                         (diff_0, diff_1, e_0.dateTime_Local, e_1.dateTime_Local)
#                         (diff_0, diff_1, e_0.dateTime_Local, e_1.dateTime_Local)

            print("[%s:%d] %s" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , msg
                        ), file=sys.stderr)
                
#             msg_Log = "[%s / %s:%d] %s" % \
            msg_Log = "[%s / %s:%d]\n%s" % \
                    (
                    libs.get_TimeLabel_Now()
                    , os.path.basename(libs.thisfile()), libs.linenum()
                    , msg)
             
            libs.write_Log(msg_Log
                        , cons_fx.FPath.dpath_LogFile.value
                        , cons_fx.FPath.fname_LogFile.value
                        , 1)
            
            
        else : #if diff_0 > 0 and diff_1 > 0
        
            pass
        
        #/if diff_0 > 0 and diff_1 > 0
            
            
        
        
#         break
        
    #/for i in range(2,:

#     msg = "Both 2 bars up => %d incidents" %\
    msg = "Both 2 bars up => %d incidents (total = %d / ratio = %.02f" %\
                (cntOf_Both2Bars_Up, lenOf_LO_BarData, (cntOf_Both2Bars_Up * 1.0 / lenOf_LO_BarData))
#                 (cntOf_Both2Bars_Up)
                
    print("[%s:%d] %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , msg
                ), file=sys.stderr)
        
    msg_Log = "[%s / %s:%d] %s" % \
            (
            libs.get_TimeLabel_Now()
            , os.path.basename(libs.thisfile()), libs.linenum()
            , msg)
     
    libs.write_Log(msg_Log
                , cons_fx.FPath.dpath_LogFile.value
                , cons_fx.FPath.fname_LogFile.value
                , 1)



    '''###################
        return        
    ###################'''
    return False
    
#/ def BUSL_2(lo_BarData):

'''###################
    sort_LO_BarData__By_Datetime(lo_BarData, orderOf_Sort = 1)
    
    @param orderOf_Sort: 1 ==> new --> old
                        2 ==> old --> new
    
    @return: list of BarDatas
    
###################'''
def sort_LO_BarData__By_Datetime(lo_BarData, orderOf_Sort = 1) :    
    
    '''###################
        get : reference data        
    ###################'''
    data_First = lo_BarData[0]
    data_Last = lo_BarData[-1]
    
    # if True --> the original list is on old-new order
    # if False --> the original list is on new-old order
    cmp_DateTime_Local = data_First.dateTime_Local > data_Last.dateTime_Local
    
    '''###################
        judge        
    ###################'''
    if (cmp_DateTime_Local == True and orderOf_Sort == 2) : #if (cmp_DateTime_Local == True and orderOf_Sort == 2)
            
        lo_BarData.reverse()
        
#         return lo_BarData
            
    elif (cmp_DateTime_Local == False and orderOf_Sort == 1) : #if (cmp_DateTime_Local == True and orderOf_Sort == 2)
            
        lo_BarData.reverse()
        
#         return lo_BarData
            
    else : #if (cmp_DateTime_Local == True and orderOf_Sort == 2)
        
        pass
    
    #/if (cmp_DateTime_Local == True and orderOf_Sort == 2)
            
    '''###################
        return        
    ###################'''
    return lo_BarData
    
            
    

#/ def sort_LO_BarData__By_Datetime(list : lo_BarData, int orderOf_Sort = 1) :    

'''###################
    get_LO_PairOf_Time_StartEnd(str_Date)
    
    at : 2018/07/09 09:16:49
    
    @param str_Date : e.g. "2018.07.07"
    
    @return: list of pair of datetimes
            [('2018.07.07 01:00', '2018.07.07 01:30'), ('2018.07.07 01:30', '2018.07.07 02:0
            0'), ('2018.07.07 02:00', '2018.07.07 02:30'), ('2018.07.07 02:30', '2018.07.07
            03:00'), ('2018.07.07 03:00', '2018.07.07 03:30'), ('2018.07.07 03:30', '2018.07
            .07 04:00'), ('2018.07.07 04:00', '2018.07.07 04:30'), ('2018.07.07 04:30', '201
            8.07.07 05:00'), ('2018.07.07 05:00', '2018.07.07 05:30'), ('2018.07.07 05:30',
            '2018.07.07 06:00'), ('2018.07.07 06:00', '2018.07.07 06:30'), ('2018.07.07 06:3
            0', '2018.07.07 07:00')]
    
###################'''
def get_LO_PairOf_Time_StartEnd(str_Date) :
    
    lo_Datetime = []
    
    lo_Minutes = ["00", "30"]
    
    hour_Start = 1
    hour_End = 6
    
    for i in range(hour_Start, hour_End + 1):
#     for i in range(1,7):
        
        tmp_1 = str_Date + " " + "0" + str(i) + ":" + lo_Minutes[0]
        tmp_2 = str_Date + " " + "0" + str(i) + ":" + lo_Minutes[1]
        tmp_3 = str_Date + " " + "0" + str(i + 1) + ":" + lo_Minutes[0]
        
#         residue = len(lo_Minutes) % 2
#         
#         tmp += ":" + lo_Minutes[residue]
            

        
        lo_Datetime.append((tmp_1, tmp_2))
        lo_Datetime.append((tmp_2, tmp_3))
#         lo_Datetime.append((tmp_1, tmp_2))
#         lo_Datetime.append(tmp)
        
    #/for i in range(1,7):

    # return
    return lo_Datetime
    
#/ def get_LO_PairOf_Time_StartEnd(str_Date) :

