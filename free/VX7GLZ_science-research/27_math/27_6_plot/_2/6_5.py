# -*- coding: utf-8 -*-
'''
file : \free\VX7GLZ_science-research\27_math\27_6_plot\_2\6_5.py
orig : \free\VX7GLZ_science-research\27_math\27_6_plot\_2\6_2.py
at : 2018/02/25 12:58:59

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_2\
python 6_5.py

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
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1')

from libs_VX7GLZ import libs_VX7GLZ
from libs_27_6_1 import cons_27_6_1
from libs_27_6_2 import cons_27_6_2

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
from sympy.matrices import *

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random, glob
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.patches as mpatches, matplotlib.cm as cm
from shutil import copyfile
from scipy.stats.stats import pearsonr
from matplotlib.patches import Ellipse, Arc
from math import pi

###############################################
def _test_2__Generate_PNGFiles \
(dpath_Full, session_Label, 
set_Pow, id_Dir, 
start_Coord=(np.cos(pi / 4 * 0), np.sin(pi / 4 * 0)),
_numOf_TickDivision = 24
):
# def _test_2__Generate_PNGFiles(dpath_Full, session_Label):
    
#     #debug
#     print()
#     print("[%s:%d] set_Pow => \n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , set_Pow
#         ), file=sys.stderr)
#     
#     return
    
    '''###################
        gen : directory        
    ###################'''
        # dirs
#     dpath_Full_Each = "%s\\%s.(%02d)(%s)" \
#     dpath_Full_Each = "%s\\%s.(%02d)(pow_%s)" \

    dpath_Full_Each = dpath_Full
#     dpath_Full_Each = "%s\\%s.(%02d)(pow.%s)" \
#                 % (
#                     dpath_Full
#                     , os.path.basename(dpath_Full)
#                     , id_Dir
#                     , "-".join([str(x) for x in set_Pow])
#                 )
                
#     dpath_Full_Each = "%s\\%s.(%02d)" \
#                 % (dpath_Full, os.path.basename(dpath_Full), id_Dir)
    
    if not os.path.isdir(dpath_Full_Each) : os.makedirs(dpath_Full_Each)
#     if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)

    print()
    print("[%s:%d] dpath_Full_Each => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Full_Each
        ), file=sys.stderr)

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
    lim_X_Start = -3
    lim_X_End = 7
#     lim_X_Start = -5
#     lim_X_End = 5
    lim_Y_Start = -3
    lim_Y_End = 3
#     lim_Y_Start = -5
#     lim_Y_End = 5
    
#     numOf_TickDivision = 24  # used in : tick_Rotate
#     numOf_TickDivision = 4  # used in : tick_Rotate
    numOf_TickDivision = _numOf_TickDivision  # used in : tick_Rotate
    
    val_StartingPoint_Multiplier = 1    # used in : x, y
    
    val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11 = \
            (1.0, 1.0, 1.0, 1.0)
#             (2.0, 3.0, 4.0, 1.0)
#             (3.0, 4.0, 1.0, 2.0)
#             (4.0, 1.0, 2.0, 3.0)
#             (1.0, 2.0, 3.0, 4.0)
#             (1.0, 2.0, 1.0, 3.0)
#             (2.0, 1.0, 1.0, 3.0)
#             (2.0, 1.0, 3.0, 1.0)
    
    val_Scalar_Max = max((val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11))
    
    # cos and sin signs
    pow_a00, pow_a01, pow_a10, pow_a11 = set_Pow
#     pow_a00, pow_a01, pow_a10, pow_a11 = \
#                         (1, 1, 1, 2)
#                         (1, 1, 2, 1)
#                         (1, 2, 1, 1)
#                         (2, 1, 1, 1)
                        
    # cos and sin signs
    rot_a00, rot_a01, rot_a10, rot_a11 = \
                        (1., -1., 1., 1.)
#                         (1., 1., -1., 1)
#                         (1., 1., 1., 1)
#                         (1., 1., 1., -1)
#                         (-1., 1., 1., 1)
    
#     tick_Rotate = np.pi / 4
#     tick_Rotate = np.pi / 12
    tick_Rotate = np.pi / numOf_TickDivision
#     tick_Rotate = np.pi / 24
    
    cnt = 0
    
    '''###################
        starting point        
    ###################'''
#     x = 1; y = 1
#     x = np.cos(pi / 2); y = np.sin(pi / 2)
#     x = np.cos(pi / 4); y = np.sin(pi / 4)
#     x, y = np.cos(pi / 4 * (-3)), np.sin(pi / 4 * (-3))
#     x, y = np.cos(pi / 4 * 3), np.sin(pi / 4 * 3)
    x, y = start_Coord
#     x, y = np.cos(pi / 4 * val_StartingPoint_Multiplier) \
#             , np.sin(pi / 4 * val_StartingPoint_Multiplier)   #
#     x, y = np.cos(pi / 4 * 1), np.sin(pi / 4 * 1)   # 45'
#     x, y = np.cos(pi / 4 * 2), np.sin(pi / 4 * 2)
#     x = np.cos(pi / 4 * 0); y = np.sin(pi / 4 * 0)  # (1, 0)
#     x = np.cos(pi / 4 * 3); y = np.sin(pi / 4 * 3)
#     x = 1; y = 0
    
    xs_ = []
    ys_ = []
    
    range_Base = np.arange(0, np.pi * 2, tick_Rotate)
    
    '''###################
        loop : i : rotate : x^2 + y^2 = 1        
    ###################'''
    for i in range_Base :
#     for i in np.arange(0, np.pi * 2, tick_Rotate) :
 
#         '''###################
#             settings        
#         ###################'''
# #             plt.grid(b=None, which='major', axis='both')
#  
#         fig = plt.figure()
#          
#         #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
#         fig.set_facecolor("#fff9c9")
#          
#         #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
#         fig.set_size_inches(18.5, 10.5)
#          
#          
#         ax  = fig.add_subplot(111)
#  
#         #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
#         ax.set_facecolor("honeydew") # 
#          
#         ax.grid(b=None, which='major', axis='both')
#          
#         #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
#         ax.set_aspect('equal')
#  
#         #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
#          
#         ax.set_xlim(lim_X_Start, lim_X_End)
#         ax.set_ylim(lim_Y_Start, lim_Y_End)
#          
#         '''###################
#             label : y
#         ###################'''
#         #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
#         tickVal_Y = 1
#         tickVal_X = 1
#          
#         # y ax
#         y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
#         ax.set_yticks(y_tick)
#         ax.set_yticklabels(y_tick, fontsize = 15)
# #         ax.set_yticklabels(y_tick, fontsize = 10)
#  
#         # x ax
#         x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
#         ax.set_xticks(x_tick)
#         ax.set_xticklabels(x_tick, fontsize = 15)
# #         ax.set_xticklabels(x_tick, fontsize = 10)
 
        '''###################
            rotate
        ###################'''
