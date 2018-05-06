'''###################
            
    C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\curr\data\miscs
    
###################'''

'''###################
    import : django        
###################'''
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django import template
#ref https://stackoverflow.com/questions/29304845/how-to-disable-cache-in-django-view
from django.views.decorators.cache import never_cache

'''###################
    import : original files        
###################'''
import sys
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')
sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from mm.libs_mm import libs
# from mm.libs_mm import libfx

from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import os
#ref https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
from os import listdir
from os.path import isfile, join, splitext
# from os.path import splitext

from sympy.physics.units.dimensions import action
from pip._vendor.requests.api import request
from macpath import defpath
from pathlib import Path

import subprocess, copy, time, glob, re, datetime
#from C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_\1_1.3.py
import xml.etree.ElementTree as ET

# import datetime
# import copy
# import time

# import glob

# import re




'''######################################
    funcs        
######################################'''
def write_Log(str_Line):

    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    #                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
    
#     msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#             )
    fout.write(str_Line)
    
    fout.write("\n")
    
    fout.close()

#/ def write_Log(str_Line):


def exec_correlations(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    message = "done (time : %02.3f sec)" % (time_Elapsed)

    dic = {"msg" : message}
    
#     print()
#     print("[%s:%d] rendering..." % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         
#         ), file=sys.stderr)
    
    return render(request, 'curr/exec_correlations.html', dic)
    
#/def exec_correlations(request):
    
def correlations(request):
    
    dic = {}
    
    return render(request, 'curr/correlations.html', dic)
    
#/def correlations(request):
    
def exec_updown_patterns(request):
    
    '''###################
        time        
    ###################'''
    time_Start = time.time()
    
    '''###################
        param : body volume : up        
    ###################'''
    threshHold_Up = request.GET.get('body_volume_up', False)
    
    if threshHold_Up == False : #if threshHold_Up == False

        threshHold_Up = 0.1
        
    else:
        
        threshHold_Up = float(threshHold_Up)
        
    #/if threshHold_Up == False
    
    '''######################################
        updown
    ######################################'''
    '''###################
        get : list of bardatas        
    ###################'''
    lo_BarDatas = libfx.get_Listof_BarDatas()
    
    # validate
    alert = ""
    
    if lo_BarDatas == None : #if lo_BarDatas == None

        print()
        print("[%s:%d] lo_BarDatas => None" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            ), file=sys.stderr)
        
        # set : message
        alert = "ERROR : Get BarData ==> returned None"
        
    #/if lo_BarDatas == None

    '''###################
        pattern match  
              
    ###################'''
    lo_Updowns = [1,1,1]
    
#     threshHold_Up = 0.1
    threshHold_Down = 0.1
#     threshHold_Up = 0.2
#     threshHold_Down = 0.2
    
    lo_Matched = libfx.pattern_Match__Body_Updown(
                lo_BarDatas, lo_Updowns, threshHold_Up, threshHold_Down)
    
    '''###################
        report        
    ###################'''
    if len(lo_Matched) > 0 : #if len(lo_Matched) > 0
    
        match_1 = lo_Matched[0]
        
        ### display
        for i in range(len(match_1)):
    
            print()
            print("[%s:%d] match_1[%d].dateTime_Local => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , i, match_1[i].dateTime_Local
                ), file=sys.stderr)
            
        #/for i in range(len(match_1)):

        
#         print()
#         print("[%s:%d] match_1 => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , match_1
#             ), file=sys.stderr)
        
    #/if len(lo_Matched) > 0
    
    '''###################
        time        
    ###################'''
    time_Elapsed = time.time() - time_Start
    
    '''###################
        message        
    ###################'''
    lenOf_Matched = len(lo_Matched)
    
    message = "done (time : %02.3f sec) (matched : %d)" \
                % (time_Elapsed, lenOf_Matched)
#                 % (time_Elapsed, len(lo_Matched))

    print()
    print("[%s:%d] message => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , message
            ), file=sys.stderr)
    
    dic = {"msg" : message, "alert" : alert}
