# -*- coding: utf-8 -*-
'''
pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_
1_1.3.py

82_6.py > tmp.log
cp_log.py

82_6.py > tmp.log && cp_log.py

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

'''

'''
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


import sys
from sympy.solvers.tests.test_constantsimp import C2

import os

sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs
from libs import libfx

from libs import cons
from libs_31 import cons31

import getopt
import os
import inspect

import math as math

import struct

from shutil import copyfile

import xml.etree.ElementTree as ET

###############################################
def test_3():
    
    '''###################
        prep : get root
    ###################'''
    fpath = cons31.FPath.dpath_In_CSV.value \
            + "/" \
            + cons31.FPath.fname_In_XML.value
            
    tree = ET.parse(fpath)
    
    root = tree.getroot()
    
    '''###################
        nodes : g-1        
    ###################'''
    print()
    print ("[%s:%d] root.tag => '%s' / root.attrib => '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum() 
            , root.tag, root.attrib))
    
    g1 = root[0]
    
    print()
    print ("[%s:%d] g1.tag => '%s' / g1.attrib => '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum() 
            , g1.tag, g1.attrib))
    
    '''###################
        nodes : g-2
    ###################'''
    g2 = []

    lenOf_g2 = len(g1)
    
    for i in range(lenOf_g2):
    
        g2.append(g1[i])
        
    #/for i in range(lenOf_g2):

    #debug
    for item in g2:

        for subitem in item:
    
            if subitem.tag == 'attribute' : #if subitem.tag == 'attribute'
            
                item.remove(subitem)
                
                print()
                print ("[%s:%d] item.tag = '%s', subitem.tag = '%s'" % \
                       (os.path.basename(libs.thisfile()), libs.linenum()
                        , item.tag, subitem.tag))
                
            #/if subitem.tag == 'attribute'
        
    #/for subitem in item:

#         attrib_Created = item.get('CREATED')
#         
#         #ref append child https://stackoverflow.com/questions/31259847/python-appending-children-to-an-already-created-xml-files-root-using-xml-dom "answered Jul 8 '15 at 11:26"
#         data2 = ET.Element("attribute"
#                            , {"NAME": "created"
#                              , "VALUE" : attrib_Created
#                              })
        
#         item.remove('attribute')
#         item.append(data2)
        
#         print()
#         print ("[%s:%d] item.tag = '%s' | item.get('CREATED') = '%s'" % \
#                (os.path.basename(libs.thisfile()), libs.linenum()
#                 , item.tag, item.get('CREATED')))

        
    #/for item in g2:
 

    '''###################
        append : child        
    ###################'''
#     #ref https://stackoverflow.com/questions/31259847/python-appending-children-to-an-already-created-xml-files-root-using-xml-dom
#     data1 = ET.Element("node", {"TEXT": "something_" + libs.get_TimeLabel_Now()})
# #     data1 = ET.Element("node", {"TEXT": "something_v001.0002.ma"})
# 
#     data2 = ET.Element("attribute", {"NAME": "created"
#                                      
#                                      , "VALUE" : "18/01/23"
#                                      })
#     
#     data1.append(data2)
#     
#     g2[0].append(data1)
#     
    '''###################
        save xml        
    ###################'''
    label = "remove-attribute-node"
    fpath_Out = "new.%s.%s.mm" % (label, libs.get_TimeLabel_Now())
    
    tree.write(fpath_Out)
    
    print()
    print ("[%s:%d] xml => written : %s" % (os.path.basename(libs.thisfile()), libs.linenum(), fpath_Out))

    
#/def test_2():

def test_2():
    
    '''###################
        prep : get root
    ###################'''
    fpath = cons31.FPath.dpath_In_CSV.value \
            + "/" \
            + cons31.FPath.fname_In_XML.value
            
    tree = ET.parse(fpath)
    
    root = tree.getroot()
    
    '''###################
        nodes : g-1        
    ###################'''
    print()
    print ("[%s:%d] root.tag => '%s' / root.attrib => '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum() 
            , root.tag, root.attrib))
    
    g1 = root[0]
    
    print()
    print ("[%s:%d] g1.tag => '%s' / g1.attrib => '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum() 
            , g1.tag, g1.attrib))
    
    '''###################
        nodes : g-2
    ###################'''
    g2 = []

    lenOf_g2 = len(g1)
    
    for i in range(lenOf_g2):
    
        g2.append(g1[i])
        
    #/for i in range(lenOf_g2):

    #debug
    for item in g2:
            
        attrib_Created = item.get('CREATED')
        
        #ref append child https://stackoverflow.com/questions/31259847/python-appending-children-to-an-already-created-xml-files-root-using-xml-dom "answered Jul 8 '15 at 11:26"
        data2 = ET.Element("attribute"
                           , {"NAME": "created"
                             , "VALUE" : attrib_Created
                             })
        
        item.append(data2)
        