#         rot_a00, rot_a01, rot_a10, rot_a11 = (1., -1., 1., 1.)
#         rot_a00 =  1
#         rot_a01 = -1
#         rot_a10 =  1
#         rot_a11 =  1
         
        rot = [
             
#                 [np.cos(i) * rot_a00, np.sin(i) * rot_a01],
#                 [np.sin(i) * rot_a10, np.cos(i) * rot_a11],
#                 [np.cos(i), - np.sin(i)],
#                 [np.sin(i),   np.cos(i)],
#                 [np.cos(i) * val_Scalar_a00, - np.sin(i) * val_Scalar_a01],
#                 [np.sin(i) * val_Scalar_a10,   np.cos(i) * val_Scalar_a11],
            [
                (np.cos(i) ** pow_a00) * val_Scalar_a00 * rot_a00
                , (np.sin(i) ** pow_a01) * val_Scalar_a01 * rot_a01
             ],
            [
                (np.sin(i) ** pow_a10) * val_Scalar_a10 * rot_a10
                , (np.cos(i) ** pow_a11) * val_Scalar_a11 * rot_a11
             ],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
             
            ]
         
        x2 = rot[0][0] * x + rot[0][1] * y
        y2 = rot[1][0] * x + rot[1][1] * y
 
        # append
        xs_.append(x2)
        ys_.append(y2)
 
    '''###################
        settings        
    ###################'''
    #             plt.grid(b=None, which='major', axis='both')
    
    fig = plt.figure()
     
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    fig.set_facecolor("#fff9c9")
     
    #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
    fig.set_size_inches(18.5, 10.5)
     
     
    ax  = fig.add_subplot(111)
    
    #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
    ax.set_facecolor("honeydew") # 
     
    ax.grid(b=None, which='major', axis='both')
     
    #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
    ax.set_aspect('equal')
    
    #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
     
    ax.set_xlim(lim_X_Start, lim_X_End)
    ax.set_ylim(lim_Y_Start, lim_Y_End)
     
    '''###################
        label : y
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_Y = 1
    tickVal_X = 1
     
    # y ax
    y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_tick, fontsize = 15)
    #         ax.set_yticklabels(y_tick, fontsize = 10)
    
    # x ax
    x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
    ax.set_xticks(x_tick)
    ax.set_xticklabels(x_tick, fontsize = 15)
    #         ax.set_xticklabels(x_tick, fontsize = 10)
 
    '''###################
        circle        
    ###################'''
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    #ref alpha https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html
    circle1 = plt.Circle(
                (0, 0)
                , 1.0
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    c2 = plt.Circle(
                (0, 0)
                , val_Scalar_Max
    #                     , val_Scalar_a01
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    ax.add_artist(circle1)
    ax.add_artist(c2)
    
     
    '''###################
        plot        
    ###################'''
    col_Series = "#00ff%02x" % (int(255 / numOf_TickDivision * cnt))
    
    #ref https://stackoverflow.com/questions/17682216/scatter-plot-and-color-mapping-in-python answered Jul 16 '13 at 16:45
    ax.plot(range_Base, xs_, range_Base, ys_, linewidth = 5)
    
#     ax.plot(xs_, ys_, linewidth = 20)
    ax.scatter(xs_, ys_, s = 20, c = range(0, len(xs_)), cmap='viridis')
#     ax.scatter([x2], [y2], s = 30, color = 'gray')

    # distance from the origin
    xs_2 = [i**2 for i in xs_]
    ys_2 = [i**2 for i in ys_]
    
    sum_xs_ys = [a + b for a, b in list(zip(xs_2, ys_2))]
    
    ax.plot(range_Base, sum_xs_ys, linewidth = 5, c = 'g')
    
    
    '''###################
        ops        
    ###################'''
    '''###################
        labels : title
    ###################'''
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n%s" \
    fpath_Images_Out = "%s\\%s.%s.(pow.%s).png" \
        % (dpath_Full_Each, session_Label, tlabel, "-".join([str(x) for x in set_Pow]))
#     fpath_Images_Out = "%s\\%s.%s.png" \
#         % (dpath_Full_Each, session_Label, tlabel)

#     fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
#         % (dpath_Full_Each, session_Label, tlabel, cnt)
    #             % (dpath_Full, session_Label, tlabel, cnt)
    
    #         str_Title = "[rot] %.03f pi / [point] (%.2f pi, %.2f pi)\n" \
    str_Title = "[rot] %.02f pi / [point] (%.2f pi, %.2f pi)\n" \
                + "[abcd] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #         str_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
    #                     + "%s" \
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n%s" \
    plt_Title = str_Title \
            % (
    #                     index / np.pi
                i / np.pi
                , x / np.pi, y / np.pi
#                 , x2 / np.pi, y2 / np.pi
                , val_Scalar_a00
                , val_Scalar_a01
                , val_Scalar_a10
                , val_Scalar_a11
    #                     , os.path.basename(fpath_Images_Out)
               )
             
    #         ax.set_title(plt_Title)
    plt.title(plt_Title, fontsize = 15)
    #         plt.title(plt_Title)
    
    '''###################
        labels : x label
    ###################'''
    str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
                + "[pow] 00 : %.1f / 01 : %.1f / 10 : %.1f / 11 : %.1f\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
    #         str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_XLabel = str_XLabel \
            % (
                  rot_a00
                , rot_a01
                , rot_a10
                , rot_a11
                 
                , pow_a00
                , pow_a01
                , pow_a10
                , pow_a11
                 
               )
             
    ax.set_xlabel(plt_XLabel, fontsize = 15)
    #         ax.set_xlabel(plt_XLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        labels : y label
    ###################'''
    str_YLabel = "[file] %s"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_YLabel = str_YLabel \
            % (
                  os.path.basename(fpath_Images_Out)
                 
               )
             
    ax.set_ylabel(plt_YLabel, fontsize = 15)
    #         ax.set_ylabel(plt_YLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        plot, save image        
    ###################'''
    #         plt.plot(x, y)
     
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

    #/for i in np.arange(0, np.pi * 2, tick_Rotate) :
    
    '''###################
        return        
    ###################'''
    return dpath_Full_Each

'''###################
    test_2()        
###################'''
def test_2():
    
    '''###################
        get : paths        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()

    PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT_27_6_5.value
#     PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT.value
    
    dname_Folder_Data   = "data.27_6_5"
    dname_Images       = "images"
    dname_Images_PNG   = "images_%s" % tlabel
    session_Label      = "6_5.test_2"
    
    fps_FFMpeg          = 6 # 4 frames per second
#     fps_FFMpeg          = 2
    
    _numOf_TickDivision = 24
    
    
    dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = \
                libs_VX7GLZ.get_FFMpeg_Paths \
                (PROJECT_ROOT, 
                 dname_Folder_Data, 
                 dname_Images, 
                 dname_Images_PNG, 
                 session_Label)
    
    # cos and sin signs
    cons_Pow = 3.5
    
    num_Base    = 1
    num_Pick   = 60  # pow --> 
#     num_Pick   = 30  # pow --> 
#     num_Pick   = 10  # pow --> 
#     num_Pick   = 5  # pow --> 5
#     num_Pick   = 4  # pow --> 4
#     num_Pick   = 3  # pow --> 3
#     num_Pick   = 2
    lenOf_List = 4
    
    '''###################
        pow        
    ###################'''
    tick_Pow = 0.1
    
    lo_Pows = np.arange(num_Base, num_Pick + 1)
#     lo_Pows = np.arange(num_Base, num_Pick + 1, tick_Pow)
    
    lenOf_PowSets = len(lo_Pows)
#     lenOf_PowSets = 10
    
#     L1 = [num_Base] * 9
    L1 = [num_Base] * lenOf_PowSets
#     L1 = [1] * 9
    
#     lo_Pows = np.linspace(1, 1.9, 9)
#     tick_Pow = 0.1

#     lo_Pows = np.linspace(num_Base, num_Pick + 1, tick_Pow)
#     lo_Pows = np.arange(num_Base, num_Pick + 1, tick_Pow)
#     lo_Pows = np.arange(num_Base, num_Pick, 0.1)
#     lo_Pows = np.arange(num_Base, num_Pick, 0.1)
    
#     lo_Pow = list(zip(lo_Pows, lo_Pows, L1, L1))
    lo_Pow = list(zip(lo_Pows, lo_Pows, lo_Pows, L1))
#     lo_Pow = list(zip(L1, lo_Pows, lo_Pows, L1))
#     lo_Pow = list(zip(L1, lo_Pows, L1, lo_Pows))
#     lo_Pow = list(zip(lo_Pows, lo_Pows, lo_Pows, lo_Pows))
#     lo_Pow = list(zip([round(x, 1) for x in lo_Pows], L1, L1, L1))
#     lo_Pow = list(zip(lo_Pows, L1, L1, L1))
    
#     print()
#     print("[%s:%d] lo_Pow =>\n" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              
#             ), file=sys.stderr)
#      
#     for item in lo_Pow : print(item)
#      
# #     lo_Pow = 
#      
#      
#     return

#     lo_Pow = libs_VX7GLZ.get_Combi_ALL(num_Base, num_Pick, lenOf_List)

#     print()
#     print("[%s:%d] lo_Pow =>\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , tuple(lo_Pow)
# #         , lo_Pow
#         ), file=sys.stderr)
#      
#     return

#     lo_Pow = (
#                   (cons_Pow, cons_Pow, 1, 1)
#                 , (cons_Pow, 1, cons_Pow, 1)
#                 , (cons_Pow, 1, 1, cons_Pow)
#                 , (1, cons_Pow, cons_Pow, 1)
#                 , (1, cons_Pow, 1, cons_Pow)
#                 , (1, 1, cons_Pow, cons_Pow)
#                   (3, 3, 1, 1)
#                 , (3, 1, 3, 1)
#                 , (3, 1, 1, 3)
#                 , (1, 3, 3, 1)
#                 , (1, 3, 1, 3)
#                 , (1, 1, 3, 3)
#                   (2, 2, 1, 1)
#                 , (2, 1, 2, 1)
#                 , (2, 1, 1, 2)
#                 , (1, 2, 2, 1)
#                 , (1, 2, 1, 2)
#                 , (1, 1, 2, 2)
#                 (1, 1, 1, 1)
#                 , (2, 1, 1, 1)
#                 , (1, 2, 1, 1)
#                 , (1, 1, 2, 1)
#                 , (1, 1, 1, 2)
#           )

    # id dir
    id_Dir = 0

    '''###################
        set : starting point        
    ###################'''
    val_StartingPoint_Multiplier = 1
#     val_StartingPoint_Multiplier = 3
#     val_StartingPoint_Multiplier = 2
#     val_StartingPoint_Multiplier = 5
    
#     val_StartingPoint_PiDivisor = 3
    val_StartingPoint_PiDivisor = 4
#     val_StartingPoint_PiDivisor = 9
#     val_StartingPoint_PiDivisor = 12
    
    start_Coord = (
#             0
#             , 0)
            np.cos(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier)
            , np.sin(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier))

    print()
    print("[%s:%d] start_Coord => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , start_Coord
        ), file=sys.stderr)

    '''###################
        dpath_Full : modify        
    ###################'''
#     dpath_Full = dpath_Full + "." + "pow.(start_%.2fpi,%.2fpi)" \
#     dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)" \

    dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%d,pick-%d)" \
                % (val_StartingPoint_Multiplier, 
                   val_StartingPoint_PiDivisor
                   , num_Base, num_Pick
                   )
                
#                 % (start_Coord[0], start_Coord[1])
#     dpath_Full = dpath_Full + "." + "pow.start_-1,0"
    

    for set_Pow in lo_Pow :
        
