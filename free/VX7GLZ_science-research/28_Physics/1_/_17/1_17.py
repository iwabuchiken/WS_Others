# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17\1_17.py
orig : C:\WORKS_2\WS\WS_Others\prog\D-7\2_2\VIRTUAL\Admin_Projects\others\VX7GLZ\28_physics\1_\_17\1_17.py
at : 2018/02/17 13:57:51

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_17
python 1_17.py

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

###############################################
def test_7():
    
    '''###################
        vars        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\28_Physics\\1_\\_17" \
                + "\\images\\images_%s" % (tlabel)

    ### make dir
    #ref https://www.tutorialspoint.com/python/os_mkdir.htm
    os.makedirs(dpath_Out)

    '''###################
        file path        
    ###################'''
#         dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    session_Label  = "1-17-2.test-7"
    
#     fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)

    tick = 0.01
#     tick = np.pi / 6
    
    rng_X_End = np.pi * (1/2)
    
    x = np.arange(0.0, rng_X_End, tick)
#     x = np.arange(0.0, 2 * np.pi, tick)
#     x = np.arange(0.0, 2, 0.01)
    y1 = np.sin(2*np.pi*x)
    y2 = 1.2*np.sin(4*np.pi*x)
    y3 = 1.2*np.sin(8*np.pi*x)
    
    cnt = 0
    
    tick = np.pi / 12
#     tick = np.pi / 36

    rng_Index_End = np.pi * 4
    
    for index in np.arange(0, rng_Index_End, tick):
#     for index in np.arange(0, np.pi, tick):
#     for index in np.arange(0, np.pi, tick):

        fig, (ax) = plt.subplots(1, 1, sharex=True)
        
        y = 1.2 * np.sin(4 * np.pi * x + index)

        ax.fill_between(x, y1, y)
        
        ax.set_ylabel("sin(2pi*x) / 1.2*sin(4pi*x)")
        
        
        
        '''###################
            save image        
        ###################'''
        fpath_Full = "%s\\image.%s.%s.(%02d).index-%.03f.png" \
                    % (dpath_Out, session_Label, tlabel, cnt, index)
        
        plt.title("1.2 * sin(4pi * x + %.03f" % (index))
            
        plt.savefig(fpath_Full)
        
        plt.close(fig)
        
#         print()
#         print("[%s:%d] fig saved, closed => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , fpath_Full
#         ), file=sys.stderr)
        
        ###  increment
        cnt += 1
        
    #/for ax in to_Axes:
    
#     print(to_Axes)
    
#     plt.show()
    
#     ax1.fill_between(x, 0, y1)
#     ax1.set_ylabel('0/y1')
# #     ax1.set_ylabel('between y1 and 0')
#     
#     ax4.fill_between(x, 0, y2)
#     ax4.set_ylabel('0/y2')
# #     ax4.set_xlabel('x')
#     
#     ax5.fill_between(x, 0, y3)
#     ax5.set_ylabel('0/y3')
# #     ax4.set_xlabel('x')
#     
#     ax2.fill_between(x, y1, 1)
#     ax2.set_ylabel('y1/1')
# #     ax2.set_ylabel('between y1 and 1')
#     
#     ax3.fill_between(x, y1, y2)
#     ax3.set_ylabel('y1/y2')
# #     ax3.set_ylabel('between y1 and y2')
#     ax3.set_xlabel('x')
    
#     # now fill between y1 and y2 where a logical condition is met.  Note
#     # this is different than calling
#     #   fill_between(x[where], y1[where],y2[where]
#     # because of edge effects over multiple contiguous regions.
#     fig, (ax, ax1) = plt.subplots(2, 1, sharex=True)
#     ax.plot(x, y1, x, y2, color='black')
#     ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
#     ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
#     ax.set_title('fill between where')
#     
#     # Test support for masked arrays.
#     y2 = np.ma.masked_greater(y2, 1.0)
#     ax1.plot(x, y1, x, y2, color='black')
#     ax1.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
#     ax1.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
#     ax1.set_title('Now regions with y2>1 are masked')
    
    # This example illustrates a problem; because of the data
    # gridding, there are undesired unfilled triangles at the crossover
    # points.  A brute-force solution would be to interpolate all
    # arrays to a very fine grid before plotting.
    
#     # show how to use transforms to create axes spans where a certain condition is satisfied
#     fig, ax = plt.subplots()
#     y = np.sin(4*np.pi*x)
#     ax.plot(x, y, color='black')
    
