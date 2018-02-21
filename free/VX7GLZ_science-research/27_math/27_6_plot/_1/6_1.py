# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_1\6_1.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17.1.py
at : 2018/02/21 10:34:31

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_1
python 6_1.py

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
        , numpy as np, matplotlib.patches as mpatches
from shutil import copyfile
from scipy.stats.stats import pearsonr

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
    
def _test_5__Params():
    
#     step_Theta = np.pi / 3
    step_Theta = np.pi / 6
     
    rng_Theta = np.arange(0, np.pi * 2, step_Theta)
#     rng_Theta = np.arange(0, np.pi * 2 + step_Theta, step_Theta)
    
#     rot = Matrix([
#             [np.cos(rng_Theta), - np.sin(rng_Theta)], 
#              [np.sin(rng_Theta), np.cos(rng_Theta)]]
#     )

    ### 
    x = 1; y = 0
    
#     r_ = []
    x_ = []
    y_ = []
    
    for item in rng_Theta:

#         rot = [
#                 [np.cos(rng_Theta), - np.sin(rng_Theta)], 
#                  [np.sin(rng_Theta), np.cos(rng_Theta)]
#          ]
        
        rot = Matrix([
                [np.cos(item), - np.sin(item)], 
                 [np.sin(item), np.cos(item)]]
        )
#         rot = Matrix([
#                 [np.cos(rng_Theta), - np.sin(rng_Theta)], 
#                  [np.sin(rng_Theta), np.cos(rng_Theta)]]
#         )
        
        ### calc
#         temp_X = rot[0][0] * x + rot[0][1] * y
#         temp_Y = rot[1][0] * x + rot[1][1] * y
        temp_X = rot[0,0] * x + rot[0,1] * y
        temp_Y = rot[1,0] * x + rot[1,1] * y
        
#         r_.append(temp_X, temp_Y)
#         r_.append([temp_X, temp_Y])
        
        x_.append(temp_X)
        y_.append(temp_Y)
        
#         print()
# #         print("[%s:%d] temp_X => %.5f" % \
#         print("[%s:%d] type(temp_X) => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , type(temp_X)
# #         , temp_X
#         ), file=sys.stderr)
        
    #/for item in rng_Theta:

    
#     print()
#     print("[%s:%d] len(rng_Theta) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(rng_Theta)
#         ), file=sys.stderr)
#     
#     print("[%s:%d] rng_Theta => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , rng_Theta
#         ), file=sys.stderr)
    
    
    '''###################
        return        
    ###################'''
    return x_, y_
    
#/def _test_5__Params():

'''###################
    <Ops>
    1. Scatter each point in z
    2. Scatter figure ---> save as png file

    @param dpath_Images: 
            e.g. "C:\\WORKS_2\\WS\\WS_Others\\free" \
                 + "\\VX7GLZ_science-research\\27_math" \
                 + "\\27_6_plot\\_1\\data.27_6_1\\images"
    @param file_Label: e.g. "6-1.test"
            => label will be "6-1.test.<time label>.(%02d).png"
    @param lbl_Plot_Title: e.g. "rotate"
            => title label : "rotate (%02d) : x = %.3f / y = %.3f\n%s"
    
    @return: dpath_Images_Out
###################'''
def _test_5_Generate_PNGFiles \
(z, dpath_Images, file_Label, lbl_Plot_Title):
    
#     '''###################
#         graph : settings        
#     ###################'''
#     # xlim
#     plt.xlim(-2,2)
#     plt.ylim(-2,2)
#     plt.grid(b=None, which='major', axis='both')

    '''###################
        paths and dirs
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
#     dpath_Images = "C:\\WORKS_2\\WS\\WS_Others\\free" \
#                 + "\\VX7GLZ_science-research\\27_math" \
#                 + "\\27_6_plot\\_1\\data.27_6_1\\images"
    
    dpath_Images_Out = "%s\\images_%s" % (dpath_Images, tlabel)
    
    # dirs
    if not os.path.isdir(dpath_Images_Out) : os.makedirs(dpath_Images_Out)
    
    '''###################
        plot        
    ###################'''
    cnt = 1
    
    for loc in z :
        
        '''###################
            graph : settings        
        ###################'''
        # xlim
        plt.xlim(-2,2)
        plt.ylim(-2,2)
        plt.grid(b=None, which='major', axis='both')

        fpath_Images_Out = "%s\\%s.%s.(%02d).png" \
                % (dpath_Images_Out, file_Label, tlabel, cnt)