#         '''###################
#             dpath_Full : modify        
#         ###################'''
# #         dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%d,pick-%d)" \
# #         dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%.1f,pick-%.1f)" \
#         dpath_Full_tmp = dpath_Full + "." + "pow.(%d-%d.pi)(base-%.1f,pick-%.1f)" \
#             % (val_StartingPoint_Multiplier, 
#                val_StartingPoint_PiDivisor
#                , num_Base
#                , tuple(set_Pow)[0]
# #                , num_Pick
#                )

        '''###################
            gen : png files        
        ###################'''

#                     (dpath_Full_tmp
        dpath_Full_Each = _test_2__Generate_PNGFiles \
                    (dpath_Full
                     , session_Label
                     , tuple(set_Pow)
#                      , set_Pow
                     , id_Dir
                     , start_Coord
                     , _numOf_TickDivision)
#                     (dpath_Full, session_Label, set_Pow, id_Dir)

        '''###################
            path : modify        
        ###################'''
        fpath_Out_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Out_FFMpeg)

        fpath_In_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_In_FFMpeg)

        fpath_Glob = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Glob)

        '''###################
            video        
        ###################'''
#         result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                         fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)

        '''###################
            increment        
        ###################'''
        id_Dir += 1

    #/for set_Pow in lo_Pow :    
    
    '''###################
        video        
    ###################'''
#     result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                     fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)
    
    
#/def test_7_4():


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
    
#     plt.show()
    
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

def _test_1_2__Generate_PNGFiles \
(dpath_Full, session_Label, 
set_Pow, id_Dir, 
start_Coord=(np.cos(pi / 4 * 0), np.sin(pi / 4 * 0)),
_numOf_TickDivision = 24
):
# def _test_1_2__Generate_PNGFiles(dpath_Full, session_Label):
    
#     #debug
#     print()
#     print("[%s:%d] set_Pow => \n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , set_Pow
#         ), file=sys.stderr)
#     
#     return
    
    '''###################
        gen : directory        
    ###################'''
        # dirs
#     dpath_Full_Each = "%s\\%s.(%02d)(%s)" \
#     dpath_Full_Each = "%s\\%s.(%02d)(pow_%s)" \

    dpath_Full_Each = dpath_Full
#     dpath_Full_Each = "%s\\%s.(%02d)(pow.%s)" \
#                 % (
#                     dpath_Full
#                     , os.path.basename(dpath_Full)
#                     , id_Dir
#                     , "-".join([str(x) for x in set_Pow])
#                 )
                
#     dpath_Full_Each = "%s\\%s.(%02d)" \
#                 % (dpath_Full, os.path.basename(dpath_Full), id_Dir)
    
    if not os.path.isdir(dpath_Full_Each) : os.makedirs(dpath_Full_Each)
#     if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)

    print()
    print("[%s:%d] dpath_Full_Each => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Full_Each
        ), file=sys.stderr)

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
    
#     numOf_TickDivision = 24  # used in : tick_Rotate
#     numOf_TickDivision = 4  # used in : tick_Rotate
    numOf_TickDivision = _numOf_TickDivision  # used in : tick_Rotate
    
    val_StartingPoint_Multiplier = 1    # used in : x, y
    
    val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11 = \
            (1.0, 1.0, 1.0, 1.0)
#             (2.0, 3.0, 4.0, 1.0)
#             (3.0, 4.0, 1.0, 2.0)
#             (4.0, 1.0, 2.0, 3.0)
#             (1.0, 2.0, 3.0, 4.0)
#             (1.0, 2.0, 1.0, 3.0)
#             (2.0, 1.0, 1.0, 3.0)
#             (2.0, 1.0, 3.0, 1.0)
    
    val_Scalar_Max = max((val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11))
    
    # cos and sin signs
    pow_a00, pow_a01, pow_a10, pow_a11 = set_Pow
#     pow_a00, pow_a01, pow_a10, pow_a11 = \
#                         (1, 1, 1, 2)
#                         (1, 1, 2, 1)
#                         (1, 2, 1, 1)
#                         (2, 1, 1, 1)
                        
    # cos and sin signs
    rot_a00, rot_a01, rot_a10, rot_a11 = \
                        (1., -1., 1., 1.)
#                         (1., 1., -1., 1)
#                         (1., 1., 1., 1)
#                         (1., 1., 1., -1)
#                         (-1., 1., 1., 1)
    
#     tick_Rotate = np.pi / 4
#     tick_Rotate = np.pi / 12
    tick_Rotate = np.pi / numOf_TickDivision
#     tick_Rotate = np.pi / 24
    
    cnt = 0
    
    '''###################
        starting point        
    ###################'''
#     x = 1; y = 1
#     x = np.cos(pi / 2); y = np.sin(pi / 2)
#     x = np.cos(pi / 4); y = np.sin(pi / 4)
#     x, y = np.cos(pi / 4 * (-3)), np.sin(pi / 4 * (-3))
#     x, y = np.cos(pi / 4 * 3), np.sin(pi / 4 * 3)
    x, y = start_Coord
#     x, y = np.cos(pi / 4 * val_StartingPoint_Multiplier) \
#             , np.sin(pi / 4 * val_StartingPoint_Multiplier)   #
#     x, y = np.cos(pi / 4 * 1), np.sin(pi / 4 * 1)   # 45'
#     x, y = np.cos(pi / 4 * 2), np.sin(pi / 4 * 2)
#     x = np.cos(pi / 4 * 0); y = np.sin(pi / 4 * 0)  # (1, 0)
#     x = np.cos(pi / 4 * 3); y = np.sin(pi / 4 * 3)
#     x = 1; y = 0
    
    xs_ = []
    ys_ = []
    
    '''###################
        loop : i : rotate : x^2 + y^2 = 1        
    ###################'''
    for i in np.arange(0, np.pi * 2, tick_Rotate) :
 
#         '''###################
#             settings        
#         ###################'''
# #             plt.grid(b=None, which='major', axis='both')
#  
#         fig = plt.figure()
#          
#         #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
#         fig.set_facecolor("#fff9c9")
#          
#         #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
#         fig.set_size_inches(18.5, 10.5)
#          
#          
#         ax  = fig.add_subplot(111)
#  
#         #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
#         ax.set_facecolor("honeydew") # 
#          
#         ax.grid(b=None, which='major', axis='both')
#          
#         #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
#         ax.set_aspect('equal')
#  
#         #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
#          
#         ax.set_xlim(lim_X_Start, lim_X_End)
#         ax.set_ylim(lim_Y_Start, lim_Y_End)
#          
#         '''###################
#             label : y
#         ###################'''
#         #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
#         tickVal_Y = 1
#         tickVal_X = 1
#          
#         # y ax
#         y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
#         ax.set_yticks(y_tick)
#         ax.set_yticklabels(y_tick, fontsize = 15)
# #         ax.set_yticklabels(y_tick, fontsize = 10)
#  
#         # x ax
#         x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
#         ax.set_xticks(x_tick)
#         ax.set_xticklabels(x_tick, fontsize = 15)
# #         ax.set_xticklabels(x_tick, fontsize = 10)
 
        '''###################
            rotate
        ###################'''
