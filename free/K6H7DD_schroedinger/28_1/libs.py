import inspect

def linenum(depth=0):
#     print "line"
    
    frame = inspect.currentframe(depth+1)
    return frame.f_lineno

def thisfile(depth=0):
# def _file(depth=0):
#     print "line"
    
    frame = inspect.currentframe(depth+1)
    return frame.f_code.co_filename