#         fpath_Images_Out = "%s\\6_1.%s.(%02d).png" \
                 
        print()
        print("[%s:%d] fpath_Images_Out => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Images_Out
            ), file=sys.stderr)
         
        '''###################
            title
        ###################'''
#         plt_Title = "rotate : (%02d) : x = %.4f / y = %.4f\n%s" \
        plt_Title = "%s : (%02d) : x = %.4f / y = %.4f\n%s" \
                    % (lbl_Plot_Title, cnt, loc[0], loc[1], 
                       os.path.basename(fpath_Images_Out))
#                     % (cnt, loc[0], loc[1], os.path.basename(fpath_Images_Out))
                    
        plt.title(plt_Title)
        
        '''###################
            grid        
        ###################'''
#         plt.grid(b=None, which='major', axis='both')
         
        '''###################
            plot        
        ###################'''
        plt.scatter([loc[0]], [loc[1]], s = 60)
         
    #     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
        plt.savefig(fpath_Images_Out)
    
        '''###################
            increment        
        ###################'''
        cnt += 1
    
        '''###################
            reset : figure  
        ###################'''
        plt.clf()
    
    '''###################
        return        
    ###################'''
    return dpath_Images_Out, tlabel

#/def _test_5_Generate_PNGFiles():
    
def test_5_3():

    '''###################
        params
    ###################'''
    x_, y_ = _test_5__Params()
 
    z = list(zip(x_, y_))
 
    dpath_Images = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\27_math" \
                + "\\27_6_plot\\_1\\data.27_6_1\\images"
 
    file_Label = "6_1.test-5-3"
     
    lbl_Plot_Title = "Rotate matrix"
 
    '''###################
        gen : png files        
    ###################'''
    dpath_Images_Out, tlabel = \
                _test_5_Generate_PNGFiles \
                (z, dpath_Images, file_Label, lbl_Plot_Title)

    '''###################
        gen : video        
    ###################'''
#     dpath_Images_Out = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1\\data.27_6_1\\images\\images_20180221_152007"
    
    fpath_Glob = "%s\\*(*).png" % (dpath_Images_Out)
#     fpath_Glob = "%s\\*.(*).png" % (dpath_Images_Out)
#     fpath_Glob = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1\\data.27_6_1\\images\\images_20180221_152007\\*.(*).png"
#     fpath_Glob = dpath_Images_Out

    fpath_In_FFMpeg = "%s\\image.%%03d.png" % (dpath_Images_Out)
#     fpath_In_FFMpeg = "%s\\image.%%03d.png" % (fpath_Glob)
    
    tlabel2 = libs.get_TimeLabel_Now()
    
    fpath_Out_FFMpeg = "%s\\movie.%s.%s.mp4" % (dpath_Images_Out, tlabel, tlabel2)
#     fpath_Out_FFMpeg = "%s\\movie.%s.mp4" % (fpath_Glob, tlabel)
    
    libs_VX7GLZ.build_Video_From_PNGFiles__V2 \
        (fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg)


