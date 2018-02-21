#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
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
import cmd

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
import getopt, inspect, struct, random, glob
import xml.etree.ElementTree as ET, math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.patches as mpatches
from shutil import copyfile
from scipy.stats.stats import pearsonr


def build_Video_From_PNGFiles \
(dpath_Full, fpath_Glob, fpath_In_FFMpeg, fpath_Out_FFMpeg):
    
    '''###################
        file path        
    ###################'''
    PROJECT_ROOT = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\1_\\_17"
    
    dpath_Out = "%s\\data_1_17.1" % (PROJECT_ROOT)
    
    ### fpath full
    tlabel = libs.get_TimeLabel_Now()
    
    session_Label = "1_17.1.test-3"
    
#     fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)
    
    '''###################
        test : video        
    ###################'''
    '''###################
        get : file list        
    ###################'''
    dname_Images = "images"
    
#     dpath_Full = "%s\\images_20180220_141141" % (dpath_Out)
#     dpath_Full = "%s\\%s\\images_20180220_141141" % (dpath_Out, dname_Images)
    
    ### validate
    if not os.path.isdir(dpath_Full) : #if os.path.isdir(dpath_Full)
    
        print()
        print("[%s:%d] dir NOT exist => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Full
        ), file=sys.stderr)
        
        return
        
    #/if os.path.isdir(dpath_Full)
    
#     fpath_Glob = "%s\\*(*).png" % (dpath_Full)
#     fpath_Glob = "%s\\*.png" % (dpath_Full)

    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    ### validate
    if len(lo_Files) < 1 : #if len(lo_Files) < 1

        print()
        print("[%s:%d] len(lo_Files) => less than 1" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files), fpath_Glob
            ), file=sys.stderr)
        
        return
    
    else :
        
        print()
        print("[%s:%d] len(lo_Files) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files)
            ), file=sys.stderr)
    #/if len(lo_Files) < 1

    '''###################
        sort : list        
    ###################'''
    #ref https://www.programiz.com/python-programming/methods/list/sort
    lo_Files.sort()
    
#     for item in lo_Files:
#     
#         print("[%s:%d] item => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , item
#             ), file=sys.stderr)
#         
#         print()
        
    #/for item in lo_Files:
    
    '''###################
        copy        
    ###################'''
    cnt = 0
    
    lo_CopiedFiles = []
    
    for item in lo_Files:
     
        dpath = os.path.dirname(item)
         
        fpath_Dst = "%s\\image.%03d.png" % (dpath, cnt)
         
         
         
        copyfile(item, fpath_Dst)
        
        # append new file path
        lo_CopiedFiles.append(fpath_Dst)
         
        print()
        print("[%s:%d] file copied : %s => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , item, fpath_Dst
                ), file=sys.stderr)
        
        # increment
        cnt += 1
        
    #/for item in lo_Files:

    '''###################
        video : generate        
    ###################'''
    dpath_In = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research" \
            + "\\28_Physics\\1_\\_17\\data_1_17.1" \
            + "\\images\\images_20180220_141141"
            
#     fpath_In = "%s\\image.%%03d.png" % (dpath_In)
#     fpath_In = "%s\\image.%03d.png" % (dpath_In)
    
#     fpath_Out = "%s\\movie.%s.mp4" % (dpath_In, libs.get_TimeLabel_Now())
    

    cmd = "ffmpeg -f image2 -r 2 -i " \
            + "%s -vcodec mpeg4 -y %s" % (fpath_In_FFMpeg, fpath_Out_FFMpeg)
#             + "%s -vcodec mpeg4 -y %s" % (fpath_In, fpath_Out)
#     cmd = "ffmpeg -f image2 -r 2 -i image.%03d.png -vcodec mpeg4 -y movie.mp4"

    # execute
    os.system(cmd)
    
    print()
    print("[%s:%d] executing command => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , cmd
        ), file=sys.stderr)

    '''###################
        delete : copied files        
    ###################'''
    while (not os.path.isfile(fpath_Out_FFMpeg)) :
        
        pass
    
    #/while (not os.path.isfile(fpath_Out)) :

    print()
    print("[%s:%d] copied files ==> deleting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    # remove files
    for item in lo_CopiedFiles:
    
        if os.path.isfile(item) : #if os.path.isfile(item)
    
            res = os.remove(item)
            
            print()
            print("[%s:%d] remove file : result => %s (%s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , res, item
                    ), file=sys.stderr)
            
        #/if os.path.isfile(item)
    
    print()
    print("[%s:%d] copied files ==> deleted" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)    
        
    #/for item in lo_CopiedFiles:

'''###################
    @return: 
        -1    glob ==> returned less than 1
        0     video ==> generated
###################'''
def build_Video_From_PNGFiles__V2 \
(fpath_Glob, fpath_In_PNGFiles, fpath_Out_FFMpeg):
    
    '''###################
        file path        
    ###################'''

    '''###################
        png files        
    ###################'''
    #ref glob https://stackoverflow.com/questions/14798220/how-can-i-search-sub-folders-using-glob-glob-module-in-python answered Feb 10 '13 at 13:31    
    lo_Files = glob.glob(fpath_Glob)
    
    ### validate
    if len(lo_Files) < 1 : #if len(lo_Files) < 1

        print()
        print("[%s:%d] len(lo_Files) => less than 1" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files), fpath_Glob
            ), file=sys.stderr)
        
        return -1
    
    else :
        
        print()
        print("[%s:%d] len(lo_Files) => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(lo_Files)
            ), file=sys.stderr)
    #/if len(lo_Files) < 1

    '''###################
        sort : list        
    ###################'''
    #ref https://www.programiz.com/python-programming/methods/list/sort
    lo_Files.sort()
    
    '''###################
        copy        
    ###################'''
    cnt = 0
    
    lo_CopiedFiles = []
    
    for item in lo_Files:
     
        dpath = os.path.dirname(item)
         
        fpath_Dst = "%s\\image.%03d.png" % (dpath, cnt)
         
         
         
        copyfile(item, fpath_Dst)
        
        # append new file path
        lo_CopiedFiles.append(fpath_Dst)
         
        print()
        print("[%s:%d] file copied : %s => %s" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , item, fpath_Dst
                ), file=sys.stderr)
        
        # increment
        cnt += 1
        
    #/for item in lo_Files:

    '''###################
        video : generate        
    ###################'''
    cmd = "ffmpeg -f image2 -r 2 -i " \
            + "%s -vcodec mpeg4 -y %s" % (fpath_In_PNGFiles, fpath_Out_FFMpeg)

    # execute
    os.system(cmd)
    
    print()
    print("[%s:%d] executing command => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , cmd
        ), file=sys.stderr)

    '''###################
        delete : copied files        
    ###################'''
    while (not os.path.isfile(fpath_Out_FFMpeg)) :
        
        pass
    
    #/while (not os.path.isfile(fpath_Out)) :

    print()
    print("[%s:%d] copied files ==> deleting..." % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
    
    # remove files
    for item in lo_CopiedFiles:
    
        if os.path.isfile(item) : #if os.path.isfile(item)
    
            res = os.remove(item)
            
            print()
            print("[%s:%d] remove file : result => %s (%s)" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()
                    , res, item
                    ), file=sys.stderr)
            
        #/if os.path.isfile(item)
    
    print()
    print("[%s:%d] copied files ==> deleted" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)    
        
    #/for item in lo_CopiedFiles:

    '''###################
        return        
    ###################'''
    return 0