#         rot_a00, rot_a01, rot_a10, rot_a11 = (1., -1., 1., 1.)
#         rot_a00 =  1
#         rot_a01 = -1
#         rot_a10 =  1
#         rot_a11 =  1
         
        rot = [
             
#                 [np.cos(i) * rot_a00, np.sin(i) * rot_a01],
#                 [np.sin(i) * rot_a10, np.cos(i) * rot_a11],
#                 [np.cos(i), - np.sin(i)],
#                 [np.sin(i),   np.cos(i)],
#                 [np.cos(i) * val_Scalar_a00, - np.sin(i) * val_Scalar_a01],
#                 [np.sin(i) * val_Scalar_a10,   np.cos(i) * val_Scalar_a11],
            [
                (np.cos(i) ** pow_a00) * val_Scalar_a00 * rot_a00
                , (np.sin(i) ** pow_a01) * val_Scalar_a01 * rot_a01
             ],
            [
                (np.sin(i) ** pow_a10) * val_Scalar_a10 * rot_a10
                , (np.cos(i) ** pow_a11) * val_Scalar_a11 * rot_a11
             ],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
             
            ]
         
        x2 = rot[0][0] * x + rot[0][1] * y
        y2 = rot[1][0] * x + rot[1][1] * y
 
        # append
        xs_.append(x2)
        ys_.append(y2)
 
    '''###################
        settings        
    ###################'''
    #             plt.grid(b=None, which='major', axis='both')
    
    fig = plt.figure()
     
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    fig.set_facecolor("#fff9c9")
     
    #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
    fig.set_size_inches(18.5, 10.5)
     
     
    ax  = fig.add_subplot(111)
    
    #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
    ax.set_facecolor("honeydew") # 
     
    ax.grid(b=None, which='major', axis='both')
     
    #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
    ax.set_aspect('equal')
    
    #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
     
    ax.set_xlim(lim_X_Start, lim_X_End)
    ax.set_ylim(lim_Y_Start, lim_Y_End)
     
    '''###################
        label : y
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_Y = 1
    tickVal_X = 1
     
    # y ax
    y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_tick, fontsize = 15)
    #         ax.set_yticklabels(y_tick, fontsize = 10)
    
    # x ax
    x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
    ax.set_xticks(x_tick)
    ax.set_xticklabels(x_tick, fontsize = 15)
    #         ax.set_xticklabels(x_tick, fontsize = 10)
 
    '''###################
        circle        
    ###################'''
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    #ref alpha https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html
    circle1 = plt.Circle(
                (0, 0)
                , 1.0
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    c2 = plt.Circle(
                (0, 0)
                , val_Scalar_Max
    #                     , val_Scalar_a01
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    ax.add_artist(circle1)
    ax.add_artist(c2)
    
     
    '''###################
        plot        
    ###################'''
    col_Series = "#00ff%02x" % (int(255 / numOf_TickDivision * cnt))
    
    #ref https://stackoverflow.com/questions/17682216/scatter-plot-and-color-mapping-in-python answered Jul 16 '13 at 16:45
    ax.scatter(xs_, ys_, s = 20, c = range(0, len(xs_)), cmap='viridis')
#     ax.scatter([x2], [y2], s = 30, color = 'gray')

    '''###################
        ops        
    ###################'''
    '''###################
        labels : title
    ###################'''
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n%s" \
    fpath_Images_Out = "%s\\%s.%s.(pow.%s).png" \
        % (dpath_Full_Each, session_Label, tlabel, "-".join([str(x) for x in set_Pow]))
#     fpath_Images_Out = "%s\\%s.%s.png" \
#         % (dpath_Full_Each, session_Label, tlabel)

#     fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
#         % (dpath_Full_Each, session_Label, tlabel, cnt)
    #             % (dpath_Full, session_Label, tlabel, cnt)
    
    #         str_Title = "[rot] %.03f pi / [point] (%.2f pi, %.2f pi)\n" \
    str_Title = "[rot] %.02f pi / [point] (%.2f pi, %.2f pi)\n" \
                + "[abcd] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #         str_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
    #                     + "%s" \
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n%s" \
    plt_Title = str_Title \
            % (
    #                     index / np.pi
                i / np.pi
                , x / np.pi, y / np.pi
#                 , x2 / np.pi, y2 / np.pi
                , val_Scalar_a00
                , val_Scalar_a01
                , val_Scalar_a10
                , val_Scalar_a11
    #                     , os.path.basename(fpath_Images_Out)
               )
             
    #         ax.set_title(plt_Title)
    plt.title(plt_Title, fontsize = 15)
    #         plt.title(plt_Title)
    
    '''###################
        labels : x label
    ###################'''
    str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
                + "[pow] 00 : %.1f / 01 : %.1f / 10 : %.1f / 11 : %.1f\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
    #         str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_XLabel = str_XLabel \
            % (
                  rot_a00
                , rot_a01
                , rot_a10
                , rot_a11
                 
                , pow_a00
                , pow_a01
                , pow_a10
                , pow_a11
                 
               )
             
    ax.set_xlabel(plt_XLabel, fontsize = 15)
    #         ax.set_xlabel(plt_XLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        labels : y label
    ###################'''
    str_YLabel = "[file] %s"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_YLabel = str_YLabel \
            % (
                  os.path.basename(fpath_Images_Out)
                 
               )
             
    ax.set_ylabel(plt_YLabel, fontsize = 15)
    #         ax.set_ylabel(plt_YLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        plot, save image        
    ###################'''
    #         plt.plot(x, y)
     
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

    #/for i in np.arange(0, np.pi * 2, tick_Rotate) :
    
    '''###################
        return        
    ###################'''
    return dpath_Full_Each

'''###################
    test_1_2()        
###################'''
def test_1_2():
    
    '''###################
        get : paths        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()

    PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT_27_6_5.value
#     PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT.value
    
    dname_Folder_Data   = "data.27_6_5"
    dname_Images       = "images"
    dname_Images_PNG   = "images_%s" % tlabel
    session_Label      = "6_5.test_1_2"
    
    fps_FFMpeg          = 6 # 4 frames per second
#     fps_FFMpeg          = 2
    
    _numOf_TickDivision = 24
    
    
    dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = \
                libs_VX7GLZ.get_FFMpeg_Paths \
                (PROJECT_ROOT, 
                 dname_Folder_Data, 
                 dname_Images, 
                 dname_Images_PNG, 
                 session_Label)
    
    # cos and sin signs
    cons_Pow = 3.5
    
    num_Base    = 1
    num_Pick   = 60  # pow --> 
#     num_Pick   = 30  # pow --> 
#     num_Pick   = 10  # pow --> 
#     num_Pick   = 5  # pow --> 5
#     num_Pick   = 4  # pow --> 4
#     num_Pick   = 3  # pow --> 3
#     num_Pick   = 2
    lenOf_List = 4
    
    '''###################
        pow        
    ###################'''
    tick_Pow = 0.1
    
    lo_Pows = np.arange(num_Base, num_Pick + 1)
#     lo_Pows = np.arange(num_Base, num_Pick + 1, tick_Pow)
    
    lenOf_PowSets = len(lo_Pows)
#     lenOf_PowSets = 10
    
#     L1 = [num_Base] * 9
    L1 = [num_Base] * lenOf_PowSets
#     L1 = [1] * 9
    
#     lo_Pows = np.linspace(1, 1.9, 9)
#     tick_Pow = 0.1

#     lo_Pows = np.linspace(num_Base, num_Pick + 1, tick_Pow)
#     lo_Pows = np.arange(num_Base, num_Pick + 1, tick_Pow)
#     lo_Pows = np.arange(num_Base, num_Pick, 0.1)
#     lo_Pows = np.arange(num_Base, num_Pick, 0.1)
    
    lo_Pow = list(zip(lo_Pows, lo_Pows, L1, L1))
#     lo_Pow = list(zip(L1, lo_Pows, L1, lo_Pows))
#     lo_Pow = list(zip(lo_Pows, lo_Pows, lo_Pows, lo_Pows))
#     lo_Pow = list(zip([round(x, 1) for x in lo_Pows], L1, L1, L1))
#     lo_Pow = list(zip(lo_Pows, L1, L1, L1))
    
#     print()
#     print("[%s:%d] lo_Pow =>\n" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#              
#             ), file=sys.stderr)
#      
#     for item in lo_Pow : print(item)
#      
# #     lo_Pow = 
#      
#      
#     return

#     lo_Pow = libs_VX7GLZ.get_Combi_ALL(num_Base, num_Pick, lenOf_List)

#     print()
#     print("[%s:%d] lo_Pow =>\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , tuple(lo_Pow)
# #         , lo_Pow
#         ), file=sys.stderr)
#      
#     return

#     lo_Pow = (
#                   (cons_Pow, cons_Pow, 1, 1)
#                 , (cons_Pow, 1, cons_Pow, 1)
#                 , (cons_Pow, 1, 1, cons_Pow)
#                 , (1, cons_Pow, cons_Pow, 1)
#                 , (1, cons_Pow, 1, cons_Pow)
#                 , (1, 1, cons_Pow, cons_Pow)
#                   (3, 3, 1, 1)
#                 , (3, 1, 3, 1)
#                 , (3, 1, 1, 3)
#                 , (1, 3, 3, 1)
#                 , (1, 3, 1, 3)
#                 , (1, 1, 3, 3)
#                   (2, 2, 1, 1)
#                 , (2, 1, 2, 1)
#                 , (2, 1, 1, 2)
#                 , (1, 2, 2, 1)
#                 , (1, 2, 1, 2)
#                 , (1, 1, 2, 2)
#                 (1, 1, 1, 1)
#                 , (2, 1, 1, 1)
#                 , (1, 2, 1, 1)
#                 , (1, 1, 2, 1)
#                 , (1, 1, 1, 2)
#           )

    # id dir
    id_Dir = 0

    '''###################
        set : starting point        
    ###################'''
    val_StartingPoint_Multiplier = 1
#     val_StartingPoint_Multiplier = 3
#     val_StartingPoint_Multiplier = 2
#     val_StartingPoint_Multiplier = 5
    
#     val_StartingPoint_PiDivisor = 3
    val_StartingPoint_PiDivisor = 4
#     val_StartingPoint_PiDivisor = 9
#     val_StartingPoint_PiDivisor = 12
    
    start_Coord = (
#             0
#             , 0)
            np.cos(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier)
            , np.sin(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier))

    print()
    print("[%s:%d] start_Coord => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , start_Coord
        ), file=sys.stderr)

    '''###################
        dpath_Full : modify        
    ###################'''
#     dpath_Full = dpath_Full + "." + "pow.(start_%.2fpi,%.2fpi)" \
#     dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)" \

    dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%d,pick-%d)" \
                % (val_StartingPoint_Multiplier, 
                   val_StartingPoint_PiDivisor
                   , num_Base, num_Pick
                   )
                
#                 % (start_Coord[0], start_Coord[1])
#     dpath_Full = dpath_Full + "." + "pow.start_-1,0"
    

    for set_Pow in lo_Pow :
        
#         '''###################
#             dpath_Full : modify        
#         ###################'''
# #         dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%d,pick-%d)" \
# #         dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%.1f,pick-%.1f)" \
#         dpath_Full_tmp = dpath_Full + "." + "pow.(%d-%d.pi)(base-%.1f,pick-%.1f)" \
#             % (val_StartingPoint_Multiplier, 
#                val_StartingPoint_PiDivisor
#                , num_Base
#                , tuple(set_Pow)[0]
# #                , num_Pick
#                )

        '''###################
            gen : png files        
        ###################'''