#     dic = {"msg" : message}
    
    '''###################
        save history
    ###################'''
    dpath_Out = DPATH_ROOT_CURR + "/" + "data/log"
    
    fname_Out = "pattern_match_history.log"
    
    fpath_Out_Full = dpath_Out + "/" + fname_Out
    
    fout = open(fpath_Out_Full, "a")
    
    ### timestamp
    fout.write("[%s : pattern match] ======================" \
            % libs.get_TimeLabel_Now(string_type = libs.TimeLabel.STRING_TYPE_BASIC.value))
#                 % libs.get_TimeLabel_Now(string_type = "basic"))
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### file name
    fout.write("file : %s" % cons_fx.FPath.fname_In_CSV.value)
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### updown pattern
    fout.write("updown pattern : %s" % ",".join([str(x) for x in lo_Updowns]))
#     fout.write("updown pattern : %s" % ",".join(lo_Updowns))
#     fout.write("updown pattern : %s" % str_Updown)
    fout.write("\n")
    
    ### threshHold_Up, Down
    fout.write("threshHold_Up = %.3f / threshHold_Down = %.3f" \
                    % (threshHold_Up, threshHold_Down))
    fout.write("\n")
    
    ### num of matched
    fout.write("num of matched : %d" % lenOf_Matched)
#     fout.write("num of matched : %d" % len(lenOf_Matched))
    fout.write("\n")
    
    ### matched data
    if lenOf_Matched > 0 : #if lenOf_Matched > 0
            
        for matched in lo_Matched:
#         for item in lo_Matched:
            
            for item in matched:
            
                fout.write("[%s:%d] datetime : %s / diff = %.3f" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , item.dateTime_Local, (item.price_Close - item.price_Open)
                    )
                )
                 
                fout.write("\n")
                
                
            #/for item in matched:

            ### separator line
            fout.write("\n")
            
#             fout.write("[%s:%d] datetime : %s / diff = %.3f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , item.dateTime_Local, (item.price_Close - item.price_Open)
#                 )
#             )
#             
#             fout.write("\n")
            
        #/for item in lo_Matched:
        
    #/if lenOf_Matched > 0
    
    ### separation line
    fout.write("\n")
    fout.write("\n")
            
    ### close file
    fout.close()
    
    '''###################
        render        
    ###################'''
    return render(request, 'curr/exec_updown_patterns.html', dic)
    
#/def exec_updown_patterns(request):

def updown_patterns(request):

    dic = {}
#     dic = {'action' : action, "message" : message}
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/updown_patterns.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/updown_patterns_full.html', dic)

def basics_Ops(request, lo_BarDatas):
    
    '''###################
        ops        
    ###################'''
    lo_Data = []
    
    cntOf_Item = 0
    
    sumOf_Diff_OC = 0
    
    for item in lo_BarDatas:

        if item.diff_OC >= 0 : #if item.diff_OC >= 0

            val = 1
        
        else : #if item.diff_OC >= 0
        
            val = -1
        
        #/if item.diff_OC >= 0
        
        # append data
        sumOf_Diff_OC += item.diff_OC
        
        lo_Data.append([cntOf_Item, val, item.diff_OC, item.dateTime_Local, sumOf_Diff_OC])