#     '''###################
#         graph : settings        
#     ###################'''
#     # xlim
#     plt.xlim(-2,2)
#     plt.ylim(-2,2)
#     plt.grid(b=None, which='major', axis='both')
# 
#     '''###################
#         paths and dirs
#     ###################'''
#     tlabel = libs.get_TimeLabel_Now()
#     
#     dpath_Images = "C:\\WORKS_2\\WS\\WS_Others\\free" \
#                 + "\\VX7GLZ_science-research\\27_math" \
#                 + "\\27_6_plot\\_1\\data.27_6_1\\images"
#     
#     dpath_Images_Out = "%s\\images_%s" % (dpath_Images, tlabel)
#     
#     # dirs
#     if not os.path.isdir(dpath_Images_Out) : os.makedirs(dpath_Images_Out)
#     
#     '''###################
#         plot        
#     ###################'''
#     cnt = 1
#     
#     for loc in z :
#          
#         fpath_Images_Out = "%s\\6_1.%s.(%02d).png" \
#                 % (dpath_Images_Out, tlabel, cnt)
#                  
#         print()
#         print("[%s:%d] fpath_Images_Out => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , fpath_Images_Out
#             ), file=sys.stderr)
#          
#         '''###################
#             title
#         ###################'''
#         plt_Title = "rotate : (%02d) : x = %.4f / y = %.4f\n%s" \
#                     % (cnt, loc[0], loc[1], os.path.basename(fpath_Images_Out))
#                     
#         plt.title(plt_Title)
#         
#         '''###################
#             grid        
#         ###################'''
# #         plt.grid(b=None, which='major', axis='both')
#          
#         '''###################
#             plot        
#         ###################'''
#         plt.scatter([loc[0]], [loc[1]], s = 60)
#          
#     #     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
#         plt.savefig(fpath_Images_Out)
#     
#         '''###################
#             increment        
#         ###################'''
#         cnt += 1
    
def test_5_2():

    '''###################
        params
    ###################'''
    x_, y_ = _test_5__Params()

    z = list(zip(x_, y_))

    '''###################
        graph : settings        
    ###################'''
    # xlim
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    plt.grid(b=None, which='major', axis='both')

    '''###################
        paths and dirs
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Images = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\27_math" \
                + "\\27_6_plot\\_1\\data.27_6_1\\images"
    
    dpath_Images_Out = "%s\\images_%s" % (dpath_Images, tlabel)
    
    # dirs
    if not os.path.isdir(dpath_Images_Out) : os.makedirs(dpath_Images_Out)
    
    '''###################
        plot        
    ###################'''
    cnt = 1
    
    for loc in z :
         
        fpath_Images_Out = "%s\\6_1.%s.(%02d).png" \
                % (dpath_Images_Out, tlabel, cnt)
                 
        print()
        print("[%s:%d] fpath_Images_Out => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Images_Out
            ), file=sys.stderr)
         
        '''###################
            title
        ###################'''
        plt_Title = "rotate : (%02d) : x = %.4f / y = %.4f\n%s" \
                    % (cnt, loc[0], loc[1], os.path.basename(fpath_Images_Out))
                    
        plt.title(plt_Title)
        
        '''###################
            grid        
        ###################'''
#         plt.grid(b=None, which='major', axis='both')
         
        '''###################
            plot        
        ###################'''
        plt.scatter([loc[0]], [loc[1]], s = 60)
         
    #     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
        plt.savefig(fpath_Images_Out)
    
        '''###################
            increment        
        ###################'''
        cnt += 1
    
#     plt.savefig("%s\\6_1.%s.png" % (dpath_Out, libs.get_TimeLabel_Now()))
    
#     plt.show()
    
#/def test_4():

def test_5():

    '''###################
        params
    ###################'''
    x_, y_ = _test_5__Params()

    z = list(zip(x_, y_))

    '''###################
        graph : settings        
    ###################'''

    
    # xlim
    plt.xlim(-2,2)
    plt.ylim(-2,2)
    plt.grid(b=None, which='major', axis='both')
    