#                     (dpath_Full_tmp
        dpath_Full_Each = _test_1_2__Generate_PNGFiles \
                    (dpath_Full
                     , session_Label
                     , tuple(set_Pow)
#                      , set_Pow
                     , id_Dir
                     , start_Coord
                     , _numOf_TickDivision)
#                     (dpath_Full, session_Label, set_Pow, id_Dir)

        '''###################
            path : modify        
        ###################'''
        fpath_Out_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Out_FFMpeg)

        fpath_In_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_In_FFMpeg)

        fpath_Glob = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Glob)

        '''###################
            video        
        ###################'''
#         result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                         fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)

        '''###################
            increment        
        ###################'''
        id_Dir += 1

    #/for set_Pow in lo_Pow :    
    
    '''###################
        video        
    ###################'''
#     result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                     fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)
    
    
#/def test_7_4():


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
    
#     plt.show()
    
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

def _test_1_1__Generate_PNGFiles \
(dpath_Full, session_Label, 
set_Pow, id_Dir, 
start_Coord=(np.cos(pi / 4 * 0), np.sin(pi / 4 * 0)),
_numOf_TickDivision = 24
):
# def _test_1_1__Generate_PNGFiles(dpath_Full, session_Label):
    
#     #debug
#     print()
#     print("[%s:%d] set_Pow => \n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , set_Pow
#         ), file=sys.stderr)
#     
#     return
    
    '''###################
        gen : directory        
    ###################'''
        # dirs
#     dpath_Full_Each = "%s\\%s.(%02d)(%s)" \
#     dpath_Full_Each = "%s\\%s.(%02d)(pow_%s)" \

    dpath_Full_Each = dpath_Full
#     dpath_Full_Each = "%s\\%s.(%02d)(pow.%s)" \
#                 % (
#                     dpath_Full
#                     , os.path.basename(dpath_Full)
#                     , id_Dir
#                     , "-".join([str(x) for x in set_Pow])
#                 )
                
#     dpath_Full_Each = "%s\\%s.(%02d)" \
#                 % (dpath_Full, os.path.basename(dpath_Full), id_Dir)
    
    if not os.path.isdir(dpath_Full_Each) : os.makedirs(dpath_Full_Each)
#     if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)

    print()
    print("[%s:%d] dpath_Full_Each => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Full_Each
        ), file=sys.stderr)

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
    
#     numOf_TickDivision = 24  # used in : tick_Rotate
#     numOf_TickDivision = 4  # used in : tick_Rotate
    numOf_TickDivision = _numOf_TickDivision  # used in : tick_Rotate
    
    val_StartingPoint_Multiplier = 1    # used in : x, y
    
    val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11 = \
            (1.0, 1.0, 1.0, 1.0)
#             (2.0, 3.0, 4.0, 1.0)
#             (3.0, 4.0, 1.0, 2.0)
#             (4.0, 1.0, 2.0, 3.0)
#             (1.0, 2.0, 3.0, 4.0)
#             (1.0, 2.0, 1.0, 3.0)
#             (2.0, 1.0, 1.0, 3.0)
#             (2.0, 1.0, 3.0, 1.0)
    
    val_Scalar_Max = max((val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11))
    
    # cos and sin signs
    pow_a00, pow_a01, pow_a10, pow_a11 = set_Pow
#     pow_a00, pow_a01, pow_a10, pow_a11 = \
#                         (1, 1, 1, 2)
#                         (1, 1, 2, 1)
#                         (1, 2, 1, 1)
#                         (2, 1, 1, 1)
                        
    # cos and sin signs
    rot_a00, rot_a01, rot_a10, rot_a11 = \
                        (1., -1., 1., 1.)
#                         (1., 1., -1., 1)
#                         (1., 1., 1., 1)
#                         (1., 1., 1., -1)
#                         (-1., 1., 1., 1)
    
#     tick_Rotate = np.pi / 4
#     tick_Rotate = np.pi / 12
    tick_Rotate = np.pi / numOf_TickDivision
#     tick_Rotate = np.pi / 24
    
    cnt = 0
    
    '''###################
        starting point        
    ###################'''
#     x = 1; y = 1
#     x = np.cos(pi / 2); y = np.sin(pi / 2)
#     x = np.cos(pi / 4); y = np.sin(pi / 4)
#     x, y = np.cos(pi / 4 * (-3)), np.sin(pi / 4 * (-3))
#     x, y = np.cos(pi / 4 * 3), np.sin(pi / 4 * 3)
    x, y = start_Coord
#     x, y = np.cos(pi / 4 * val_StartingPoint_Multiplier) \
#             , np.sin(pi / 4 * val_StartingPoint_Multiplier)   #
#     x, y = np.cos(pi / 4 * 1), np.sin(pi / 4 * 1)   # 45'
#     x, y = np.cos(pi / 4 * 2), np.sin(pi / 4 * 2)
#     x = np.cos(pi / 4 * 0); y = np.sin(pi / 4 * 0)  # (1, 0)
#     x = np.cos(pi / 4 * 3); y = np.sin(pi / 4 * 3)
#     x = 1; y = 0
    
    xs_ = []
    ys_ = []
    
    '''###################
        loop : i : rotate : x^2 + y^2 = 1        
    ###################'''
    for i in np.arange(0, np.pi * 2, tick_Rotate) :
 
#         '''###################
#             settings        
#         ###################'''
# #             plt.grid(b=None, which='major', axis='both')
#  
#         fig = plt.figure()
#          
#         #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
#         fig.set_facecolor("#fff9c9")
#          
#         #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
#         fig.set_size_inches(18.5, 10.5)
#          
#          
#         ax  = fig.add_subplot(111)
#  
#         #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
#         ax.set_facecolor("honeydew") # 
#          
#         ax.grid(b=None, which='major', axis='both')
#          
#         #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
#         ax.set_aspect('equal')
#  
#         #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
#          
#         ax.set_xlim(lim_X_Start, lim_X_End)
#         ax.set_ylim(lim_Y_Start, lim_Y_End)
#          
#         '''###################
#             label : y
#         ###################'''
#         #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
#         tickVal_Y = 1
#         tickVal_X = 1
#          
#         # y ax
#         y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
#         ax.set_yticks(y_tick)
#         ax.set_yticklabels(y_tick, fontsize = 15)
# #         ax.set_yticklabels(y_tick, fontsize = 10)
#  
#         # x ax
#         x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
#         ax.set_xticks(x_tick)
#         ax.set_xticklabels(x_tick, fontsize = 15)
# #         ax.set_xticklabels(x_tick, fontsize = 10)
 
        '''###################
            rotate
        ###################'''
