# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\10_electromagnetic\1_\10_1.9.py
orig : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\10_electromagnetic\1_\10_1.8.py
at : 2018/05/09 18:04:28

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\10_electromagnetic\1_
python 10_1.9.py

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

from mm.libs_mm import libs

'''###################
    import : built-in modules        
###################'''
import getopt, inspect, struct, random, glob
import math as math, matplotlib.pyplot as plt \
        , numpy as np, matplotlib.lines as mlines
from shutil import copyfile

###############################################
#ref https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib
# def newline(p1, p2):
def newline(p1, p2, ax):
    
#     ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    
    return l

def test_1():
    
    '''###################
        setup        
    ###################'''
    # time label
    tlabel = libs.get_TimeLabel_Now()

    dpath_Images_Out = "C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research" \
                + "\\28_Physics\\10_electromagnetic\\1_\\images\\" \
                + "9_%s" % tlabel
#                 + "9_"
                
    
    # dirs
    if not os.path.isdir(dpath_Images_Out) : os.makedirs(dpath_Images_Out)
    
    #ref https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib
    x = np.linspace(0,5)
#     y = x**2
    
    e = 1
    r = 2
    
    t = np.pi / 4
    
#     A = [0, 0]
# #     B = [0, e]
#     B = [e, 0]
#     C = [r * np.cos(t), r * np.sin(t)]
#     D = [e + r * np.cos(t), r * np.sin(t)]
    
#     print("[%s:%d] D =>" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             
#             ), file=sys.stderr)
#     
#     print(D)
    
    '''###################
        graph setup        
    ###################'''
    plt.grid(b=None, which='major', axis='both')
    
    #ref https://stackoverflow.com/questions/2849286/python-matplotlib-subplot-how-to-set-the-axis-range
    plt.ylim([-3, 3])
#     plt.ylim([-1 * (e * r * 1.5) * 1.0, (e * r * 1.5) * 1.0])
    plt.xlim([-1 * (e * r * 1.5) * 1.0, (e * r * 1.5) * 1.0])
#     plt.ylim([-3, 3])
#     plt.xlim([-1, 3])

    #ref https://stackoverflow.com/questions/4136244/matplotlib-pyplot-how-to-enforce-axis-range
    ax = plt.gca()
    ax.set_autoscale_on(False)

    #ref https://matplotlib.org/examples/pylab_examples/equal_aspect_ratio.html
    # xy ratio ---> equal
#     plt.axes().set_aspect('equal')
#     plt.axes().set_aspect('equal', 'datalim')

    '''###################
        lines        
    ###################'''
    cons_Width = 10
    
#     rng = np.linspace(0, np.pi / 2, 12)
#     rng = np.linspace(0, np.pi, 6)
    rng = np.linspace(0, np.pi / 2, 24)
#     rng = np.linspace(0, np.pi / 2, 12)
#     rng = np.linspace(0, np.pi / 2, 6)
#     rng = np.linspace(0, np.pi / 2, np.pi / 8)
    
    #debug
    print("rng =>")
    print(rng)
#     return
    
    # counter for iteration
    cntOf_Iter = 0
    
    for th in rng :
        
        '''###################
            data        
        ###################'''
        A = [0, 0]
    #     B = [0, e]
        B = [e, 0]
        C = [r * np.cos(th), r * np.sin(th)]
        D = [e + r * np.cos(th), r * np.sin(th)]
        
        E = [0                  , - r * np.cos(th)]
        F = [e                  , - r * np.cos(th)]

        # AC, AB
        x1, y1 = [A[0], C[0], A[0], B[0]], \
                    [A[1], C[1], A[1], B[1]]
        # CD BD
        x2, y2 = [C[0], D[0], B[0], D[0]], \
                    [C[1], D[1], B[1], D[1]]
        # AE
        x3, y3 = [A[0], E[0]], \
                    [A[1], E[1]]
        # BF
        x4, y4 = [B[0], F[0]], \
                    [B[1], F[1]]
        
        # EF
        x5, y5 = [E[0], F[0]], \
                    [E[1], F[1]]
        
    #     x2, y2 = [C[0], D[0]], \
    #                 [C[1], D[1]]
    #     x1, y1 = [-1, 12], [1, 4]
    #     x2, y2 = [1, 10], [3, 2]
        '''###################
            graph        
        ###################'''
        plt.ylim([-3, 3])
    #     plt.ylim([-1 * (e * r * 1.5) * 1.0, (e * r * 1.5) * 1.0])
        plt.xlim([-1 * (e * r * 1.5) * 1.0, (e * r * 1.5) * 1.0])
        
        plt.grid(b=None, which='major', axis='both')
    
        # title
        plt_Title = "theta=%d-over-pi" % (cntOf_Iter)
        
        # increment counter
        cntOf_Iter += 1