#         print()
#         print ("[%s:%d] item.tag = '%s' | item.get('CREATED') = '%s'" % \
#                (os.path.basename(libs.thisfile()), libs.linenum()
#                 , item.tag, item.get('CREATED')))

        
    #/for item in g2:
 

    '''###################
        append : child        
    ###################'''
#     #ref https://stackoverflow.com/questions/31259847/python-appending-children-to-an-already-created-xml-files-root-using-xml-dom
#     data1 = ET.Element("node", {"TEXT": "something_" + libs.get_TimeLabel_Now()})
# #     data1 = ET.Element("node", {"TEXT": "something_v001.0002.ma"})
# 
#     data2 = ET.Element("attribute", {"NAME": "created"
#                                      
#                                      , "VALUE" : "18/01/23"
#                                      })
#     
#     data1.append(data2)
#     
#     g2[0].append(data1)
#     
    '''###################
        save xml        
    ###################'''
    label = "add_Attrib_Created"
    fpath_Out = "new.%s.%s.mm" % (label, libs.get_TimeLabel_Now())
    
    tree.write(fpath_Out)
    
    print()
    print ("[%s:%d] xml => written : %s" % (os.path.basename(libs.thisfile()), libs.linenum(), fpath_Out))

    
#/def test_2():

def exec_prog(): # from : 
    
    test_3()
#     test_2()
    
#     '''###################
#         prep        
#     ###################'''
#     fpath = cons31.FPath.dpath_In_CSV.value \
#             + "/" \
#             + cons31.FPath.fname_In_XML.value
#             
#     tree = ET.parse(fpath)
#     
#     root = tree.getroot()
#     
#     #debug
#     print()
#     print ("[%s:%d] root => %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum(), root))
#     
#     '''###################
#         nodes : g-1        
#     ###################'''
#     print()
#     print ("[%s:%d] root.tag => '%s' / root.attrib => '%s'" % \
#            (os.path.basename(libs.thisfile()), libs.linenum() 
#             , root.tag, root.attrib))
#     
#     g1 = root[0]
#     
#     print()
#     print ("[%s:%d] g1.tag => '%s' / g1.attrib => '%s'" % \
#            (os.path.basename(libs.thisfile()), libs.linenum() 
#             , g1.tag, g1.attrib))
#     
#     g2 = []
#     
#     lenOf_g2 = len(g1)
#     
#     for i in range(lenOf_g2):
#     
#         g2.append(g1[i])
#         
#     #/for i in range(lenOf_g2):
# 
#     print()
#     print ("[%s:%d] g2 => %s" % \
#            (os.path.basename(libs.thisfile()), libs.linenum(), g2))
#     
#     '''###################
#         report : g2        
#     ###################'''
#     for i in range(lenOf_g2):
#     
#         node = g2[i]
#         
#         print ("[%s:%d] g2[%d] => %s" % \
#                (os.path.basename(libs.thisfile()), libs.linenum()
#                 , i, node.attrib))
#                 #         [1_1.3.py:108] g2 => [<Element 'node' at 0x0000000007E1EA48>, <Element 'node' at
#                 #  0x0000000007E22138>, <Element 'node' at 0x0000000007E22368>]
#     #/for node in g2:
#     
#     '''###################
#         append : child        
#     ###################'''
#     #ref https://stackoverflow.com/questions/31259847/python-appending-children-to-an-already-created-xml-files-root-using-xml-dom
#     data1 = ET.Element("node", {"TEXT": "something_" + libs.get_TimeLabel_Now()})
# #     data1 = ET.Element("node", {"TEXT": "something_v001.0002.ma"})
# 
#     data2 = ET.Element("attribute", {"NAME": "created"
#                                      
#                                      , "VALUE" : "18/01/23"
#                                      })
#     
#     data1.append(data2)
#     
#     g2[0].append(data1)
#     
#     '''###################
#         save xml        
#     ###################'''
#     fpath_Out = "new.%s.mm" % (libs.get_TimeLabel_Now())
#     
#     tree.write(fpath_Out)
#     
#     print()
#     print ("[%s:%d] xml => written : %s" % (os.path.basename(libs.thisfile()), libs.linenum(), fpath_Out))
    
    
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

