# -*- coding: utf-8 -*-
'''
C:\WORKS_2\WS\WS_Others\prog\D-7\2_
python 1_1.py

82_6.py > tmp.log
cp_log.py

82_6.py > tmp.log && cp_log.py
1_1.3.py > tmp.log && python C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\cp_log.py -ladd-attribute-CREATED

ref : http://aidiary.hatenablog.com/entry/20110607/1307449007

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_
python 1_1.3.py created > tmp.log && python C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\cp_log.py -ladd-attrib-created

pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\31_Materials\1_
python 1_1.3.py numbering > tmp.log && python C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\cp_log.py -ladd-numbering-through

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

from libs_D_7 import cons_D_7
# from libs_31 import libmt

import getopt
import os
import inspect

import math as math

import struct

from shutil import copyfile

import xml.etree.ElementTree as ET

###############################################
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
    
#     '''###################
#         params        
#     ###################'''
#     args = sys.argv
#     
#     if len(args) < 2 : #if len(args) < 2
# 
#         print()
#         print ("[%s:%d] param needed : len(args) = %d" % \
#                (os.path.basename(libs.thisfile()), libs.linenum(), len(args)))
#                
#         print()
#         print("<Usage> python 1_1.3.py <numbering|created>")
#         
#         return
#     
#     param = args[1]
#     
#     print()
#     print("param => %s" % (param))
#     
# 
#     #/if len(args) < 2
# 
#     '''###################
#         dispatch        
#     ###################'''
#     if param == "numbering" : #if param == "numbering"
# 
#         test_5__Numbering()
#     
#     elif param == "created" : #if param == "numbering"
#         
#         test_4()
#         
#     else : #if param == "numbering"
#     
#         print()
#         print ("[%s:%d] unknown param => '%s'" % \
#                (os.path.basename(libs.thisfile()), libs.linenum(), param))
#     
#         print()
#     
#         return
    
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