#     # use the data coordinates for the x-axis and the axes coordinates for the y-axis
#     import matplotlib.transforms as mtransforms
#     trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
#     theta = 0.9
#     ax.axhline(theta, color='green', lw=2, alpha=0.5)
#     ax.axhline(-theta, color='red', lw=2, alpha=0.5)
#     ax.fill_between(x, 0, 1, where=y > theta, facecolor='green', alpha=0.5, transform=trans)
#     ax.fill_between(x, 0, 1, where=y < -theta, facecolor='red', alpha=0.5, transform=trans)
    
    
#     plt.show()
#     plt.legend(handles=[red_patch])
    
#     plt.savefig(fpath_Full)
    
#     plt.show()
    
#/def test_5():

def test_6():
    
    '''###################
        vars        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\28_Physics\\1_\\_17" \
                + "\\images"

    '''###################
        file path        
    ###################'''
#         dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    session_Label  = "1-17-2.test-5"
    
    fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)

    x = np.arange(0.0, 2, 0.01)
    y1 = np.sin(2*np.pi*x)
    y2 = 1.2*np.sin(4*np.pi*x)
    y3 = 1.2*np.sin(8*np.pi*x)
    
    fig, to_Axes = plt.subplots(5, 1, sharex=True)
#     fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, sharex=True)
#     fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True)
#     fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True)
    
    do_Params = {
        
            0 : (0, y1, "0 / y1"),
            1 : (0, y2, "0 / y2"),
            2 : (0, y3, "0 / y3"),
            3 : (y1, y2, "y1 / y2"),
            4 : (y1, y3, "y1 / y3"),
        
        }
    
    cnt = 0
    
    for ax in to_Axes:

        print(ax)
        print('')

        ax.fill_between(x, do_Params[cnt][0], do_Params[cnt][1])
        ax.set_ylabel("%d / %s" % (cnt, do_Params[cnt][2]))
        
        ###  increment
        cnt += 1
        
    #/for ax in to_Axes:

    
#     print(to_Axes)
    
    plt.show()
    
#     ax1.fill_between(x, 0, y1)
#     ax1.set_ylabel('0/y1')
# #     ax1.set_ylabel('between y1 and 0')
#     
#     ax4.fill_between(x, 0, y2)
#     ax4.set_ylabel('0/y2')
# #     ax4.set_xlabel('x')
#     
#     ax5.fill_between(x, 0, y3)
#     ax5.set_ylabel('0/y3')
# #     ax4.set_xlabel('x')
#     
#     ax2.fill_between(x, y1, 1)
#     ax2.set_ylabel('y1/1')
# #     ax2.set_ylabel('between y1 and 1')
#     
#     ax3.fill_between(x, y1, y2)
#     ax3.set_ylabel('y1/y2')
# #     ax3.set_ylabel('between y1 and y2')
#     ax3.set_xlabel('x')
    
#     # now fill between y1 and y2 where a logical condition is met.  Note
#     # this is different than calling
#     #   fill_between(x[where], y1[where],y2[where]
#     # because of edge effects over multiple contiguous regions.
#     fig, (ax, ax1) = plt.subplots(2, 1, sharex=True)
#     ax.plot(x, y1, x, y2, color='black')
#     ax.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
#     ax.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
#     ax.set_title('fill between where')
#     
#     # Test support for masked arrays.
#     y2 = np.ma.masked_greater(y2, 1.0)
#     ax1.plot(x, y1, x, y2, color='black')
#     ax1.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
#     ax1.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
#     ax1.set_title('Now regions with y2>1 are masked')
    
    # This example illustrates a problem; because of the data
    # gridding, there are undesired unfilled triangles at the crossover
    # points.  A brute-force solution would be to interpolate all
    # arrays to a very fine grid before plotting.
    
#     # show how to use transforms to create axes spans where a certain condition is satisfied
#     fig, ax = plt.subplots()
#     y = np.sin(4*np.pi*x)
#     ax.plot(x, y, color='black')
    
#     # use the data coordinates for the x-axis and the axes coordinates for the y-axis
#     import matplotlib.transforms as mtransforms
#     trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
#     theta = 0.9
#     ax.axhline(theta, color='green', lw=2, alpha=0.5)
#     ax.axhline(-theta, color='red', lw=2, alpha=0.5)
#     ax.fill_between(x, 0, 1, where=y > theta, facecolor='green', alpha=0.5, transform=trans)
#     ax.fill_between(x, 0, 1, where=y < -theta, facecolor='red', alpha=0.5, transform=trans)
    
    
#     plt.show()
#     plt.legend(handles=[red_patch])
    
#     plt.savefig(fpath_Full)
    
#     plt.show()
    
#/def test_5():