#         rot_a00, rot_a01, rot_a10, rot_a11 = (1., -1., 1., 1.)
#         rot_a00 =  1
#         rot_a01 = -1
#         rot_a10 =  1
#         rot_a11 =  1
         
        rot = [
             
#                 [np.cos(i) * rot_a00, np.sin(i) * rot_a01],
#                 [np.sin(i) * rot_a10, np.cos(i) * rot_a11],
#                 [np.cos(i), - np.sin(i)],
#                 [np.sin(i),   np.cos(i)],
#                 [np.cos(i) * val_Scalar_a00, - np.sin(i) * val_Scalar_a01],
#                 [np.sin(i) * val_Scalar_a10,   np.cos(i) * val_Scalar_a11],
            [
                (np.cos(i) ** pow_a00) * val_Scalar_a00 * rot_a00
                , (np.sin(i) ** pow_a01) * val_Scalar_a01 * rot_a01
             ],
            [
                (np.sin(i) ** pow_a10) * val_Scalar_a10 * rot_a10
                , (np.cos(i) ** pow_a11) * val_Scalar_a11 * rot_a11
             ],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
             
            ]
         
        x2 = rot[0][0] * x + rot[0][1] * y
        y2 = rot[1][0] * x + rot[1][1] * y
 
        # append
        xs_.append(x2)
        ys_.append(y2)
 
    '''###################
        settings        
    ###################'''
    #             plt.grid(b=None, which='major', axis='both')
    
    fig = plt.figure()
     
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    fig.set_facecolor("#fff9c9")
     
    #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
    fig.set_size_inches(18.5, 10.5)
     
     
    ax  = fig.add_subplot(111)
    
    #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
    ax.set_facecolor("honeydew") # 
     
    ax.grid(b=None, which='major', axis='both')
     
    #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
    ax.set_aspect('equal')
    
    #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
     
    ax.set_xlim(lim_X_Start, lim_X_End)
    ax.set_ylim(lim_Y_Start, lim_Y_End)
     
    '''###################
        label : y
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_Y = 1
    tickVal_X = 1
     
    # y ax
    y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_tick, fontsize = 15)
    #         ax.set_yticklabels(y_tick, fontsize = 10)
    
    # x ax
    x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
    ax.set_xticks(x_tick)
    ax.set_xticklabels(x_tick, fontsize = 15)
    #         ax.set_xticklabels(x_tick, fontsize = 10)
 
    '''###################
        circle        
    ###################'''
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    #ref alpha https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html
    circle1 = plt.Circle(
                (0, 0)
                , 1.0
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    c2 = plt.Circle(
                (0, 0)
                , val_Scalar_Max
    #                     , val_Scalar_a01
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    ax.add_artist(circle1)
    ax.add_artist(c2)
    
     
    '''###################
        plot        
    ###################'''
    col_Series = "#00ff%02x" % (int(255 / numOf_TickDivision * cnt))
    
    #ref https://stackoverflow.com/questions/17682216/scatter-plot-and-color-mapping-in-python answered Jul 16 '13 at 16:45
    ax.scatter(xs_, ys_, s = 20, c = range(0, len(xs_)), cmap='viridis')
#     ax.scatter([x2], [y2], s = 30, color = 'gray')

    '''###################
        ops        
    ###################'''
    '''###################
        labels : title
    ###################'''
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n%s" \
    fpath_Images_Out = "%s\\%s.%s.(pow.%s).png" \
        % (dpath_Full_Each, session_Label, tlabel, "-".join([str(x) for x in set_Pow]))
#     fpath_Images_Out = "%s\\%s.%s.png" \
#         % (dpath_Full_Each, session_Label, tlabel)

#     fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
#         % (dpath_Full_Each, session_Label, tlabel, cnt)
    #             % (dpath_Full, session_Label, tlabel, cnt)
    
    #         str_Title = "[rot] %.03f pi / [point] (%.2f pi, %.2f pi)\n" \
    str_Title = "[rot] %.02f pi / [point] (%.2f pi, %.2f pi)\n" \
                + "[abcd] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #         str_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
    #                     + "%s" \
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n%s" \
    plt_Title = str_Title \
            % (
    #                     index / np.pi
                i / np.pi
                , x / np.pi, y / np.pi
#                 , x2 / np.pi, y2 / np.pi
                , val_Scalar_a00
                , val_Scalar_a01
                , val_Scalar_a10
                , val_Scalar_a11
    #                     , os.path.basename(fpath_Images_Out)
               )
             
    #         ax.set_title(plt_Title)
    plt.title(plt_Title, fontsize = 15)
    #         plt.title(plt_Title)
    
    '''###################
        labels : x label
    ###################'''
    str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
                + "[pow] 00 : %.1f / 01 : %.1f / 10 : %.1f / 11 : %.1f\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
    #         str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_XLabel = str_XLabel \
            % (
                  rot_a00
                , rot_a01
                , rot_a10
                , rot_a11
                 
                , pow_a00
                , pow_a01
                , pow_a10
                , pow_a11
                 
               )
             
    ax.set_xlabel(plt_XLabel, fontsize = 15)
    #         ax.set_xlabel(plt_XLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        labels : y label
    ###################'''
    str_YLabel = "[file] %s"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_YLabel = str_YLabel \
            % (
                  os.path.basename(fpath_Images_Out)
                 
               )
             
    ax.set_ylabel(plt_YLabel, fontsize = 15)
    #         ax.set_ylabel(plt_YLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        plot, save image        
    ###################'''
    #         plt.plot(x, y)
     
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

    #/for i in np.arange(0, np.pi * 2, tick_Rotate) :
    
    '''###################
        return        
    ###################'''
    return dpath_Full_Each

'''###################
    test_1_1()        
###################'''
def test_1_1():

#     ### test
#     num_Base = 1
# #     num_Pick = 2.3
#     num_Pick = 2
#     lenOf_Num_Pick = 3
# #     lenOf_Num_Pick = 2
# #     lenOf_List = 5
#     lenOf_List = 4
#     
#     res = libs_VX7GLZ.get_Combi_ALL(num_Base, num_Pick, lenOf_List)
# #     res = libs_VX7GLZ.get_Combi(num_Base, num_Pick, lenOf_Num_Pick, lenOf_List)
#     
#     print()
#     print("[%s:%d] res =>\nlen = (%d)\n" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(res)
#         ), file=sys.stderr)
#     
#     for item in res:
# 
#         print(item)
#         
#     #/for item in res:
# 
#     
# #     print("[%s:%d] res => %s" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum()
# #         , res
# #         ), file=sys.stderr)
# #     
#     return
    
    
    '''###################
        get : paths        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()

    PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT_27_6_5.value
#     PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT.value
    
    dname_Folder_Data   = "data.27_6_5"
    dname_Images       = "images"
    dname_Images_PNG   = "images_%s" % tlabel
    session_Label      = "6_5.test_1_1"
    
    fps_FFMpeg          = 6 # 4 frames per second
#     fps_FFMpeg          = 2
    
    _numOf_TickDivision = 24
    
    
    dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = \
                libs_VX7GLZ.get_FFMpeg_Paths \
                (PROJECT_ROOT, 
                 dname_Folder_Data, 
                 dname_Images, 
                 dname_Images_PNG, 
                 session_Label)
    
    # cos and sin signs
    cons_Pow = 3.5
    
    num_Base    = 1
    num_Pick   = 5  # pow --> 5
#     num_Pick   = 4  # pow --> 4
#     num_Pick   = 3  # pow --> 3
#     num_Pick   = 2
    lenOf_List = 4
    
    lo_Pow = libs_VX7GLZ.get_Combi_ALL(num_Base, num_Pick, lenOf_List)

#     print()
#     print("[%s:%d] lo_Pow =>\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , tuple(lo_Pow)
# #         , lo_Pow
#         ), file=sys.stderr)
#      
#     return

#     lo_Pow = (
#                   (cons_Pow, cons_Pow, 1, 1)
#                 , (cons_Pow, 1, cons_Pow, 1)
#                 , (cons_Pow, 1, 1, cons_Pow)
#                 , (1, cons_Pow, cons_Pow, 1)
#                 , (1, cons_Pow, 1, cons_Pow)
#                 , (1, 1, cons_Pow, cons_Pow)
#                   (3, 3, 1, 1)
#                 , (3, 1, 3, 1)
#                 , (3, 1, 1, 3)
#                 , (1, 3, 3, 1)
#                 , (1, 3, 1, 3)
#                 , (1, 1, 3, 3)
#                   (2, 2, 1, 1)
#                 , (2, 1, 2, 1)
#                 , (2, 1, 1, 2)
#                 , (1, 2, 2, 1)
#                 , (1, 2, 1, 2)
#                 , (1, 1, 2, 2)
#                 (1, 1, 1, 1)
#                 , (2, 1, 1, 1)
#                 , (1, 2, 1, 1)
#                 , (1, 1, 2, 1)
#                 , (1, 1, 1, 2)
#           )

    # id dir
    id_Dir = 0

    '''###################
        set : starting point        
    ###################'''
    val_StartingPoint_Multiplier = 1
#     val_StartingPoint_Multiplier = 3
#     val_StartingPoint_Multiplier = 2
#     val_StartingPoint_Multiplier = 5
    
#     val_StartingPoint_PiDivisor = 3
    val_StartingPoint_PiDivisor = 4
#     val_StartingPoint_PiDivisor = 9
#     val_StartingPoint_PiDivisor = 12
    
    start_Coord = (
#             0
#             , 0)
            np.cos(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier)
            , np.sin(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier))
#             np.cos(pi / 4 * val_StartingPoint_Multiplier)
#             , np.sin(pi / 4 * val_StartingPoint_Multiplier))

    print()
    print("[%s:%d] start_Coord => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , start_Coord
        ), file=sys.stderr)

    '''###################
        dpath_Full : modify        
    ###################'''
#     dpath_Full = dpath_Full + "." + "pow.(start_%.2fpi,%.2fpi)" \
#     dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)" \
    dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)(base-%d,pick-%d)" \
                % (val_StartingPoint_Multiplier, 
                   val_StartingPoint_PiDivisor
                   , num_Base, num_Pick
                   )
#                 % (start_Coord[0], start_Coord[1])
#     dpath_Full = dpath_Full + "." + "pow.start_-1,0"
    

    for set_Pow in lo_Pow :
        '''###################
            gen : png files        
        ###################'''
#         val_StartingPoint_Multiplier = 3
#         
#         start_Coord = (
#                 np.cos(pi / 4 * val_StartingPoint_Multiplier)
#                 , np.sin(pi / 4 * val_StartingPoint_Multiplier))

        dpath_Full_Each = _test_1_1__Generate_PNGFiles \
                    (dpath_Full
                     , session_Label
                     , tuple(set_Pow)
#                      , set_Pow
                     , id_Dir
                     , start_Coord
                     , _numOf_TickDivision)
#                     (dpath_Full, session_Label, set_Pow, id_Dir)

        '''###################
            path : modify        
        ###################'''
        fpath_Out_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Out_FFMpeg)

        fpath_In_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_In_FFMpeg)

        fpath_Glob = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Glob)

        '''###################
            video        
        ###################'''
#         result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                         fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)

        '''###################
            increment        
        ###################'''
        id_Dir += 1

    #/for set_Pow in lo_Pow :    
    
    '''###################
        video        
    ###################'''
#     result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                     fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)
    
    
#/def test_7_4():


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
    
#     plt.show()
    
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

def _test_1__Generate_PNGFiles \
(dpath_Full, session_Label, 
set_Pow, id_Dir, 
start_Coord=(np.cos(pi / 4 * 0), np.sin(pi / 4 * 0)),
_numOf_TickDivision = 24
):
# def _test_1__Generate_PNGFiles(dpath_Full, session_Label):
    
#     #debug
#     print()
#     print("[%s:%d] set_Pow => \n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , set_Pow
#         ), file=sys.stderr)
#     
#     return
    
    '''###################
        gen : directory        
    ###################'''
        # dirs
