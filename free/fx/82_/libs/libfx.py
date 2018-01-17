#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe

# -*- coding: utf-8 -*-
'''
C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py

'''

import inspect
import os

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
# from __builtin__ import str
from sympy.physics.vector.printing import params
from sympy.matrices.densetools import row
from _ast import If
# from curses.ascii import NUL

'''###################
    libs : C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libs.py
###################'''
from libs import libs
# import libs

import csv
import sys

from libs import cons
# import cons

import copy

import numpy

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
    
    print ("[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fname_In))

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
    
    #debug
    print ("[%s:%d] len(result) => %d" % \
                (libs.thisfile(), libs.linenum(), len(result)))
    print
    
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
    
    #debug
    print ("[%s:%d] len(aryOf_BarDatas) => %d" % \
                (libs.thisfile(), libs.linenum(), len(aryOf_BarDatas)))
    print
    
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
    bb_M1S       = -1.0
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
    cnt_Max = 8
    
    '''###################
        for : i        
    ###################'''
    for i in range(lenOf_Data - lenOf_FlatBars):
        
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
        
        '''###################
            for : j        
        ###################'''
        for j in range(lenOf_FlatBars): # range : 0 ~ 3

            d2 = ary_BarDatas_tmp[j]
            
            '''###################
                get : rsi values        
            ###################'''
            r1 = d1.rsi
            r2 = d2.rsi
            
            diff = r1 - r2
            
        #/for j in range(lenOf_FlatBars:

        
    #/for i in range(lenOf_Data - lenOf_FlatBars):

    
    '''###################
        return        
    ###################'''
    return None

#/get_AryOf_BarDatas_PatternMatched__RSI__V2
