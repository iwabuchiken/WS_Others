# -*- coding: utf-8 -*-
'''###################
    file    : C:\WORKS_2\WS\WS_Others\free\fx\82_\82_6\cp_log.py
    at      : 2018/01/16 10:52:36
    
    <Usage>
    cp_log.py
    
        ==> change "tmp.log" file name to "tmp.XXXX.log"
            --> XXXX is a time stamp(serial format)
###################'''

import os
import sys
import inspect
from time import gmtime, strftime, localtime, time

from shutil import copyfile

import getopt as go

sys.path.append('.')
sys.path.append('..')

import libs
# from libs import libs


def linenum(depth=0):
#     print "line"
    
    #ref https://stackoverflow.com/questions/6810999/how-to-determine-file-function-and-line-number 'answered Jul 25 '11 at 1:31'
    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                        # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
#     return info.filename                       # __FILE__     -> Test.py
    #     print info.filename                       # __FILE__     -> Test.py
    #     print info.function                       # __FUNCTION__ -> Main
    #     print info.lineno                         # __LINE__     -> 13
    return info.lineno                         # __LINE__     -> 13

    
    '''
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno
    
    '''

def thisfile(depth=0):
# def _file(depth=0):
#     print "line"

    callerframerecord = inspect.stack()[1]    # 0 represents this line
                                            # 1 represents line at caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    return info.filename                       # __FILE__     -> Test.py
#     print info.filename                       # __FILE__     -> Test.py
#     print info.function                       # __FUNCTION__ -> Main
#     print info.lineno                         # __LINE__     -> 13
    
    '''    
        frame = inspect.currentframe(0)
    #     frame = inspect.currentframe(depth+1)
        
        return os.path.basename(frame.f_code.co_filename)
    #     return frame.f_code.co_filename
    '''
#/def thisfile(depth=0):

def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
#     str = strftime("%Y%m%d_%H%M%S", t)
#     str = strftime("%Y%m%d_%H%M%S", localtime())
    str = strftime("%Y%m%d_%H%M%S", localtime(t))
    
    #ref https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python "answered May 13 '11 at 22:21"
    if mili == True :

        #ref decimal value https://stackoverflow.com/questions/30090072/get-decimal-part-of-a-float-number-in-python "answered May 7 '15 at 1:56"          
        str = "%s_%03d" % (str, int(t % 1 * 1000))
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():

# def exec_prog(label="nolabel"):
def exec_prog(label = None):
    
    '''###################
        validate : label        
    ###################'''
    if label == None : #if label == None

        label = "nolabel"
        
    #/if label == None
    

    
    fname_In = "tmp.log"
    
    fname_Out = "tmp" + "." \
                + label + "." \
                + get_TimeLabel_Now() + ".log"
    
    # rename
    # copy file
    copyfile(fname_In, fname_Out)
#     os.rename(fname_In, fname_Out)
    
    print("copy file => done : %s" % (fname_Out))
#     print("rename => done : %s" % (fname_Out))
    
#/exec_prog()



if __name__ == "__main__" :

    '''###################
        validate : help option        
    ###################'''

    '''###################
        prep : option chars        
    ###################'''
#     args = sys.argv[0:]
    args = sys.argv
    
#     print(args)
#     print()
    
    ### validate : length
    if len(args) < 2 : #if len(args) < 2
    
        print()
        print ("[%s:%d] args not enough! => len(args) = %d \n'%s'" % \
               (os.path.basename(libs.thisfile()), libs.linenum(), len(args), args))
    
        exit()
        
    #/if len(args) < 2
    
    '''###################
        get options        
    ###################'''
    keychars = None
#     keychars = "lm"
#     keychars = "l"
    result = libs.get_opt_2(sys.argv)
#     result = libs.get_opt_2(sys.argv, keychars)
#     result = libs.get_opt_2(sys.argv, args[1])
#     result = libs.get_opt_2(sys.argv, "abc")
     
#     print()
#     print(result)
#     print()

#     exit()

    '''###################
        get : label string        
    ###################'''
    label = ""
    
    #ref in https://stackoverflow.com/questions/1323410/has-key-or-in "answered Aug 24 '09 at 22:11"
    if '-l' in result : #if not result['-l'] == None
#     if not result.has_key('-l') == None : #if not result['-l'] == None

        label = result['-l']
    
    else : #if not result['-l'] == None
    
        label = None
    
    #/if not result['-l'] == None
    
    print()
    print ("[%s:%d] label => '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), label))

    '''###################
        execute        
    ###################'''
    exec_prog(label)
#     exec_prog()

    print()
    
    print ("[%s:%d] all done" % (os.path.basename(os.path.basename(thisfile())), linenum()))


#####################################/EOF