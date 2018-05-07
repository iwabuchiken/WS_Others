# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\10_electromagnetic\1_\10_1.8.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_2\6_2.py
at : 2018/05/08 07:47:28

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\10_electromagnetic\1_
python 10_1.8.py

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
# from cProfile import label
# from pip._vendor.requests.sessions import session
# import cmd
# from mailbox import fcntl

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# 
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1')

# #debug
# for item in sys.path: print(item)


# from libs_VX7GLZ import libs_VX7GLZ
# # from libs_VX7GLZ import cons_VX7GLZ
# from libs_27_6_1 import cons_27_6_1
# # from libs_27_6_2 import *
# from libs_27_6_2 import cons_27_6_2

from mm.libs_mm import libs
# from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from sympy.matrices import *

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random, glob
# import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
import math as math, matplotlib.pyplot as plt \
        , numpy as np
#         , numpy as np, matplotlib.patches as mpatches, matplotlib.cm as cm
from shutil import copyfile
# from scipy.stats.stats import pearsonr
# from matplotlib.patches import Ellipse, Arc
# from math import pi

###############################################
def test_1():
    
    cons_Width = 10
    
    x = np.linspace(- cons_Width * np.pi, cons_Width * np.pi, 1000)
#     x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
#     x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
    
#     fig = plt.figure()
#     
#     ax  = fig.add_subplot(111)
    
    # time label
    tlabel = libs.get_TimeLabel_Now()
    
    # num of files
    numOf_ImageFiles = 30
#     numOf_ImageFiles = 15
    
    for i in range(numOf_ImageFiles):
#     for i in range(6):

        plt_Title = "sin(x - %.02f x np.pi)" % (i / 2 * 3)
#         plt_Title = "sin(x + %.02f x np.pi)" % (i / 2 * 3)
#         plt_Title = "sin(x + %.02f * np.pi)" % (i / 2 * 3)
#         plt_Title = "sin(x + %02f * np.pi)" % (i / 2 * 3)
#         plt_Title = "sin(x + %02f * np.pi)" % (i / 2)
#         plt_Title = "sin(x + %d * np.pi)" % (i)

        plt.title(plt_Title, fontsize = 15)

        y1 = np.sin(x - (i / 2) * np.pi)
#         y1 = np.sin(x + (i / 2) * np.pi)
#         y1 = np.sin(x + i * np.pi)
    #     y2 = np.sin(x * 2)
        
        plt.plot(x, y1)
    #     plt.plot(x, y2)
        
        '''###################
            graph : settings        
        ###################'''
        plt.grid(b=None, which='major', axis='both')
        
    #     x_tick = np.arange(-3*np.pi, 3*np.pi, np.pi / 4)
    #     
    #     x_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]
    #     
    #     plt.set_xticklabels(x_label2, fontsize = 10)
        
        dpath_Images_Out = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\10_electromagnetic\\1_\\images\\8_"
        fname_Images_Out = "image.%s.%s.png" % (tlabel, plt_Title)
#         fname_Images_Out = "image.%s.(sin_+%02f).png" % (tlabel, i / 2)
#         fname_Images_Out = "image.%s.(i=%d).png" % (tlabel, i)
#         fname_Images_Out = "image.%s.png" % (libs.get_TimeLabel_Now())
        
        fpath_Images_Out = "%s\\%s" % (dpath_Images_Out, fname_Images_Out)
        
        plt.savefig(fpath_Images_Out)
        
        # clear plot
        plt.clf()
        
#/for i in range(6):

#     y1 = np.sin(x)
# #     y2 = np.sin(x * 2)
#     
#     plt.plot(x, y1)
# #     plt.plot(x, y2)
#     
#     '''###################
#         graph : settings        
#     ###################'''
#     plt.grid(b=None, which='major', axis='both')
#     
# #     x_tick = np.arange(-3*np.pi, 3*np.pi, np.pi / 4)
# #     
# #     x_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]
# #     
# #     plt.set_xticklabels(x_label2, fontsize = 10)
#     
#     dpath_Images_Out = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\10_electromagnetic\\1_\\images\\8_"
#     fname_Images_Out = "image.%s.png" % (libs.get_TimeLabel_Now())
#     
#     fpath_Images_Out = "%s\\%s" % (dpath_Images_Out, fname_Images_Out)
#     
#     plt.savefig(fpath_Images_Out)
#     plt.show()

    
    
#/def test_4():


def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
#     test_5_1()
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



