'''###################
    file : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_\test.py        
    
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_
test.py

    
###################'''

########################### imports
import sys

########################### funcs
def test_1():
    
    '''###################
        test : open mm file        
    ###################'''
    fpath_In = "C:/WORKS_2/WS/FM_2_20171104_225946/Materials_Science/test.mm"
    
    f_In = open(fpath_In, "r")
    
    msg = f_In.close()
    
#     msg = "test_1 : %s" % (fpath_In)
    
    print(sys.argv)
#     print(msg + " : " + sys.argv)
    
    return msg
#/def test_1():


res = test_1()

# exit(res)