#     dpath_Full_Each = "%s\\%s.(%02d)(%s)" \
#     dpath_Full_Each = "%s\\%s.(%02d)(pow_%s)" \

    dpath_Full_Each = dpath_Full
#     dpath_Full_Each = "%s\\%s.(%02d)(pow.%s)" \
#                 % (
#                     dpath_Full
#                     , os.path.basename(dpath_Full)
#                     , id_Dir
#                     , "-".join([str(x) for x in set_Pow])
#                 )
                
#     dpath_Full_Each = "%s\\%s.(%02d)" \
#                 % (dpath_Full, os.path.basename(dpath_Full), id_Dir)
    
    if not os.path.isdir(dpath_Full_Each) : os.makedirs(dpath_Full_Each)
#     if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)

    print()
    print("[%s:%d] dpath_Full_Each => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Full_Each
        ), file=sys.stderr)

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
    
#     numOf_TickDivision = 24  # used in : tick_Rotate
#     numOf_TickDivision = 4  # used in : tick_Rotate
    numOf_TickDivision = _numOf_TickDivision  # used in : tick_Rotate
    
    val_StartingPoint_Multiplier = 1    # used in : x, y
    
    val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11 = \
            (1.0, 1.0, 1.0, 1.0)
#             (2.0, 3.0, 4.0, 1.0)
#             (3.0, 4.0, 1.0, 2.0)
#             (4.0, 1.0, 2.0, 3.0)
#             (1.0, 2.0, 3.0, 4.0)
#             (1.0, 2.0, 1.0, 3.0)
#             (2.0, 1.0, 1.0, 3.0)
#             (2.0, 1.0, 3.0, 1.0)
    
    val_Scalar_Max = max((val_Scalar_a00, val_Scalar_a01, val_Scalar_a10, val_Scalar_a11))
    
    # cos and sin signs
    pow_a00, pow_a01, pow_a10, pow_a11 = set_Pow
#     pow_a00, pow_a01, pow_a10, pow_a11 = \
#                         (1, 1, 1, 2)
#                         (1, 1, 2, 1)
#                         (1, 2, 1, 1)
#                         (2, 1, 1, 1)
                        
    # cos and sin signs
    rot_a00, rot_a01, rot_a10, rot_a11 = \
                        (1., -1., 1., 1.)
#                         (1., 1., -1., 1)
#                         (1., 1., 1., 1)
#                         (1., 1., 1., -1)
#                         (-1., 1., 1., 1)
    
#     tick_Rotate = np.pi / 4
#     tick_Rotate = np.pi / 12
    tick_Rotate = np.pi / numOf_TickDivision
#     tick_Rotate = np.pi / 24
    
    cnt = 0
    
    '''###################
        starting point        
    ###################'''
#     x = 1; y = 1
#     x = np.cos(pi / 2); y = np.sin(pi / 2)
#     x = np.cos(pi / 4); y = np.sin(pi / 4)
#     x, y = np.cos(pi / 4 * (-3)), np.sin(pi / 4 * (-3))
#     x, y = np.cos(pi / 4 * 3), np.sin(pi / 4 * 3)
    x, y = start_Coord
#     x, y = np.cos(pi / 4 * val_StartingPoint_Multiplier) \
#             , np.sin(pi / 4 * val_StartingPoint_Multiplier)   #
#     x, y = np.cos(pi / 4 * 1), np.sin(pi / 4 * 1)   # 45'
#     x, y = np.cos(pi / 4 * 2), np.sin(pi / 4 * 2)
#     x = np.cos(pi / 4 * 0); y = np.sin(pi / 4 * 0)  # (1, 0)
#     x = np.cos(pi / 4 * 3); y = np.sin(pi / 4 * 3)
#     x = 1; y = 0
    
    xs_ = []
    ys_ = []
    
    '''###################
        loop : i : rotate : x^2 + y^2 = 1        
    ###################'''
    for i in np.arange(0, np.pi * 2, tick_Rotate) :
 
#         '''###################
#             settings        
#         ###################'''
# #             plt.grid(b=None, which='major', axis='both')
#  
#         fig = plt.figure()
#          
#         #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
#         fig.set_facecolor("#fff9c9")
#          
#         #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
#         fig.set_size_inches(18.5, 10.5)
#          
#          
#         ax  = fig.add_subplot(111)
#  
#         #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
#         ax.set_facecolor("honeydew") # 
#          
#         ax.grid(b=None, which='major', axis='both')
#          
#         #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
#         ax.set_aspect('equal')
#  
#         #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
#          
#         ax.set_xlim(lim_X_Start, lim_X_End)
#         ax.set_ylim(lim_Y_Start, lim_Y_End)
#          
#         '''###################
#             label : y
#         ###################'''
#         #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
#         tickVal_Y = 1
#         tickVal_X = 1
#          
#         # y ax
#         y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
#         ax.set_yticks(y_tick)
#         ax.set_yticklabels(y_tick, fontsize = 15)
# #         ax.set_yticklabels(y_tick, fontsize = 10)
#  
#         # x ax
#         x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
#         ax.set_xticks(x_tick)
#         ax.set_xticklabels(x_tick, fontsize = 15)
# #         ax.set_xticklabels(x_tick, fontsize = 10)
 
        '''###################
            rotate
        ###################'''
