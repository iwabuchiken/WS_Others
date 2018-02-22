# -*- coding: utf-8 -*-
'''
file : \free\VX7GLZ_science-research\27_math\27_6_plot\_2\6_2.py
orig : \free\VX7GLZ_science-research\27_math\27_6_plot\_1\6_1.py
at : 2018/02/22 07:18:31

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_2\
python 6_2.py

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
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1')

# #debug
# for item in sys.path: print(item)


from libs_VX7GLZ import libs_VX7GLZ
# from libs_VX7GLZ import cons_VX7GLZ
from libs_27_6_1 import cons_27_6_1
# from libs_27_6_2 import *
from libs_27_6_2 import cons_27_6_2

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
from sympy.matrices import *

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random, glob
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.patches as mpatches
from shutil import copyfile
from scipy.stats.stats import pearsonr
from matplotlib.patches import Ellipse, Arc
from math import pi

###############################################
def _test_3__Generate_PNGFiles(dpath_Full, session_Label):
    
    '''###################
        gen        
    ###################'''
        # dirs
    if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)

    '''######################################
        plot        
    ######################################'''
#     '''###################
#         settings        
#     ###################'''
#     plt.xlim(-2 * np.pi,2 * np.pi)
#     plt.ylim(-2,2)
#     plt.grid(b=None, which='major', axis='both')
    
    tlabel = libs.get_TimeLabel_Now()
    
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    
#     fig = plt.figure()
#     ax  = fig.add_subplot(111)

    '''###################
        constants        
    ###################'''
    lim_X_Start = -5
    lim_X_End = 5
    lim_Y_Start = -5
    lim_Y_End = 5
    
    cnt = 0
    
    x = 1; y = 0
    
    for index in np.arange(0, np.pi * 2, np.pi / 6):

        '''###################
            settings        
        ###################'''
#         plt.xlim(-2, 2)
#         plt.ylim(-2, 2)
        
        plt.grid(b=None, which='major', axis='both')

#         plt.axes().set_aspect('equal', 'datalim')

        fig = plt.figure()
        
        #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
        fig.set_facecolor("#fff9c9")
        
        ax  = fig.add_subplot(111)

        ax.grid(b=None, which='major', axis='both')
        
        #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
        ax.set_aspect('equal')

        #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
        
        ax.set_xlim(lim_X_Start, lim_X_End)
        ax.set_ylim(lim_Y_Start, lim_Y_End)
#         ax.set_xlim(-5,5)
#         ax.set_ylim(-5,5)
#         ax.set_xlim(-2, 2)
#         ax.set_ylim(-2, 2)

        '''###################
            label : y
        ###################'''
        #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
        tickVal_Y = 1
        tickVal_X = 1
        
        # y ax
        y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
        ax.set_yticks(y_tick)
        ax.set_yticklabels(y_tick, fontsize = 10)

        # x ax
        x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
        ax.set_xticks(x_tick)
        ax.set_xticklabels(x_tick, fontsize = 10)

        '''###################
            circle        
        ###################'''
#         #ref https://stackoverflow.com/questions/4143502/how-to-do-a-scatter-plot-with-empty-circles-in-python
#         ax.scatter(0, 0, s = 600, facecolors='none', edgecolors='r')
#         plt.scatter(x, y, s=80, facecolors='none', edgecolors='r')
        
        
        #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
        circle1 = plt.Circle((0, 0), 1.0, color='r', fill= False, linewidth = 1, alpha = 0.5)
#         circle1 = plt.Circle((0, 0), 1.0, color='r', fill= False, linewidth = 1)
#         circle1 = plt.Circle((0, 0), 1.0, color='r', fill= False, linewidth = 10)
        #ref https://stackoverflow.com/questions/9215658/plot-a-circle-with-pyplot
#         circle1 = plt.Circle((0, 0), 1.0, color='r')
         
        ax.add_artist(circle1)

        #ref https://stackoverflow.com/questions/20634170/drawing-obtuse-circular-arc-with-arrowhead-in-matplotlib answered Dec 17 '13 at 14:42
        #Arc(xy, width, height[, angle, theta1, theta2])
#         ellipse = Arc([0,2.5],10,10,0,0,pi,color='green', linewidth='10')
#         ellipse = Arc([0,2.5],5,5,0,0,pi,color='green', linewidth='10')
#         ellipse = Arc([2.5,2.5],5,5,0,0,pi,color='green', linewidth='10')
#         ellipse = Arc([2.5,2.5],1,1,0,0,pi,color='green', linewidth='0.5')
        
#         ax.add_patch(ellipse)

        '''###################
            labels        
        ###################'''

        '''###################
            y values
        ###################'''
        rot = [
            
                [np.cos(index), - np.sin(index)],
                [np.sin(index),   np.cos(index)],
            
            ]
        
        x_ = rot[0][0] * x  - rot[0][1] * y
        y_ = rot[1][0] *  x + rot[1][1] * y
        
        '''###################
            plot        
        ###################'''
        ax.scatter([x_], [y_], s = 40, color = 'b')
