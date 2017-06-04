import inspect
import os

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
from __builtin__ import str

def linenum(depth=0):
#     print "line"
    
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno

def thisfile(depth=0):
# def _file(depth=0):
#     print "line"
    
    frame = inspect.currentframe(depth+1)
    
    return os.path.basename(frame.f_code.co_filename)
#     return frame.f_code.co_filename

def get_opt(arg_ary):
    
#     print "[%s:%d] args =>" % (thisfile(), linenum())
    
#     print arg_ary
    
    # validate
    if len(arg_ary) < 1 :
        
        print "[%s:%d] no args" % (thisfile(), linenum())
        
        return (None, None)
    
    # return tuple
    result = []
    # loop
    for elem in arg_ary :
        
        #ref https://www.tutorialspoint.com/python/string_startswith.htm
        if elem.startswith('-E') and len(elem) > 2 :
            
            #ref append https://stackoverflow.com/questions/1878470/add-tuple-to-list-of-tuples-in-python
            #ref slice http://www.pythonweb.jp/tutorial/string/index11.html
            result.append(('-E', elem[2:]))
    
    return result

'''
    @param string_type
            serial    "20160604_1934"
'''
def get_TimeLabel_Now(string_type="serial", mili=False):
# def get_TimeLabel_Now(string_type="serial"):
    
    t = time()
    
    str = strftime("%Y%m%d_%H%M%S", localtime())
    
#     if mili == True :
#         
#         str += 
    
    return str
    
    #ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
#     return strftime("%Y%m%d_%H%M%S", localtime())
#     return strftime("%Y%m%d_%H%M%S", gmtime())
    
#]]get_TimeLabel_Now():