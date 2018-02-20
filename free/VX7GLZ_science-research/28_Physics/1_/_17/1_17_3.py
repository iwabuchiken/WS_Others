# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17_3.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17.py
at : 2018/02/17 13:57:51

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17
python 1_17_3.py

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

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')
# 
# sys.path.append('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/31_Materials')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\mm')
# sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')

# #debug
# for item in sys.path :
#     
#     print(item)

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from mm.libs_mm import libs
# from mm.libs_mm import libfx

# from Admin_Projects.definitions import ROOT_DIR
# from Admin_Projects.definitions import DPATH_ROOT_CURR

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.patches as mpatches
from shutil import copyfile
from scipy.stats.stats import pearsonr

# import cv2

###############################################

def test_4():
    
    #ref https://stackoverflow.com/questions/19390895/matplotlib-plot-with-variable-line-width
    x = np.linspace(0,10,10000)
    y = 2 - 0.5*np.abs(x-4)
    lwidths = (1+x)**2 # scatter 'o' marker size is specified by area not radius 
    plt.scatter(x,y, s=lwidths, color='blue')
    plt.xlim(0,9)
    plt.ylim(0,2.1)
    plt.show()
    
#/def test_4():
    
def test_3():
    
    '''###################
        file path        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\28_Physics\\1_\\_17\\" \
                + "images\\images_%s" % tlabel

#     ### make dir
#     os.makedirs(dpath_Out)
                 
#     ### fpath full
#     fpath_Full = "%s\\tmp.%s.png" % (dpath_Out, )
    
    '''###################
        ops        
    ###################'''
    x = [1]
    y = [0]

#     fig = plt.figure()
#     ax = fig.gca()
#     ax.set_xticks(np.arange(-1, 1, 0.1))
#     ax.set_yticks(np.arange(-1, 1, 0.1))
    
    plt.grid(b=None, which='major', axis='both')
    
    #ref https://stackoverflow.com/questions/19390895/matplotlib-plot-with-variable-line-width answered Nov 29 '14 at 17:42
    plt.scatter(x, y, s = 20)
#     plt.plot(x, y, linewidth = 10)
#     plt.scatter(x, y, s = 1)
#     plt.plot(x, y, linewidth = 1)
#     plt.plot(x, y)
    
#     plt.set_xticks(np.arange(-1, 1, 0.1))
#     plt.set_yticks(np.arange(-1, 1, 0.1))
    
    
    plt.show()
    
    
#/def test_2():

def test_2():
    
    '''###################
        file path        
    ###################'''
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    fpath_Full = "%s\\tmp.%s.png" % (dpath_Out, libs.get_TimeLabel_Now())
    
    '''###################
        ops        
    ###################'''
#     print(cv2.__version__)
    
    fname_In = "image.1-17-2.20180219_093551.png"
    
    img = cv2.imread(fname_In)
    
    print()
    print("[%s:%d] img => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , img
        ), file=sys.stderr)
    
#/def test_2():


def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
#     test_4()
    test_3()
#     test_2()
    
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



