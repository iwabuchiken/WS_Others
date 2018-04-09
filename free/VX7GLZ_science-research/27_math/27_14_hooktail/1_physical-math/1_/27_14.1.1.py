# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_14_hooktail\1_physical-math\1_\27_14.1.1.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_6_plot\_1\6_1.py
at : 2018/02/21 10:34:31

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_14_hooktail\1_physical-math\1_\
python 27_14.1.1.py

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

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# 
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects')
sys.path.append('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research')

from libs_VX7GLZ import libs_VX7GLZ
# from libs_27_6_1 import cons_27_6_1

from mm.libs_mm import cons_mm, cons_fx, libs, libfx
# from sympy.matrices import *

'''###################
    import : built-in modules        
###################'''
# import getopt, inspect, struct, random, glob
# import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
#         , numpy as np, matplotlib.patches as mpatches
# from shutil import copyfile
# from scipy.stats.stats import pearsonr

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
    
def _test_6__Params(x = 1, y = 0):
    
#     step_Theta = np.pi / 3
    step_Theta = np.pi / 12
#     step_Theta = np.pi / 6
     
    rng_Theta = np.arange(0, np.pi * 2, step_Theta)
#     rng_Theta = np.arange(0, np.pi * 2 + step_Theta, step_Theta)
    
#     rot = Matrix([
#             [np.cos(rng_Theta), - np.sin(rng_Theta)], 
#              [np.sin(rng_Theta), np.cos(rng_Theta)]]
#     )

    ### 
#     x = 1; y = 0
    
#     r_ = []
    x_ = []
    y_ = []
    
    for item in rng_Theta:

#         rot = [
#                 [np.cos(rng_Theta), - np.sin(rng_Theta)], 
#                  [np.sin(rng_Theta), np.cos(rng_Theta)]
#          ]
        
        a = 1
#         a = 2
        
        rot = Matrix([
                [np.cos(item), - np.sin(item) * a], 
                 [np.sin(item) * a, np.cos(item)]]
#                 [np.cos(item), - np.sin(item)], 
#                  [np.sin(item), np.cos(item)]]
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

def _test_5__Params():
    
#     step_Theta = np.pi / 3
    step_Theta = np.pi / 12
#     step_Theta = np.pi / 6
     
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
def test_1():

    pass
    
#/def test_1():


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



