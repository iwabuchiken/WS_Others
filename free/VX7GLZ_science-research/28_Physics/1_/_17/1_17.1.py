# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17.1.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17_3.py
at : 2018/02/20 13:34:36

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17
python 1_17.1.py

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

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# 
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')

from mm.libs_mm import cons_mm, cons_fx, libs, libfx

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.patches as mpatches
from shutil import copyfile
from scipy.stats.stats import pearsonr

###############################################

def test_1():
    
    '''###################
        file path        
    ###################'''
    PROJECT_ROOT = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\1_\\_17"
    
    dpath_Out = "%s\\data_1_17.1" % (PROJECT_ROOT)
    
    ### fpath full
    tlabel = libs.get_TimeLabel_Now()
    
    session_Label = "1_17.1"
    
    fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)
    
    '''###################
        ops        
    ###################'''
    
    x = np.linspace(0, np.pi * 2, 100)
#     x = np.linspace(0, np.pi, 1000)
    
    y = np.sin(x)
    
    # graph : settings
    plt.ylim(-2,2)
    plt.xlim(0, np.pi * 2)
    plt.grid(b=None, which='major', axis='both')
    plt.xticks(np.arange(0, np.pi*2, np.pi / 4))
    plt.yticks(np.arange(-2, 2, 0.5))
#     plt.yticks([-2,-1,1,2])
#     plt.xticks([-2,-1,1,2])

    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("x ~ sin(x)\n%s" % (os.path.basename(fpath_Full)))

    # plot
    plt.plot(x, y)

    plt.savefig(fpath_Full)
    plt.show()
    
#/def test_2():


def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_1()
    
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



