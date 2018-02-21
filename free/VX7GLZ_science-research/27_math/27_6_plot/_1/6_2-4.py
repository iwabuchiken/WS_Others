# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_1\6_2-4.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17.1.py
at : 2018/02/21 10:34:31

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_1
python 6_2-4.py

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


import sys, os
from cProfile import label
from pip._vendor.requests.sessions import session
import cmd

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# 
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')

from libs_VX7GLZ import libs_VX7GLZ
from libs_27_6_1 import cons_27_6_1

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
from sympy.matrices import *

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random, glob
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.patches as mpatches, random as rd
from shutil import copyfile
from scipy.stats.stats import pearsonr

from matplotlib.dates import DateFormatter, WeekdayLocator,\
    DayLocator, MONDAY
from matplotlib.finance import quotes_historical_yahoo_ohlc, candlestick_ohlc
from matplotlib.lines import Line2D  


###############################################
def get_FFMpeg_Paths():
    
    '''###################
        file path        
    ###################'''
    PROJECT_ROOT = cons_27_6_1.FPath.PROJECT_ROOT.value
#     PROJECT_ROOT = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\1_\\_17"
    
    dname_Folder_Data = "data.27_6_1"
    dname_Images = "images"
    dname_Images_PNG = "images_20180220_140814"
    session_Label = "6_1.test-1"
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Out = "%s\\%s" % (PROJECT_ROOT, dname_Folder_Data)
    fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)
    dpath_Full = "%s\\%s\\%s" % (dpath_Out, dname_Images, dname_Images_PNG)
    fpath_Glob = "%s\\*(*).png" % (dpath_Full)
#     dpath_In = "%s" + "\\%s" + "\\%s" \
#             + "%s" \
    dpath_In = "%s\\%s\\%s" \
            % (PROJECT_ROOT, dname_Folder_Data, dname_Images)
            
    dpath_In = "%s\\%s" % (dpath_In, dname_Images_PNG)
#     dpath_In = "%s\\%s\\%s" \
#             + "%s" \
#             % (PROJECT_ROOT, dname_Folder_Data, dname_Images, dname_Images_PNG)
#             + "\\images\\images_20180220_141141"
    fpath_In_FFMpeg = "%s\\image.%%03d.png" % (dpath_In)
#     fpath_In = "%s\\image.%03d.png" % (dpath_In)
    
    fpath_Out_FFMpeg = "%s\\movie.%s.mp4" % (dpath_In, libs.get_TimeLabel_Now())
    
#     dpath_Out = "%s\\data.27_6_1" % (PROJECT_ROOT)
    
    ### fpath full
    
    

#     dname_Images_PNG = "images_20180220_140223"
#     dname_Images_PNG = "images_20180220_141101"
    
#     dpath_Full = "%s\\images_20180220_141141" % (dpath_Out)
#     dpath_Full = "%s\\%s\\images_20180220_141141" % (dpath_Out, dname_Images)
    
    
#     dpath_In = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research" \
#             + "\\28_Physics\\1_\\_17\\data_1_17.1" \
            

    '''###################
        return        
    ###################'''
    return dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg
    
    
#/def get_FFMpeg_Paths():

def test_2_mpl_finance():
    
    '''###################
        ref : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\mpl_finance\mpl_finance.py        
    ###################'''
    fig = plt.figure()
    
    ax = fig.add_subplot(111)
    
    x = [rd.randint(1,10) for x in range(1,10)]
    y = [rd.randint(1,10) for x in range(1,10)]
#     x = [10,24,23,23,3]
#     y = [12,2,3,4,2]
    
    line = Line2D(x, y)
    ax.add_line(line)
    
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))
    
    plt.show()
    
        
#/def test_2_mpl_finance():    

def test_1():

    #ref https://matplotlib.org/examples/pylab_examples/finance_demo.html

    # (Year, month, day) tuples suffice as args for quotes_historical_yahoo
    date1 = (2004, 2, 1)
    date2 = (2004, 4, 12)
    
    
    mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
    alldays = DayLocator()              # minor ticks on the days
    weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
    dayFormatter = DateFormatter('%d')      # e.g., 12
    
    print()
    print("[%s:%d] mondays => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , mondays
                ), file=sys.stderr)
    
    quotes = quotes_historical_yahoo_ohlc('INTC', date1, date2)
    
    
#/def test_4():


def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_2_mpl_finance()
#     test_1()
    
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
    exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(libs.thisfile())), libs.linenum()))