#         ax.scatter([x_], [y_], s = 20)
#         plt.scatter([x_], [y_], s = 20)
        
        '''###################
            ops        
        ###################'''
        fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
                    % (dpath_Full, session_Label, tlabel, cnt)
        
        plt_Title = "rot : %.03f pi\n%s" % (index / np.pi, os.path.basename(fpath_Images_Out))
        plt.title(plt_Title)
        
        plt.plot(x, y)
        
        plt.savefig(fpath_Images_Out)
#         #debug
#         plt.show()
        
        cnt += 1

#         #debug
#         print()
#         print("[%s:%d] breaking the loop..." % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#               
#             ), file=sys.stderr)
#         break

        # clear
#         plt.clf()
        
        '''###################
            clear        
        ###################'''
        plt.close(fig)
        
    #/for index in np.arange(0, np.pi * 2, np.pi / 12):

    print()
    print("[%s:%d] image files saved => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , cnt
        ), file=sys.stderr)
    
#/def _test_2__Generate_PNGFiles(dpath_Full):
    
def _test_2__Generate_PNGFiles(dpath_Full, session_Label):
    
    '''###################
        gen        
    ###################'''
        # dirs
    if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)

    '''######################################
        plot        
    ######################################'''
#     '''###################
#         settings        
#     ###################'''
#     plt.xlim(-2 * np.pi,2 * np.pi)
#     plt.ylim(-2,2)
#     plt.grid(b=None, which='major', axis='both')
    
    tlabel = libs.get_TimeLabel_Now()
    
    x = np.linspace(-2 * np.pi, 2 * np.pi, 500)
    
    fig = plt.figure()
    ax  = fig.add_subplot(111)

    
    cnt = 0
    
    for index in np.arange(0, np.pi * 2, np.pi / 12):

        '''###################
            settings        
        ###################'''
        plt.xlim(-2 * np.pi,2 * np.pi)
        plt.ylim(-2,2)
        plt.grid(b=None, which='major', axis='both')

        fig = plt.figure()
        ax  = fig.add_subplot(111)

        ax.grid(b=None, which='major', axis='both')

        '''###################
            labels        
        ###################'''
        tickVal_Y = np.pi / 2
#         tickVal_Y = np.pi
#         tickVal_Y = 1
        
        x_tick = np.arange(-2 * np.pi, 2 * np.pi + tickVal_Y, tickVal_Y)
#         x_tick = np.arange(-2, 2 + tickVal_Y, tickVal_Y)
        
        x_label = [r"$" + format(r / np.pi, ".2g")+ r"\pi$" for r in x_tick]
#         x_label = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]

        ax.set_xticks(x_tick)
        
        ax.set_xticklabels(x_label, fontsize = 10)

        '''###################
            y values
        ###################'''
        y = np.sin(x + index)
        
        '''###################
            ops        
        ###################'''
        fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
                    % (dpath_Full, session_Label, tlabel, cnt)
        
        plt_Title = "sin(x + %03f)" % (index)
        
        plt.title(plt_Title)
        
        plt.plot(x, y)
        
        plt.savefig(fpath_Images_Out)
        
        cnt += 1

        # clear
#         plt.clf()
        
        '''###################
            clear        
        ###################'''
        plt.close(fig)
        
    #/for index in np.arange(0, np.pi * 2, np.pi / 12):

    print()
    print("[%s:%d] image files saved => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , cnt
        ), file=sys.stderr)
    
#/def _test_2__Generate_PNGFiles(dpath_Full):
    
def test_3():
    
    '''###################
        get : paths        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()

    PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT.value
    
    dname_Folder_Data   = "data.27_6_2"
    dname_Images       = "images"
    dname_Images_PNG   = "images_%s" % tlabel
    session_Label      = "6_2-2.test-3"
    
    fps_FFMpeg          = 2
    
    dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = \
                libs_VX7GLZ.get_FFMpeg_Paths \
                (PROJECT_ROOT, 
                 dname_Folder_Data, 
                 dname_Images, 
                 dname_Images_PNG, 
                 session_Label)
    
#     #ref https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
#     msg = "exists" if (os.path.isdir(os.path.dirname(dpath_Full))) else "NOT"
# #     msg = (os.path.isdir(os.path.dirname(dpath_Full)) == True) ? "exists" : "NOT"
#     
#     print()
#     print("[%s:%d] dpath_Full => %s (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , os.path.dirname(dpath_Full), msg
# #         , dpath_Full, msg
#         ), file=sys.stderr)
    
    '''###################
        gen : png files        
    ###################'''
    result = _test_3__Generate_PNGFiles(dpath_Full, session_Label)
    
    '''###################
        video        
    ###################'''
    result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
                    fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)
