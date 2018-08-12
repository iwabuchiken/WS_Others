# -*- coding: utf-8 -*-
'''
file : C:\WORKS_2\WS\WS_Others\JVEMV6\tasks_20180811_100035\1_1.py
orig : C:\WORKS_2\WS\WS_Others.Art\JVEMV6\46_art\VIRTUAL\Admin_Projects\ip\data\ops\1_1.py
at : 2018/06/30 09:32:18

r w && r d3
pushd C:\WORKS_2\WS\WS_Others\JVEMV6\tasks_20180811_100035
python 1_1.py

'''
###############################################
import sys
from distutils import text_file
# from pandas.compat import str_to_bytes
# from numpy.distutils.from_template import item_re
#ref https://stackoverflow.com/questions/3129322/how-do-i-get-monitor-resolution-in-python
# from win32api import GetSystemMetrics
# from matplotlib import pylab as plt

'''###################
    import : original files        
###################'''
sys.path.append('.')
sys.path.append('..')
# sys.path.append('C:\\WORKS_2\\WS\\WS_Others.Art\\JVEMV6\\46_art\\VIRTUAL\\Admin_Projects') # libs_mm

import libs

'''###################
    import : built-in modules        
###################'''
# import getopt
import os
# import inspect

# import math as math

###############################################
def show_Message() :
    
    msg = '''
    <Options>
    -v	Volume down the amplitude --> 1.0 * v / 1000
    -f	Base frequency ---> e.g. 262 for the A tone
    -p	Phase of the sine curves ---> sin(2 * np.pi * f0 * n * phase / fs)'''
    
    print (msg)

def test_1():

    '''######################################
        ops        
    ######################################'''
    # file
    dpath_Tasks = "C:\\WORKS_2\\WS\\WS_Others\\JVEMV6\\tasks_20180811_100035"
#     C:\WORKS_2\WS\WS_Others\JVEMV6\tasks_20180811_100035
    
    fname_Tasks = "tasks.20180811_100146.txt"
    
    # open
    fpath_Tasks = os.path.join(dpath_Tasks, fname_Tasks)
    
    fin_Tasks = open(fpath_Tasks, "r")
    
    text = fin_Tasks.readlines()
    
    print(text)
    
    #debug
    for line in text: print(line)
        

#     print(text)
    
    # strip white chars
    text_Strip = []
    
    # strip
    for line in text:
        
        text_Strip.append(line.strip())
        
    # ends with "\t*"
    text_Final = []
    
    for line in text_Strip:
        
        print("[%s:%d] line is '%s'" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , line
            ), file=sys.stderr)
        
        #if line.endswith("\t*") : #if line.endswith("\t*")
        if line.endswith("\td") : #if line.endswith("\t*")
            
            print("[%s:%d] ==> ends with \\t*" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                
                ), file=sys.stderr)
            
            # append
            text_Final.append(line.strip())
            
        #/if line.endswith("\t*")
    
    
#         text_Strip.append(line.strip())
#         text_Strip.append(line.strip())
        
    #/for line in text_Strip:

    
    fin_Tasks.close()

    print()
    print("[%s:%d] lines =>" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print(text_Strip)
    for line in text_Final: print(line)
#     for line in text_Strip: print(line)

    '''###################
        write to file
    ###################'''
    time_Label = libs.get_TimeLabel_Now()
    
    fname_Final = "tasks.final.%s.txt" % (time_Label)
    
    fpath_Final = os.path.join(dpath_Tasks, fname_Final)
    
    fout = open(fpath_Final, "w")
    
    # sum
    fout.write("num of tasks\t%d" % len(text_Final))
    fout.write("\n")
    
    for line in text_Final:
        
        # build line
        tokens = line.split("\t")
        
        #tokens_sub = tokens[:-2]
        tokens_sub = tokens[:3]
        
        tokens_sub.append(time_Label)
        
        line_Final = "\t".join(tokens_sub)
        
        fout.write(line_Final)
#         fout.write(line)
        fout.write("\n")
        
    #/for line in text_Final:
    
    fout.close()
    
    print("[%s:%d] file written => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , fpath_Final
            ), file=sys.stderr)
    
    '''###################
        message
    ###################'''
    print()
    print("[%s:%d] test_1 =======================" % \
                    (os.path.basename(libs.thisfile()), libs.linenum()

                    ), file=sys.stderr)
#/ def test_1():

def exec_prog():
    
    '''###################
        ops        
    ###################'''
    test_1()
    
    print("[%s:%d] exec_prog() => done (time = %s)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , libs.get_TimeLabel_Now()
            ), file=sys.stderr)
    
#def exec_prog()

'''
<usage>
test_1.py [-fXXX]  #=> frequency
test_1.py -f402
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
    
    print("[%s:%d] done" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            
            ), file=sys.stderr)
#     print "[%s:%d] done" % (thisfile(), linenum())