#         plt_Title = "theta=%d-over-pi" % (th)
#         plt_Title = "theta = %d / pi" % (th)
#         plt_Title = "theta = %.02f pi" % (th / np.pi)
#         plt_Title = "theta = %.02f pi" % (t / np.pi)
        
        plt.title(plt_Title, fontsize = 15)
        
        plt.axes().set_aspect('equal')
        
#         #ref https://stackoverflow.com/questions/19125722/adding-a-legend-to-pyplot-in-matplotlib-in-the-most-simple-manner-possible
#         plt.legend(loc='upper left')
        
        '''###################
            plot        
        ###################'''
#         handle_AC_AB, = plt.plot(x1, y1, x2, y2, marker = 'o', label='AC AB')
#         handle_AE, = plt.plot(x3, y3, marker = 'o', label='AE')
#         handle_AE, = plt.plot(x3, y3, marker = 'o', label='AE')
#         plt.plot(x4, y4, x5, y5, marker = 'o')
#         plt.plot(x3, y3, x4, y4, x5, y5, marker = 'o')
#         plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, marker = 'o')

#         plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, marker = 'o')
#         plt.plot(x1, y1, x2, y2, x3, y3, marker = 'o')
#         plt.plot(x1, y1, x2, y2, marker = 'o')
        
        plt.plot(x1, y1, marker = 'o', label="AC AB")
        plt.plot(x2, y2, marker = '^', label="CD BD")
        plt.plot(x3, y3, marker = '1', label="AE")
        plt.plot(x4, y4, marker = 's', label="BF")
        plt.plot(x5, y5, marker = 'P', label="EF")
        
#         plt.legend()
        #ref https://qiita.com/okadate/items/00227316187b60f861f5 "枠外に出す"
        plt.legend(bbox_to_anchor=(1.01,1), loc=2, borderaxespad=0)
        
        # legend
        #ref https://matplotlib.org/users/legend_guide.html
#         plt.legend(handles=[handle_AC_AB, handle_AE])
#         plt.legend(handles=[line_up, line_down])
        
        '''###################
            save : image        
        ###################'''
        fname_Images_Out = "image.%s.%s.png" % (tlabel, plt_Title)
        
        fpath_Images_Out = "%s\\%s" % (dpath_Images_Out, fname_Images_Out)
        
        plt.savefig(fpath_Images_Out)
            
            # clear plot
        plt.clf()

#     plt.plot(x1, y1, marker = 'o')
#     plt.plot(x1, y1, x2, y2, marker = 'o')
    
#     plt.plot(A, B, marker = 'o')
#     plt.plot(x1, y1, x2, y2, marker = 'o')
    
    
#     ax = plt.gca()
#     
#     newline(A, B, ax)
#     newline(B, D, ax)
#     newline(C, D)
#     newline(A, C)
    
    
    
#     x = np.linspace(0,10)
#     y = x**2
#     
#     p1 = [1,20]
#     p2 = [6,70]
    
#     plt.plot(x, y)
#     newline(p1,p2)

#     '''###################
#         graph setup        
#     ##################'''
#     plt.grid(b=None, which='major', axis='both')
#     
# #     ref https://stackoverflow.com/questions/2849286/python-matplotlib-subplot-how-to-set-the-axis-range
#     plt.ylim([-3, 3])
#     plt.xlim([-1, 3])


#     #ref https://matplotlib.org/examples/pylab_examples/equal_aspect_ratio.html
#     # xy ratio ---> equal
#     plt.axes().set_aspect('equal', 'datalim')

#     plt.show()
    
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