#     plt.scatter([z[0][0]], [z[0][1]], s = 60)
# #     plt.scatter([z[0][0]], [z[0][1]], linewidth = 30)
#      
#     plt.show()
# 
#     print()
# #     print("[%s:%d] x_[0] => %s" % \
#     print("[%s:%d] x_ => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , x_
#         ), file=sys.stderr)
# #     print()
# #     print("[%s:%d] z[0] => %s" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum()
# #         , z[0]
# #         ), file=sys.stderr)
# #     print()
# #     print("[%s:%d] r_[0] => %s" % \
# #         (os.path.basename(libs.thisfile()), libs.linenum()
# #         , r_[0]
# #         ), file=sys.stderr)

    '''###################
        plot        
    ###################'''
#     plt.scatter([r_[0][0]], [r_[0][1]], linewidth = 30)
# #     plt.plot([r_[0][0]], [r_[0][1]], linewidth = 30)
# #     plt.plot(r_[0][0], r_[0][1], linewidth = 20)
#     
#     plt.show()
    
#     #debug
#     return

    
#     print()
#     print("[%s:%d] r_ returned => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(r_)
#             ), file=sys.stderr)
#     
#     #debug
#     return

#     step_Theta = np.pi / 6
#     
#     rng_Theta = np.arange(0, np.pi * 2 + step_Theta, step_Theta)
#     
# #     x = np.sin(rng_Theta)
# #     y = np.cos(rng_Theta)
#     
#     r = Matrix([
#             [1],
#             [0]
#         
#         ])
#     
#     rot = Matrix([
#                 [np.cos(rng_Theta), - np.sin(rng_Theta)], 
#                  [np.sin(rng_Theta), np.cos(rng_Theta)]]
#         )
#     
#     prod = rot * r
#     
#     print()
#     print("[%s:%d] len(rot) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(rot)
#         ), file=sys.stderr)
#     print("[%s:%d] len(prod) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(prod)
#         ), file=sys.stderr)
#     
#     #debug
#     return
    
    #
    cnt = 1
    
    tlabel = libs.get_TimeLabel_Now()
    
    # dir
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1"
    
#     for loc in z :
#         
#         fpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
#                 + "\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1" \
#                 + "\\6_1.%s.(%02d).png" % (tlabel, cnt)
#                 
# #         print()
# #         print("[%s:%d] fpath_Out => %s" % \
# #             (os.path.basename(libs.thisfile()), libs.linenum()
# #             , fpath_Out
# #             ), file=sys.stderr)
#         
#         '''###################
#             title
#         ###################'''
#         plt.title("rotate : (%02d) : x = %.4f / y = %.4f\n%s" \
#                     % (cnt, loc[0], loc[1], os.path.basename(fpath_Out)))
#         '''###################
#             grid        
#         ###################'''
# #         plt.grid(b=None, which='major', axis='both')
#         
#         '''###################
#             plot        
#         ###################'''
#         plt.scatter([loc[0]], [loc[1]], s = 60)
#         
#     #     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
#         plt.savefig(fpath_Out)
    
#     plt.savefig("%s\\6_1.%s.png" % (dpath_Out, libs.get_TimeLabel_Now()))
    
#     plt.show()
    
#/def test_4():

def test_4():

    '''###################
        plot        
    ###################'''
    rng_X_Scalar = 4
    
    rng_X_Start = - rng_X_Scalar * np.pi
    rng_X_End = rng_X_Scalar * np.pi
    
    x=np.linspace(rng_X_Start, rng_X_End, 1000)
#     x=np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y=np.sin(x)
    y2= [i**2 for i in y]
    
    
    fig = plt.figure()
    ax  = fig.add_subplot(111)
    
    ax.plot(x,y,'b')
    
    ### sum
    ysum = y
    
    rng_Start = 2; rng_End = 10
#     rng_Start = 2; rng_End = 6
    
    for index in np.arange(rng_Start, rng_End):
#     for index in np.arange(2,4):
#     for index in np.arange(2,3):
#     for index in (2,2):
#     for index in (2, 3):
#     for index in (1,2):
#     for index in (1,2,3):
#     for index in (1,2,3,4):

        y_ = [i ** index for i in y]
        
        ysum = ysum + y_