#         lo_Data.append(val)
        
        # count
        cntOf_Item += 1
        
    #/for item in lo_BarDatas:
    
    print()
    print("[%s:%d] lo_Data => " % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
    
    for item in lo_Data[:20]:
            
        print(item)
        
    #/for item in lo_Data[:20]:

#     print(lo_Data[:20])
    
    '''###################
        write data        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "lo_BarDatas.20180502_113828.txt"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
    
    for item in lo_Data:
    
        str_Line = ""
        
        for elem in item:
            
            str_Line += "%s," % elem
        
        fout.write(str_Line)
        
        fout.write("\n")
        
    #/for elem in item:
    
    fout.close()
        
    #/for item in lo_Data:
    
    print()
    print("[%s:%d] lo_Data => written" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
#/ def basics_Ops(request, lo_BarDatas):

def basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath_Data, fname_Data):
# def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
    '''###################
        vars        
    ###################'''
    idx         = 0
    idx_Start   = 0
    sumOf_Diff  = 0.0
    sum_Max     = 0.0
    f_New       = True
    
    lo_Max      = []
    
    idxOf_SumMax = -1
    
    '''###################
        file : finish        
    ###################'''
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
        
    fname = "detect_peaks.log"
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "a")
    
    fout.write("\n")
    fout.write("[%s]======================" % (libs.get_TimeLabel_Now()))
    fout.write("\n")
    
    fout.close()

    '''###################
        flows        
    ###################'''
    lo_BarDatas_Tmp = copy.deepcopy(lo_BarDatas)
    
    lo_BarDatas_Tmp.reverse()
    
    for item in lo_BarDatas_Tmp :
#     for item in lo_BarDatas:
    
#         #debug
#         if idx > 50 : break
    
#         # reset idx_Start
#         if f_New == True : idx_Start = idx
        
        '''###################
            j : 1
        ###################'''
        diff_OC = item.diff_OC
        
        if diff_OC < 0 : #if item.diff_OC < 0
#             #report
# #             msg = "[%s:%d] (%02d) %s : diff_OC < 0 : %03f" % \
#             msg = "[%s:%d] (%02d) %s : diff_OC < 0 : %03f (f_New = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, diff_OC, f_New
#                             )
#                              
#             write_Log(msg)
    
            '''###################
                j : 4
            ###################'''
            if f_New == True : #if f_New == True
                
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
            
            else : #if f_New == True
            
                # sum of dill
                sumOf_Diff += diff_OC
#                 sumOf_Diff -= diff_OC
            
                '''###################
                    j : 5
                ###################'''
                if sumOf_Diff < (sum_Max / 2) : #if sumOf_Diff < (sum_Max / 2)

                    '''###################
                        file : finish        
                    ###################'''
                    dpath = cons_fx.FPath.dpath_Data_Miscs.value
                        
                    fname = "detect_peaks.log"
                    
                    fpath = "%s/%s" % (dpath, fname)
                    
                    fout = open(fpath, "a")
                    
                    fout.write("\n")
#                     fout.write("sumOf_Diff < (sum_Max / 2)" % (libs.get_TimeLabel_Now()))
                    
                    msg = "[%s:%d] (%02d) %s : sumOf_Diff < (sum_Max / 2) : sumOf_Diff = %03f sum_Max = %03f" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , idx, item.dateTime_Local, sumOf_Diff, sum_Max
                            )
                    fout.write(msg)

                    fout.write("\n")
                    
                    fout.close()

                    '''###################
                        ops : sumOf_Diff ---> went under
                    ###################'''
                    # reset flag    ### j : 5 / y : 1
                    f_New = True
                    
                    # report
                    msg = "[%s:%d] (%02d) %s : f_New => back to %s" % \
                            (os.path.basename(libs.thisfile()), libs.linenum()
                            , idx, item.dateTime_Local, f_New
                            )

                    write_Log(msg)
                    
                    '''###################
                        append data        
                    ###################'''
                    # register : sum_Max, idx    ### j : 5 / y : 2
                    data = (round(sum_Max, 3)
                            , int(idx_Start)
                            , round(idxOf_SumMax, 3)
                            , item.dateTime_Local
                            
                            )
#                     data = (round(sum_Max, 3), round(idxOf_SumMax, 3))
                    
                    
                    lo_Max.append(data)
#                     lo_Max.append((round(sum_Max, 3), round(idxOf_SumMax, 3)))
#                     lo_Max.append((sum_Max, idxOf_SumMax))
                    
                    ### j : 5 / y : 3
                    # reset : sum_Max
                    sum_Max = 0.0
                    
                    # reset : sumOf_Diff
                    sumOf_Diff = 0.0
                    
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
                
                else : #if sumOf_Diff < (sum_Max / 2)
                
                    # next index in the loop f1
                    #count
                    idx += 1
                    
                    # next index
                    continue
