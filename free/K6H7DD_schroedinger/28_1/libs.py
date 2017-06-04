import inspect
import os

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