#         ysum = y_
#         ysum += y_
        
        ax.plot(x, ysum)
        
        print()
        print("[%s:%d] index => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , index
            ), file=sys.stderr)
        
    #/for index in (1,2,3,4):

    
#     ax.plot(x,y2,'g')
#     ax.plot(x,y + y2,'r')
#     ax.plot(x,y,'b.')
    
#     y_pi   = y/np.pi
#     unit   = 0.25
#     y_tick = np.arange(-0.5, 0.5+unit, unit)
#     
    '''###################
        label : y
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_Y = 1
#     tickVal_X = 1
    
    y_tick = np.arange(-2, rng_End + tickVal_Y, tickVal_Y)
#     x_tick = np.arange(-2, 2, 1)
    
    y_label = y_tick
#     y_label = [r"$" + format(r, ".2g")+ r"\pi$" for r in y_tick]
    
    ax.set_yticks(y_tick)
#     ax.set_yticks(y_tick * np.pi)
    
    ax.set_yticklabels(y_label, fontsize = 10)
    
    '''###################
        label : x
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_X = 0.5
#     tickVal_X = 1
    
    x_tick = np.arange(- rng_X_Scalar, rng_X_Scalar + tickVal_X, tickVal_X)
#     x_tick = np.arange(-2, 2 + tickVal_X, tickVal_X)
#     x_tick = np.arange(-2, 2, 1)
    
    x_label = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]
    
    ax.set_xticks(x_tick * np.pi)
    
    ax.set_xticklabels(x_label, fontsize = 10)
    
    
#     x_label = np.arange(-10 / np.pi, 10 / np.pi, np.pi / 2)
# #     x_label = np.arange(-np.pi * 3, np.pi * 3, np.pi / 2)
#     
#     x_label_pi = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_label]
#     
#     ax.set_xticks(x_label)
#     
#     ax.set_xticklabels(x_label_pi, fontsize = 10)
#     
# #     x_label_pi = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
#     
#     '''###################
#         label : y        
#     ###################'''
#     y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
#     ax.set_yticks(y_tick*np.pi)
#     ax.set_yticklabels(y_label, fontsize=20)
#     
#     y_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in y_tick]
#     ax2 = ax.twinx()
#     ax2.set_yticks(y_tick*np.pi)
#     ax2.set_yticklabels(y_label2, fontsize=20)
    fpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
            + "\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1" \
            + "\\6_1.%s.png" % (libs.get_TimeLabel_Now())
            
    print()
    print("[%s:%d] fpath_Out => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Out
        ), file=sys.stderr)
    
    '''###################
        title
    ###################'''
    plt.title("sin(x)^a : a = %02d ~ %02d\n%s" \
                % (rng_Start, (rng_End - 1), os.path.basename(fpath_Out)))
    '''###################
        grid        
    ###################'''
    plt.grid(b=None, which='major', axis='both')
    
    '''###################
        plot        
    ###################'''
#     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
    plt.savefig(fpath_Out)
    
#     plt.savefig("%s\\6_1.%s.png" % (dpath_Out, libs.get_TimeLabel_Now()))
    
    plt.show()
    
#/def test_4():

def test_3():

    '''###################
        plot        
    ###################'''
    x=np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    y=np.sin(x)
    y2= [i**2 for i in y]
    
    
    fig = plt.figure()
    ax  = fig.add_subplot(111)
    
    ax.plot(x,y,'b')
    ax.plot(x,y2,'g')
    ax.plot(x,y + y2,'r')
#     ax.plot(x,y,'b.')
    
#     y_pi   = y/np.pi
#     unit   = 0.25
#     y_tick = np.arange(-0.5, 0.5+unit, unit)
#     
    '''###################
        label : x
    ###################'''
    #ref https://stackoverflow.com/questions/10729737/how-can-i-set-the-y-axis-in-radians-in-a-python-plot
    tickVal_X = 0.5
#     tickVal_X = 1
    
    x_tick = np.arange(-2, 2 + tickVal_X, tickVal_X)