#                     pass
                
                #/if sumOf_Diff < (sum_Max / 2) ### j : 5
                
                
            
            #/if f_New == True ### j : 3
    
    
        
        else : #if item.diff_OC < 0 ### j : 1
        
#             #report
# #             msg = "[%s:%d] (%02d) %s : diff_OC >= 0 : %03f" % \
#             msg = "[%s:%d] (%02d) %s : diff_OC >= 0 : %03f (f_New = %s)" % \
#                             (os.path.basename(libs.thisfile()), libs.linenum()
#                             , idx, item.dateTime_Local, diff_OC, f_New
#                             )
#                             
#             write_Log(msg)

            # f_New ---> on
            if f_New == True : 
                
                # set flag
                f_New = False
                
                # set : idx_Start
                idx_Start = idx
                
                # report
                dpath = cons_fx.FPath.dpath_Data_Miscs.value
                
                fname = "detect_peaks.log"
                
                fpath = "%s/%s" % (dpath, fname)
                
                fout = open(fpath, "a")
                
                msg = "[%s:%d] (%02d) %s : f_New ==> turned to False" % \
                        (os.path.basename(libs.thisfile()), libs.linenum()
                        , idx, item.dateTime_Local
                        )
                fout.write(msg)
                
                fout.write("\n")
            
            # sum of diff
            sumOf_Diff += diff_OC
            
            '''###################
                j : 2        
            ###################'''
            if sumOf_Diff > sum_Max : #if sumOf_Diff> sum_Max
                
                # update sum_Max
                sum_Max = sumOf_Diff
                
                # update index
                idxOf_SumMax = idx
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue

            else : #if sumOf_Diff> sum_Max
            
                # next index in the loop f1
                #count
                idx += 1
                
                # next index
                continue
#                 pass
            
            #/if sumOf_Diff> sum_Max
            
            
        
        #/if item.diff_OC < 0 ### j : 1
        
#         '''###################
#             report        
#         ###################'''
#         dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#         fname = "detect_peaks.log"
#         
#         fpath = "%s/%s" % (dpath, fname)
#         
#         fout = open(fpath, "a")
#         
#         msg = "[%s:%d] (%02d) %s / diff_OC = %03f / sumOf_Diff = %03f / sum_Max = %03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , idx, item.dateTime_Local, diff_OC, sumOf_Diff, sum_Max
#                 )
#         fout.write(msg)
#         
#         fout.write("\n")
#             
#         #/for elem in item:
#         
#         fout.close()

#         print()
#         print("[%s:%d] (%02d) %s / sumOf_Diff = %03f / sum_Max = %03f" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , idx, item.dateTime_Local, sumOf_Diff, sum_Max
#                 ), file=sys.stderr)
        
        '''###################
            j : 3
            next item
        ###################'''
        # counter
        idx += 1
        
        # next index in the loop f1
        continue
        
    #/for item in lo_BarDatas:

    '''###################
        report : sum_Max
    ###################'''
    print()
    print("[%s:%d] lo_Max ==>" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    
                    ), file=sys.stderr)
    
    print(lo_Max)
#     msg = "[%s:%d] lo_Max ==>" % \
#                         (os.path.basename(libs.thisfile()), libs.linenum()
#                         
#                         )
#                         
#     write_Log(msg)
#     write_Log(lo_Max)
    
    '''###################
        write : lo_Max
    ###################'''
    # report
    dpath = cons_fx.FPath.dpath_Data_Miscs.value
    
    fname = "detect_peaks.sum_Max.%s.log" % libs.get_TimeLabel_Now()
    
    fpath = "%s/%s" % (dpath, fname)
    
    fout = open(fpath, "w")
#     fout = open(fpath, "a")
    
    # header : meta data
    msg = "source = %s (%s)" % \
            (fname_Data, dpath_Data)