def test_5():
    
    '''###################
        vars        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\28_Physics\\1_\\_17" \
                + "\\images"

    '''###################
        file path        
    ###################'''
#         dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    session_Label  = "1-17-2"
    
    fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)

    x = np.arange(0.0, 2, 0.01)
    y1 = np.sin(2*np.pi*x)
    y2 = 1.2*np.sin(4*np.pi*x)
    
    plt.plot(x, y1, label="sin(2πx)")
    plt.plot(x, y2, label="1.2*sin(4πx)")
#     plt.plot(x, y1, label="x and y1")
#     plt.plot(x, y2, label="x and y2")
    
    #ref https://matplotlib.org/users/legend_guide.html
#     plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#     plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#     plt.legend(bbox_to_anchor=(0.5, 1.02, 1., .102), loc=3,
#     plt.legend(bbox_to_anchor=(0.5, 1.02, 0.7, .102), loc=3,
#     plt.legend(bbox_to_anchor=(0., 1.02, 0.3, .102), loc=3,

    _anchor = (.7, 1.)
#     _anchor = (.9, .1)
#     _anchor = (.9, .5)
#     _anchor = (1.05, .5)
#     _anchor = (1.05, 1)
#     _anchor = (0., 1.02, 0.5, .102)
    loc_Legend = 2
#     loc_Legend = "best"
#     loc_Legend = 1
    ncol_Legend = 1
#     ncol_Legend = 2
    
    _borderaxespad = 0.5
    
#     plt.legend(bbox_to_anchor=(0., 1.02, 0.5, .102), loc=1,
    plt.legend(bbox_to_anchor= _anchor, loc= loc_Legend,
            ncol= ncol_Legend, borderaxespad= _borderaxespad)
#            borderaxespad= _borderaxespad)
#            ncol= ncol_Legend, borderaxespad=0.)
#            ncol= ncol_Legend, mode="expand", borderaxespad=0.)
#            ncol=2, mode="expand", borderaxespad=0.)
    
#     plt.plot(x, y1, y2)
#     plt.plot(x, y1)
    
    plt.xlabel("x")
    plt.ylabel("y1")
    plt.title("test_5 : anchor=[%s]\nloc=%s borderaxespad=%.2f" \
                % (
                    ",".join([str(x) for x in _anchor])
                    , str(loc_Legend), _borderaxespad
#                     , loc_Legend
                )
        )
#     plt.title("test_5")
    
#     red_patch = mpatches.Patch(color='red', label='The red data')
#     plt.legend(handles=[red_patch])
    
    plt.savefig(fpath_Full)
    
#     plt.show()
    
#/def test_5():


def test_4():
    
    '''###################
        vars        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\28_Physics\\1_\\_17" \
                + "\\images"

    '''###################
        file path        
    ###################'''
#         dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    session_Label  = "1-17-2"
    
    fpath_Full = "%s\\image.%s.%s.png" % (dpath_Out, session_Label, tlabel)
    
    '''###################
        ops        
    ###################'''
    #ref https://stackoverflow.com/questions/30209187/matplotlib-chart-area-vs-plot-area answered May 13 '15 at 23:00
    x1 = np.random.randint(-5, 5, 50)
    x2 = np.random.randn(20)
    
    fig = plt.figure(figsize=(8,6))  # sets the window to 8 x 6 inches
    
    # left, bottom, width, height (range 0 to 1)
    # so think of width and height as a percentage of your window size
    big_ax = fig.add_axes([0.1, 0.1, 0.8, 0.8]) 
    small_ax = fig.add_axes([0.52, 0.15, 0.3, 0.3]) # left, bottom, width, height (range 0 to 1)
    
    big_ax.fill_between(np.arange(len(x1)), x1, color='blue', alpha=0.3)
#     big_ax.fill_between(np.arange(len(x1)), x1, color='green', alpha=0.3)
    small_ax.stem(x2)
    
    plt.setp(small_ax.get_yticklabels(), visible=False)
    plt.setp(small_ax.get_xticklabels(), visible=False)
#     plt.show()
    
    fig.savefig(fpath_Full)
#     plt.savefig(fpath_Full)
    plt.close(fig)
    
    print()
    print("[%s:%d] file saved : %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , fpath_Full
        ), file=sys.stderr)
    
#/def test_4():

def test_3():
    
    '''###################
        vars        
    ###################'''
    tlabel = libs.get_TimeLabel_Now()
    
    '''###################
        dir        
    ###################'''
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\free" \
                + "\\VX7GLZ_science-research\\28_Physics\\1_\\_17" \
                + "\\images\\\images_%s" % (tlabel)
    
    ### make dir
    #ref https://www.tutorialspoint.com/python/os_mkdir.htm
    os.makedirs(dpath_Out)
    
    print()
    print("[%s:%d] dpath_Out => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , dpath_Out
        ), file=sys.stderr)
    
    #from : C:\WORKS_2\WS\WS_Others\JVEMV6\34\libs\labs.py
    