#         rot_a00, rot_a01, rot_a10, rot_a11 = (1., -1., 1., 1.)
#         rot_a00 =  1
#         rot_a01 = -1
#         rot_a10 =  1
#         rot_a11 =  1
         
        rot = [
             
#                 [np.cos(i) * rot_a00, np.sin(i) * rot_a01],
#                 [np.sin(i) * rot_a10, np.cos(i) * rot_a11],
#                 [np.cos(i), - np.sin(i)],
#                 [np.sin(i),   np.cos(i)],
#                 [np.cos(i) * val_Scalar_a00, - np.sin(i) * val_Scalar_a01],
#                 [np.sin(i) * val_Scalar_a10,   np.cos(i) * val_Scalar_a11],
            [
                (np.cos(i) ** pow_a00) * val_Scalar_a00 * rot_a00
                , (np.sin(i) ** pow_a01) * val_Scalar_a01 * rot_a01
             ],
            [
                (np.sin(i) ** pow_a10) * val_Scalar_a10 * rot_a10
                , (np.cos(i) ** pow_a11) * val_Scalar_a11 * rot_a11
             ],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
#             [np.cos(i) * val_Scalar_a00 * rot_a00, np.sin(i) * val_Scalar_a01 * rot_a01],
#             [np.sin(i) * val_Scalar_a10 * rot_a10, np.cos(i) * val_Scalar_a11 * rot_a11],
             
            ]
         
        x2 = rot[0][0] * x + rot[0][1] * y
        y2 = rot[1][0] * x + rot[1][1] * y
 
        # append
        xs_.append(x2)
        ys_.append(y2)
 
    '''###################
        settings        
    ###################'''
    #             plt.grid(b=None, which='major', axis='both')
    
    fig = plt.figure()
     
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    fig.set_facecolor("#fff9c9")
     
    #ref https://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib answered Nov 29 '10 at 17:30
    fig.set_size_inches(18.5, 10.5)
     
     
    ax  = fig.add_subplot(111)
    
    #ref https://stackoverflow.com/questions/14088687/how-to-change-plot-background-color answered May 14 '14 at 4:05
    ax.set_facecolor("honeydew") # 
     
    ax.grid(b=None, which='major', axis='both')
     
    #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
    ax.set_aspect('equal')
    
    #ref https://stackoverflow.com/questions/15858192/how-to-set-xlim-and-ylim-for-a-subplot-in-matplotlib answered Apr 7 '13 at 2:33
     
    ax.set_xlim(lim_X_Start, lim_X_End)
    ax.set_ylim(lim_Y_Start, lim_Y_End)
     
    '''###################
        label : y
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_Y = 1
    tickVal_X = 1
     
    # y ax
    y_tick = np.arange(lim_Y_Start, lim_Y_End + tickVal_Y, tickVal_Y)
    ax.set_yticks(y_tick)
    ax.set_yticklabels(y_tick, fontsize = 15)
    #         ax.set_yticklabels(y_tick, fontsize = 10)
    
    # x ax
    x_tick = np.arange(lim_X_Start, lim_X_End + tickVal_X, tickVal_X)
    ax.set_xticks(x_tick)
    ax.set_xticklabels(x_tick, fontsize = 15)
    #         ax.set_xticklabels(x_tick, fontsize = 10)
 
    '''###################
        circle        
    ###################'''
    #ref https://stackoverflow.com/questions/45771474/matplotlib-make-center-circle-transparent
    #ref alpha https://matplotlib.org/devdocs/api/_as_gen/matplotlib.pyplot.scatter.html
    circle1 = plt.Circle(
                (0, 0)
                , 1.0
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    c2 = plt.Circle(
                (0, 0)
                , val_Scalar_Max
    #                     , val_Scalar_a01
                , color='r'
                , fill= False
                , linewidth = 1
                , alpha = 0.5
            )
      
    ax.add_artist(circle1)
    ax.add_artist(c2)
    
     
    '''###################
        plot        
    ###################'''
    col_Series = "#00ff%02x" % (int(255 / numOf_TickDivision * cnt))
    
    #ref https://stackoverflow.com/questions/17682216/scatter-plot-and-color-mapping-in-python answered Jul 16 '13 at 16:45
    ax.scatter(xs_, ys_, s = 20, c = range(0, len(xs_)), cmap='viridis')
#     ax.scatter([x2], [y2], s = 30, color = 'gray')

    '''###################
        ops        
    ###################'''
    '''###################
        labels : title
    ###################'''
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n%s" \
    fpath_Images_Out = "%s\\%s.%s.(pow.%s).png" \
        % (dpath_Full_Each, session_Label, tlabel, "-".join([str(x) for x in set_Pow]))
#     fpath_Images_Out = "%s\\%s.%s.png" \
#         % (dpath_Full_Each, session_Label, tlabel)

#     fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
#         % (dpath_Full_Each, session_Label, tlabel, cnt)
    #             % (dpath_Full, session_Label, tlabel, cnt)
    
    #         str_Title = "[rot] %.03f pi / [point] (%.2f pi, %.2f pi)\n" \
    str_Title = "[rot] %.02f pi / [point] (%.2f pi, %.2f pi)\n" \
                + "[abcd] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #         str_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f"
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
    #                     + "%s" \
    #         plt_Title = "rot : %.03f pi / start = (%.2f pi, %.2f pi)\n00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n%s" \
    plt_Title = str_Title \
            % (
    #                     index / np.pi
                i / np.pi
                , x / np.pi, y / np.pi
#                 , x2 / np.pi, y2 / np.pi
                , val_Scalar_a00
                , val_Scalar_a01
                , val_Scalar_a10
                , val_Scalar_a11
    #                     , os.path.basename(fpath_Images_Out)
               )
             
    #         ax.set_title(plt_Title)
    plt.title(plt_Title, fontsize = 15)
    #         plt.title(plt_Title)
    
    '''###################
        labels : x label
    ###################'''
    str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n" \
                + "[pow] 00 : %.1f / 01 : %.1f / 10 : %.1f / 11 : %.1f\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
#                 + "[pow] 00 : %d / 01 : %d / 10 : %d / 11 : %d\n"
    #         str_XLabel = "[rot matrix] 00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_XLabel = str_XLabel \
            % (
                  rot_a00
                , rot_a01
                , rot_a10
                , rot_a11
                 
                , pow_a00
                , pow_a01
                , pow_a10
                , pow_a11
                 
               )
             
    ax.set_xlabel(plt_XLabel, fontsize = 15)
    #         ax.set_xlabel(plt_XLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        labels : y label
    ###################'''
    str_YLabel = "[file] %s"
    #         str_XLabel = "rot matrix\n" \
    #                     + "00 : %.2f / 01 : %.2f / 10 : %.2f / 11 : %.2f\n"
                 
    plt_YLabel = str_YLabel \
            % (
                  os.path.basename(fpath_Images_Out)
                 
               )
             
    ax.set_ylabel(plt_YLabel, fontsize = 15)
    #         ax.set_ylabel(plt_YLabel)
    #         plt.xlabel(plt_XLabel)
    
    '''###################
        plot, save image        
    ###################'''
    #         plt.plot(x, y)
     
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

    #/for i in np.arange(0, np.pi * 2, tick_Rotate) :
    
    '''###################
        return        
    ###################'''
    return dpath_Full_Each

'''###################
    test_1()        
###################'''
def test_1():

#     ### test
#     num_Base = 1
# #     num_Pick = 2.3
#     num_Pick = 2
#     lenOf_Num_Pick = 3
# #     lenOf_Num_Pick = 2
# #     lenOf_List = 5
#     lenOf_List = 4
#     
#     res = libs_VX7GLZ.get_Combi_ALL(num_Base, num_Pick, lenOf_List)
# #     res = libs_VX7GLZ.get_Combi(num_Base, num_Pick, lenOf_Num_Pick, lenOf_List)
#     
#     print()
#     print("[%s:%d] res =>\nlen = (%d)\n" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#          , len(res)
#         ), file=sys.stderr)
#     
#     for item in res:
# 
#         print(item)
#         
#     #/for item in res:
# 
#     
# #     print("[%s:%d] res => %s" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum()
# #         , res
# #         ), file=sys.stderr)
# #     
#     return
    
    
    '''###################
        get : paths        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()

    PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT_27_6_5.value
#     PROJECT_ROOT = cons_27_6_2.FPath.PROJECT_ROOT.value
    
    dname_Folder_Data   = "data.27_6_5"
    dname_Images       = "images"
    dname_Images_PNG   = "images_%s" % tlabel
    session_Label      = "6_5.test_1"
    
    fps_FFMpeg          = 6 # 4 frames per second
#     fps_FFMpeg          = 2
    
    _numOf_TickDivision = 24
    
    
    dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg = \
                libs_VX7GLZ.get_FFMpeg_Paths \
                (PROJECT_ROOT, 
                 dname_Folder_Data, 
                 dname_Images, 
                 dname_Images_PNG, 
                 session_Label)
    
    # cos and sin signs
    cons_Pow = 3.5
    
    num_Base    = 1
    num_Pick   = 2
    lenOf_List = 4
    
    lo_Pow = libs_VX7GLZ.get_Combi_ALL(num_Base, num_Pick, lenOf_List)

#     print()
#     print("[%s:%d] lo_Pow =>\n%s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , tuple(lo_Pow)
# #         , lo_Pow
#         ), file=sys.stderr)
#      
#     return

#     lo_Pow = (
#                   (cons_Pow, cons_Pow, 1, 1)
#                 , (cons_Pow, 1, cons_Pow, 1)
#                 , (cons_Pow, 1, 1, cons_Pow)
#                 , (1, cons_Pow, cons_Pow, 1)
#                 , (1, cons_Pow, 1, cons_Pow)
#                 , (1, 1, cons_Pow, cons_Pow)
#                   (3, 3, 1, 1)
#                 , (3, 1, 3, 1)
#                 , (3, 1, 1, 3)
#                 , (1, 3, 3, 1)
#                 , (1, 3, 1, 3)
#                 , (1, 1, 3, 3)
#                   (2, 2, 1, 1)
#                 , (2, 1, 2, 1)
#                 , (2, 1, 1, 2)
#                 , (1, 2, 2, 1)
#                 , (1, 2, 1, 2)
#                 , (1, 1, 2, 2)
#                 (1, 1, 1, 1)
#                 , (2, 1, 1, 1)
#                 , (1, 2, 1, 1)
#                 , (1, 1, 2, 1)
#                 , (1, 1, 1, 2)
#           )

    # id dir
    id_Dir = 0

    '''###################
        set : starting point        
    ###################'''
    val_StartingPoint_Multiplier = 1
#     val_StartingPoint_Multiplier = 3
#     val_StartingPoint_Multiplier = 2
#     val_StartingPoint_Multiplier = 5
    
#     val_StartingPoint_PiDivisor = 3
    val_StartingPoint_PiDivisor = 4
#     val_StartingPoint_PiDivisor = 9
#     val_StartingPoint_PiDivisor = 12
    
    start_Coord = (
#             0
#             , 0)
            np.cos(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier)
            , np.sin(pi / val_StartingPoint_PiDivisor * val_StartingPoint_Multiplier))
#             np.cos(pi / 4 * val_StartingPoint_Multiplier)
#             , np.sin(pi / 4 * val_StartingPoint_Multiplier))

    print()
    print("[%s:%d] start_Coord => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , start_Coord
        ), file=sys.stderr)

    '''###################
        dpath_Full : modify        
    ###################'''
#     dpath_Full = dpath_Full + "." + "pow.(start_%.2fpi,%.2fpi)" \
    dpath_Full = dpath_Full + "." + "pow.(%d-%d.pi)" \
                % (val_StartingPoint_Multiplier, val_StartingPoint_PiDivisor)
#                 % (start_Coord[0], start_Coord[1])
#     dpath_Full = dpath_Full + "." + "pow.start_-1,0"
    

    for set_Pow in lo_Pow :
        '''###################
            gen : png files        
        ###################'''
#         val_StartingPoint_Multiplier = 3
#         
#         start_Coord = (
#                 np.cos(pi / 4 * val_StartingPoint_Multiplier)
#                 , np.sin(pi / 4 * val_StartingPoint_Multiplier))

        dpath_Full_Each = _test_1__Generate_PNGFiles \
                    (dpath_Full
                     , session_Label
                     , tuple(set_Pow)
#                      , set_Pow
                     , id_Dir
                     , start_Coord
                     , _numOf_TickDivision)
#                     (dpath_Full, session_Label, set_Pow, id_Dir)

        '''###################
            path : modify        
        ###################'''
        fpath_Out_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Out_FFMpeg)

        fpath_In_FFMpeg = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_In_FFMpeg)

        fpath_Glob = dpath_Full_Each + "\\" \
            + os.path.basename(fpath_Glob)

        '''###################
            video        
        ###################'''
#         result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                         fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)

        '''###################
            increment        
        ###################'''
        id_Dir += 1

    #/for set_Pow in lo_Pow :    
    
    '''###################
        video        
    ###################'''
#     result = libs_VX7GLZ.build_Video_From_PNGFiles__V3(
#                     fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg, fps_FFMpeg)
    
    
#/def test_7_4():


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
#     test_5_1()
    test_2()
#     test_1_2()
#     test_1_1()
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