#             (fname_Data, dpath_Data)
            
    fout.write(msg)
    
    fout.write("\n")
    
    # header : columns
    #     data = (round(sum_Max, 3)
    #                 , int(idx_Start)
    #                 , round(idxOf_SumMax, 3)
    #                 , item.dateTime_Local
    msg = "Max,idx_Start,idxOf_SumMax,dateTime_Local"
            
    fout.write(msg)
    fout.write("\n")
    
    # write
    for item in lo_Max:
        
            # data = (round(sum_Max, 3), round(idxOf_SumMax, 3))
        msg = "%03f,%02d,%02d,%s" % \
                (item[0], int(item[1]), int(item[2]), item[3])
#                 (item[0], item[1])
                
        fout.write(msg)
        fout.write("\n")
        
    #/for item in lo_Max:

    
    fout.write("\n")
    
    fout.close()

    '''###################
        file : finish        
    ###################'''
    msg = "\n\n"
    
    write_Log(msg)
    
#     dpath = cons_fx.FPath.dpath_Data_Miscs.value
#         
#     fname = "detect_peaks.log"
#     
#     fpath = "%s/%s" % (dpath, fname)
#     
#     fout = open(fpath, "a")
#     
#     fout.write("\n\n")
#     
#     fout.close()

    
#/ def basics_Ops_1__DetectPieaks(request, lo_BarDatas):
    
def basics(request):

    dic = {}
#     dic = {'action' : action, "message" : message}
    
    '''###################
        params
    ###################'''
    
    
    '''###################
        ops
    ###################'''
    dpath = cons_fx.FPath.dpath_In_CSV.value
    
    fname = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"
#     fname = cons_fx.FPath.fname_In_CSV.value
    
    header_Length   = 2
     
    skip_Header     = False

    lo_BarDatas = libfx.get_Listof_BarDatas_2(
                        dpath, fname, header_Length, skip_Header)
    
#     #test
#     lo_BarDatas = None
    
    # validate
    if lo_BarDatas == None : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => None" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)

    
        msg = "lo_BarDatas => None"
        dic = {"msg" : msg}
    
        return render(request, 'curr/error.html', dic)
#         return render(request, 'curr/error.html', msg)

    else : #if lo_BarDatas == None
    
        print()
        print("[%s:%d] lo_BarDatas => %d" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , len(lo_BarDatas)
                ), file=sys.stderr)
    
    #/if lo_BarDatas == None
    result = basics_Ops_1__DetectPieaks(request, lo_BarDatas, dpath, fname)
#     result = basics_Ops_1__DetectPieaks(request, lo_BarDatas)
#     result = basics_Ops(request, lo_BarDatas)
    
    
    '''###################
        get : referer        
    ###################'''
    referer_MM = "http://127.0.0.1:8000/curr/"
    
    referer_Current = request.META.get('HTTP_REFERER')


    '''###################
        render        
    ###################'''
    dic["msg"] = "rendering... (%s)" % libs.get_TimeLabel_Now()
    
    if referer_Current == referer_MM : #if referer_Current == referer_MM
    
        print()
        print("[%s:%d] referer_Current == referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)
    
        return render(request, 'curr/basics.html', dic)
#         return render(request, 'mm/numbering.html', dic)
        
    else : #if referer_Current == referer_MM

        print()
        print("[%s:%d] referer_Current <> referer_MM (current = %s / referer = %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                ,referer_Current, referer_MM
                ), file=sys.stderr)

        return render(request, 'curr/basics_full.html', dic)

#     return render(request, 'curr/updown_patterns.html', dic)

    
#/def basics(request):
    
    
def index(request):


    action = "action"
    message = "message"
    
    lo_Commands = cons_mm.CURROp.lo_Commands.value
#     lo_Commands = cons_mm.ImOp.lo_Commands.value
    
    #debug
    print()
    print(lo_Commands)
    
    dic = {'action' : action, "message" : message, "lo_Commands" : lo_Commands}
    
    return render(request, 'curr/index.html', dic)
#     return render(request, 'mm/index.html', dic)

    
#     return HttpResponse("Hello Django")