#     for a in np.arange(1,2):
#     for a in np.arange(1,10, 0.5):
#     for a in np.arange(1,2, 0.1):
#     for a in np.arange(1, 5, 0.1):
    
    maxnum = 30
    
#     tick = np.pi / 60
    tick = np.pi / 30

    ### counter
    cnt = 1
    
    for a in np.arange(0, np.pi * 4, tick):
#     for a in np.arange(0, np.pi * 2, tick):
#     for a in np.arange(0, maxnum, tick):
#     for a in np.arange(0, 10, 0.1):

#         a = 1
        
#         s1 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        s1 = [np.sin(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s1 = [np.sin(x * a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        s2 = [np.cos(x * a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s2 = [np.cos(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s2 = [np.cos(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        
#         s3 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s4 = [np.cos(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
        
#         s2 = [np.sin(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
#         s2 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
    
        '''###################
            file path        
        ###################'''
#         dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
        ### fpath full
        fpath_Full = "%s\\tmp.%s.(%02d).a=%.3f.png" % (dpath_Out, tlabel, cnt, a)
#         fpath_Full = "%s\\tmp.%s.a=%.3f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
#         fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
#         fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
        
        ### increment
        cnt += 1
        
        '''###################
            gca        
        ###################'''
        fig = plt.figure()
        ax = fig.gca()
        ax.set_xticks(np.arange(-1, 1, 0.1))
        ax.set_yticks(np.arange(-1, 1, 0.1))

        
        
        '''###################
            plot
        ###################'''    
        plt.plot(s1, s2)
#         plt.plot(s3, s4)
        
        ### ratio
        #ref https://matplotlib.org/examples/pylab_examples/equal_aspect_ratio.html
        #ref https://stackoverflow.com/questions/7965743/how-can-i-set-the-aspect-ratio-in-matplotlib
#         plt.axes().set_aspect('equal', 'datalim')
        plt.axes().set_aspect('equal')
#         plt.axes().set_aspect(2)
#         plt.set_aspect(2)
        
        #ref https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python answered Nov 21 '11 at 11:00
        
#         fig = plt.figure()
#         ax = fig.gca()
#         ax.set_xticks(np.arange(-1, 1, 0.1))
#         ax.set_yticks(np.arange(-1, 1, 0.1))
        
        plt.grid(b=None, which='major', axis='both')
        
        plt.xlabel("sin(x)")
#         plt.xlabel("sin(x + %.3f)" % a)
        plt.ylabel("cos(x * %.3f)" % a)
#         plt.ylabel("cos(x + %.3f)" % a)
#         plt.ylabel("cos(x)")
        
        plt.title("a = %.3f" % a)
        
#         plt.show()
        plt.savefig(fpath_Full)
        
        
        ### close
        plt.close(fig)
        
#         print()
#         print("[%s:%d] file saved => %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , fpath_Full
#                 ), file=sys.stderr)
    #/for a in np.arange(1,3):


    
#     plt.close(fig)
#     plt.close(fig)
    
#     plt.show()
    
#/def test_2():

def test_2():
    
    #from : C:\WORKS_2\WS\WS_Others\JVEMV6\34\libs\labs.py
    a = 1
    
    s1 = [np.sin(x) for x in np.arange(-np.pi, np.pi, np.pi / 360)]
    s2 = [np.sin(x + a) for x in np.arange(-np.pi, np.pi, np.pi / 360)]

    '''###################
        file path        
    ###################'''
    dpath_Out = "C:\\WORKS_2\\WS\\WS_Others\\prog\\D-7\\2_2\\VIRTUAL\\Admin_Projects\\others\\VX7GLZ\\28_physics\\1_\\_16"
    ### fpath full
    fpath_Full = "%s\\tmp.%s.a=%.1f.png" % (dpath_Out, libs.get_TimeLabel_Now(), a)
    
    '''###################
        plot
    ###################'''    
    plt.plot(s1, s2)
    
    plt.savefig(fpath_Full)

    print()
    print("[%s:%d] file saved => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Full
            ), file=sys.stderr)
    
#     plt.close(fig)
#     plt.close(fig)
    
#     plt.show()
    
#/def test_2():


def exec_prog(): # from : 
    
    '''###################
        ops        
    ###################'''
    test_7()
#     test_6()
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