#     result = libs_VX7GLZ.build_Video_From_PNGFiles__V2(
#                     fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg)
    
    
#/def test_2():

def test_2():
    
    '''###################
        get : paths        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()

    PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT.value
    
    dname_Folder_Data   = "data.27_6_2"
    dname_Images       = "images"
    dname_Images_PNG   = "images_%s" % tlabel
    session_Label      = "6_2-2.test-2"
    
    dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = \
                libs_VX7GLZ.get_FFMpeg_Paths \
                (PROJECT_ROOT, 
                 dname_Folder_Data, 
                 dname_Images, 
                 dname_Images_PNG, 
                 session_Label)
    
#     #ref https://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator
#     msg = "exists" if (os.path.isdir(os.path.dirname(dpath_Full))) else "NOT"
# #     msg = (os.path.isdir(os.path.dirname(dpath_Full)) == True) ? "exists" : "NOT"
#     
#     print()
#     print("[%s:%d] dpath_Full => %s (%s)" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , os.path.dirname(dpath_Full), msg
# #         , dpath_Full, msg
#         ), file=sys.stderr)
    
    '''###################
        gen : png files        
    ###################'''
    result = _test_2__Generate_PNGFiles(dpath_Full, session_Label)
    
    '''###################
        video        
    ###################'''
    result = libs_VX7GLZ.build_Video_From_PNGFiles__V2(
                    fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg)
    
    
#/def test_2():

def test_1():

    '''###################
        plot        
    ###################'''
    x = np.linspace(-3 * np.pi, 3 * np.pi, 1000)
#     x = np.linspace(-3 * np.pi, 3 * np.pi, 100)
    
    y1 = np.sin(x)
    y2 = np.sin(x * 2)
    
    plt.plot(x, y1)
    plt.plot(x, y2)
    
    '''###################
        graph : settings        
    ###################'''
    plt.grid(b=None, which='major', axis='both')
    
#     x_tick = np.arange(-3*np.pi, 3*np.pi, np.pi / 4)
#     
#     x_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]
#     
#     plt.set_xticklabels(x_label2, fontsize = 10)
    
    plt.show()
    
#     return
    
    '''###################
        build : paths        
    ###################'''
#     dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = get_FFMpeg_Paths()
    
#     #debug
#     print()
#     print("[%s:%d] dpath_Full => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , dpath_Full
#             ), file=sys.stderr)
#     
#     print("[%s:%d] fpath_Glob => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , fpath_Glob
#             ), file=sys.stderr)
#     
#     print("[%s:%d] fpath_In_FFMpeg => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , fpath_In_FFMpeg
#             ), file=sys.stderr)
#     
# #     return
#     '''###################
#         file path        
#     ###################'''
#     PROJECT_ROOT = cons_27_6_1.FPath.PROJECT_ROOT.value
# #     PROJECT_ROOT = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\1_\\_17"
#     
#     dname_Folder_Data = "data.27_6_1"
#     
#     dpath_Out = "%s\\%s" % (PROJECT_ROOT, dname_Folder_Data)
# #     dpath_Out = "%s\\data.27_6_1" % (PROJECT_ROOT)
#     
#     ### fpath full
#     tlabel = libs.get_TimeLabel_Now()
#     
#     session_Label = "6_1.test-1"
#     
#     fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)
# 
#     dname_Images = "images"
#     
#     dname_Images_PNG = "images_20180220_140223"
# #     dname_Images_PNG = "images_20180220_141101"
#     
# #     dpath_Full = "%s\\images_20180220_141141" % (dpath_Out)
#     dpath_Full = "%s\\%s\\%s" % (dpath_Out, dname_Images, dname_Images_PNG)
# #     dpath_Full = "%s\\%s\\images_20180220_141141" % (dpath_Out, dname_Images)
#     
#     fpath_Glob = "%s\\*(*).png" % (dpath_Full)
#     
#     dpath_In = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research" \
#             + "\\28_Physics\\1_\\_17\\data_1_17.1" \
#             + "\\images\\%s" % (dname_Images_PNG)
# #             + "\\images\\images_20180220_141141"
#             
#     fpath_In_FFMpeg = "%s\\image.%%03d.png" % (dpath_In)
# #     fpath_In = "%s\\image.%03d.png" % (dpath_In)
#     
#     fpath_Out_FFMpeg = "%s\\movie.%s.mp4" % (dpath_In, libs.get_TimeLabel_Now())
    
    '''###################
        build : video        
    ###################'''
#     libs_VX7GLZ.build_Video_From_PNGFiles \
#         (dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg)
    
#/def test_4():


def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_3()
#     test_2()
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