#     x_tick = np.arange(-2, 2, 1)
    
    x_label = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_tick]
    
    ax.set_xticks(x_tick * np.pi)
    
    ax.set_xticklabels(x_label, fontsize = 10)
    
    
#     x_label = np.arange(-10 / np.pi, 10 / np.pi, np.pi / 2)
# #     x_label = np.arange(-np.pi * 3, np.pi * 3, np.pi / 2)
#     
#     x_label_pi = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_label]
#     
#     ax.set_xticks(x_label)
#     
#     ax.set_xticklabels(x_label_pi, fontsize = 10)
#     
# #     x_label_pi = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
#     
#     '''###################
#         label : y        
#     ###################'''
#     y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
#     ax.set_yticks(y_tick*np.pi)
#     ax.set_yticklabels(y_label, fontsize=20)
#     
#     y_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in y_tick]
#     ax2 = ax.twinx()
#     ax2.set_yticks(y_tick*np.pi)
#     ax2.set_yticklabels(y_label2, fontsize=20)
    fpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
            + "\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1" \
            + "\\6_1.%s.png" % (libs.get_TimeLabel_Now())
            
    print()
    print("[%s:%d] fpath_Out => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Out
        ), file=sys.stderr)
    
    '''###################
        grid        
    ###################'''
    plt.grid(b=None, which='major', axis='both')
    
    '''###################
        plot        
    ###################'''
#     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
    plt.savefig(fpath_Out)
    
#     plt.savefig("%s\\6_1.%s.png" % (dpath_Out, libs.get_TimeLabel_Now()))
    
    plt.show()
    
#/def test_4():

def test_2():

    '''###################
        plot        
    ###################'''
    x=np.arange(-10.0,10.0,0.1)
    y=np.arctan(x)
    
    fig = plt.figure()
    ax  = fig.add_subplot(111)
    
    ax.plot(x,y,'b.')
    
    y_pi   = y/np.pi
    unit   = 0.25
    y_tick = np.arange(-0.5, 0.5+unit, unit)
    
    '''###################
        label : x
    ###################'''
    x_label = np.arange(-10 / np.pi, 10 / np.pi, np.pi / 2)
#     x_label = np.arange(-np.pi * 3, np.pi * 3, np.pi / 2)
    
    x_label_pi = [r"$" + format(r, ".2g")+ r"\pi$" for r in x_label]
    
    ax.set_xticks(x_label)
    
    ax.set_xticklabels(x_label_pi, fontsize = 10)
    
#     x_label_pi = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
    
    '''###################
        label : y        
    ###################'''
    y_label = [r"$-\frac{\pi}{2}$", r"$-\frac{\pi}{4}$", r"$0$", r"$+\frac{\pi}{4}$",   r"$+\frac{\pi}{2}$"]
    ax.set_yticks(y_tick*np.pi)
    ax.set_yticklabels(y_label, fontsize=20)
#     
#     y_label2 = [r"$" + format(r, ".2g")+ r"\pi$" for r in y_tick]
#     ax2 = ax.twinx()
#     ax2.set_yticks(y_tick*np.pi)
#     ax2.set_yticklabels(y_label2, fontsize=20)
    fpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
            + "\\VX7GLZ_science-research\\27_math\\27_6_plot\\_1" \
            + "\\6_1.%s.png" % (libs.get_TimeLabel_Now())
            
    print()
    print("[%s:%d] fpath_Out => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Out
        ), file=sys.stderr)
    
    '''###################
        grid        
    ###################'''
    plt.grid(b=None, which='major', axis='both')
    
    '''###################
        plot        
    ###################'''
#     ax.savefig("%s\\6_1.%s.png" % (fpath_Out, libs.get_TimeLabel_Now()))
    plt.savefig(fpath_Out)
    
#     plt.savefig("%s\\6_1.%s.png" % (dpath_Out, libs.get_TimeLabel_Now()))
    
    plt.show()
    
#/def test_4():

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
    test_5_3()
#     test_5_2()
#     test_5()
#     test_4()
#     test_3()
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



