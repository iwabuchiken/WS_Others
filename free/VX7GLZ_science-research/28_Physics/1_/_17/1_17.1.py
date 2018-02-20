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

###############################################

def test_3():
    
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
    dpath_Full = "%s\\%s\\images_20180220_141141" % (dpath_Out, dname_Images)
    
    ### validate
    if not os.path.isdir(dpath_Full) : #if os.path.isdir(dpath_Full)
    
        print()
        print("[%s:%d] dir NOT exist => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Full
        ), file=sys.stderr)
        
        return
        
    #/if os.path.isdir(dpath_Full)
    
    
    
    fpath_Glob = "%s\\*(*).png" % (dpath_Full)
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
     
    for item in lo_Files:
     
        dpath = os.path.dirname(item)
         
        fpath_Dst = "%s\\image.%03d.png" % (dpath, cnt)
         
         
         
        copyfile(item, fpath_Dst)
         
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
            
    fpath_In = "%s\\image.%%03d.png" % (dpath_In)
#     fpath_In = "%s\\image.%03d.png" % (dpath_In)
    
    fpath_Out = "%s\\movie.%s.mp4" % (dpath_In, libs.get_TimeLabel_Now())
    

    cmd = "ffmpeg -f image2 -r 2 -i " \
            + "%s -vcodec mpeg4 -y %s" % (fpath_In, fpath_Out)
#     cmd = "ffmpeg -f image2 -r 2 -i image.%03d.png -vcodec mpeg4 -y movie.mp4"

    # execute
    os.system(cmd)
    
    print()
    print("[%s:%d] executing command => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , cmd
        ), file=sys.stderr)

    '''###################
        copy        
    ###################'''

    
        
def test_2():
    
    '''###################
        file path        
    ###################'''
    PROJECT_ROOT = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\28_Physics\\1_\\_17"
    
    dpath_Out = "%s\\data_1_17.1" % (PROJECT_ROOT)
    
    ### fpath full
    tlabel = libs.get_TimeLabel_Now()
    
    session_Label = "1_17.1"
    
#     fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)
    
    '''###################
        ops        
    ###################'''
    
    x = np.linspace(0, np.pi * 2, 100)
#     x = np.linspace(0, np.pi, 1000)
    
    ### dir path
    dpath_Full = "%s\\images\\images_%s" % (dpath_Out, tlabel)
    ### make dir
    #ref is directory https://stackoverflow.com/questions/82831/how-to-check-whether-a-file-exists answered Sep 17 '08 at 15:01
    if not os.path.isdir(dpath_Full) : os.makedirs(dpath_Full)
#     os.makedirs(dpath_Out)
    
    '''###################
        graph : settings        
    ###################'''
#     # graph : settings
#     plt.ylim(-2,2)
#     plt.xlim(0, np.pi * 2)
#     plt.grid(b=None, which='major', axis='both')
#     plt.xticks(np.arange(0, np.pi*2, np.pi / 4))
#     plt.yticks(np.arange(-2, 2, 0.5))

    
    for index in np.arange(0, 12, 1):
#     for index in np.arange(0, 11, 1):
#     for index in np.arange(0, 20, 1):
        
        # graph : settings
        plt.ylim(-2,2)
        plt.xlim(0, np.pi * 2)
        plt.grid(b=None, which='major', axis='both')
        plt.xticks(np.arange(0, np.pi*2, np.pi / 4))
        plt.yticks(np.arange(-2, 2, 0.5))

        ### fpath
        fpath_Full = "%s\\image.%s.%s.(%02d).png" \
                    % (dpath_Full, session_Label, tlabel, index)

        tick = np.pi / 6 * index
        
        y = np.sin(x + tick)
        
#         # graph : settings
#         plt.ylim(-2,2)
#         plt.xlim(0, np.pi * 2)
#         plt.grid(b=None, which='major', axis='both')
#         plt.xticks(np.arange(0, np.pi*2, np.pi / 4))
#         plt.yticks(np.arange(-2, 2, 0.5))
    #     plt.yticks([-2,-1,1,2])
    #     plt.xticks([-2,-1,1,2])
    
        plt.xlabel("x")
        plt.ylabel("sin(x + %.3f)" % (tick))
        plt.title("x ~ sin(x + a) (index = %d)\n%s" \
                    % (index, os.path.basename(fpath_Full)))
    
        # plot
        plt.plot(x, y)
    
    
        plt.savefig(fpath_Full)

        # clear
#         plt.gcf().clear()
        plt.clf()
        
#     plt.show()
    
#/def test_2():

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



