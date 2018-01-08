# -*- coding: utf-8 -*-
'''
C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libfx.py

'''

import inspect
import os

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
from __builtin__ import str
from sympy.physics.vector.printing import params
from sympy.matrices.densetools import row
from _ast import If
# from curses.ascii import NUL

'''###################
    libs : C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libs.py
###################'''
import libs

import csv
import sys

import cons

###############################################

def test_func():
    
    print "[%s:%d] test_func()" % (thisfile(), linenum())
    

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
    
    print "[%s:%d] file => opened : %s" % (libs.thisfile(), libs.linenum(), fname_In)
    
    '''###################
        file : read
    ###################'''
    '''###################
        skip header
    ###################'''
    print "[%s:%d] skip headers => %d lines" % \
                    (libs.thisfile(), libs.linenum(), header_Length)
    
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
        
        print "[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum())
        
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
        print "[%s:%d] row =>" % (libs.thisfile(), libs.linenum())
        
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
    
    print "[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fname_In)

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
    f = open(fname_In, 'rb')
    
    print "[%s:%d] file => opened : %s" % (libs.thisfile(), libs.linenum(), fname_In)
    
    '''###################
        file : read
    ###################'''
    '''###################
        skip header
    ###################'''
    print "[%s:%d] skip headers => %d lines" % \
                    (libs.thisfile(), libs.linenum(), header_Length)
    
    #ref delimiter https://docs.python.org/3.5/library/csv.html
#     delim = ';'
    reader = csv.reader(f, delimiter = delim)
    
    # validate
    if reader is None:
#     if data_Csv is None:
        
        print "[%s:%d] read lines => None" % (libs.thisfile(), libs.linenum())
        
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
            
            print "[%s:%d] header skipped => %d lines" % \
                        (libs.thisfile(), libs.linenum(), header_Length)
            
        #/if skip_Header == True


        
        '''###################
            read rows        
        ###################'''
        count = 0
        
        for row in reader : 
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
    
    print "[%s:%d] file => closed : %s" % \
                (libs.thisfile(), libs.linenum(), fname_In)

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
    
#     print "[%s:%d] result[0] => %s" % (libs.thisfile(), libs.linenum(), result[0])
#     print
    
    #debug
    print "[%s:%d] len(result) => %d" % \
                (libs.thisfile(), libs.linenum(), len(result))
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
    print "[%s:%d] len(aryOf_BarDatas) => %d" % \
                (libs.thisfile(), libs.linenum(), len(aryOf_BarDatas))
    print
    
    #debug
    print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
                (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].no)
    print "[%s:%d] aryOf_BarDatas[%d].price_Open => %.3f" % \
                (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].price_Open)
    print "[%s:%d] aryOf_BarDatas[%d].diff_OC => %.3f" % \
                (libs.thisfile(), libs.linenum(), 0, aryOf_BarDatas[0].diff_OC)
                
    print
    print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
                (libs.thisfile(), libs.linenum(), 1, aryOf_BarDatas[1].no)
    print "[%s:%d] aryOf_BarDatas[%d].id => %d" % \
                (libs.thisfile(), libs.linenum(), 2, aryOf_BarDatas[2].no)
    print
    
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
    
    #ref extend https://stackoverflow.com/questions/10487278/how-to-declare-and-add-items-to-an-array-in-python
    aryOf_Price_OpenClose.extend([x.price_Close for x in target_Ary])
#     aryOf_Price_Close = [x.price_Close for x in target_Ary]
#     sum = [x for x.price_Open in target_Ary]
    
#     aryOf_Price_OpenClose = aryOf_Price_Open.extend(aryOf_Price_Close)
    
    print "[%s:%d] aryOf_Price_OpenClose => %s" % \
                (libs.thisfile(), libs.linenum(), aryOf_Price_OpenClose)
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
    @param typeOf_Data: type of data to obtain
            e.g. "OpenClose"
    @return: dict of max, min and diff
            e.g. {'OC' : [112.677, 112.57, 0.107], 'HL' : [...], ...}
###################'''
def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End) :
# def get_HighLowDiffs(aryOf_BarDatas, typeOf_Data, id_Start, id_End) :
    
    '''###################
        prep : target array        
    ###################'''
    #ref slice https://www.pythoncentral.io/how-to-slice-listsarrays-and-tuples-in-python/
    target_Ary = aryOf_BarDatas[id_Start : (id_End + 1)]
    
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
    
    '''######################################
        data : final product        
    ######################################'''
    dict = {cons.LABEL_OC : aryOf_HighLowDiff__OC}
    
    return dict
#     return aryOf_HighLowDiff__OC
    
#/get_HighLowDiffs(aryOf_BarDatas)
