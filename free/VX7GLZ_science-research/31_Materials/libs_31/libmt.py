# -*- coding: utf-8 -*-

import inspect
import os

import sys

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
from platform import node
from uuid import _windll_getnode
from matplotlib.pyplot import hist
from _ctypes import sizeof
# from compiler.future import tree

'''###################
    libs : C:\WORKS_2\WS\WS_Others\free\fx\82_\libs\libs.py
###################'''
sys.path.append('.')
sys.path.append('..')
sys.path.append('C:/WORKS_2/WS/WS_Others/free/fx/82_')

from libs import libs

sys.path.append('C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/mm')
from libs_mm import cons_mm

# import libs

import csv
import sys

from libs import cons

from libs_31 import cons31
# import cons31
# import cons

import copy

import numpy

import xml.etree.ElementTree as ET

import datetime

from random import randint

import time

import math

################################################### funcs
def add_Created(node):
    
    lenOf_Node = len(node)
    
    if lenOf_Node > 0 :
        
        for item in node:

            add_Created(item)
            
        #/for item in node:

        
#         node = add_Created(node)
    
    ### add created
    created = node.get('CREATED')
    
    '''###################
        judge : node is "arrowlink" ?
    ###################'''
    if not created == None : #if not created == None
    
#         time_float = float(created)
        
        s = float(created) / 1000.0
        
        stamp = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S.%f')
#         stamp = datetime.datetime.fromtimestamp(float(created)).strftime('%Y-%m-%d %H:%M:%S.%f')
    
        data2 = ET.Element("attribute"
                            , {"NAME": "created"
                              , "VALUE" : stamp
#                               , "VALUE" : created
                         })
#         <attribute_layout NAME_WIDTH="74" VALUE_WIDTH="119"/>
        data3 = ET.Element("attribute_layout"
                    , {"NAME_WIDTH": "75"
                      , "VALUE_WIDTH" : "120"
#                     , {"NAME_WIDTH": 75
#                       , "VALUE_WIDTH" : 120
#                     , {"NAME_WIDTH": cons31.NodeVar.ATTRIB_NAME_WIDTH.value
#                       , "VALUE_WIDTH" : cons31.NodeVar.ATTRIB_VALUE_WIDTH.value
                         })
#         data3 = ET.Element(
#                     "attribute_layout"
#                     , {"NAME_WIDTH": 75
#                       , "VALUE_WIDTH" : 120
# #                     , {"NAME_WIDTH": cons31.NodeVar.ATTRIB_NAME_WIDTH.value
# #                       , "VALUE_WIDTH" : cons31.NodeVar.ATTRIB_VALUE_WIDTH.value
#                          })
        
        ### append
        node.append(data2)
#         node.append(data2)
        node.append(data3)
        
        print ("[%s:%d] appended : %s" % \
               (os.path.basename(libs.thisfile()), libs.linenum(), node.attrib))
        
    else : #/if not created == None
        
        print ("[%s:%d] 'CREATED' => None : %s" % \
               (os.path.basename(libs.thisfile()), libs.linenum(), node.attrib))
        
    #/if not created == None
    
#     ### report
#     print()
#     print ("[%s:%d] node.attrib = '%s', data2.tab = '%s'" % \
#            (os.path.basename(libs.thisfile()), libs.linenum()
#             , node.attrib, data2.tag))
    
    return node
    
#/def add_Created(node):

def add_Node_Attribute_Created(tree) :
    
    root = tree.getroot()
    
    '''###################
        nodes : g-1        
    ###################'''
    print()
    print ("[%s:%d] root.tag => '%s' / root.attrib => '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum() 
            , root.tag, root.attrib))
    
    g1 = root[0]
    
    g1 = add_Created(g1)

    '''###################
        return        
    ###################'''
    return tree
    
#/add_Node_Attribute_Created(tree)

def add_Number(node) :
# def _add_Numbering(node) :
    
    #debug
    print()
    print ("[%s:%d] node.tag = '%s'\nnode.attrib = '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), node.tag, node.attrib))
    
    lenOf_Node = len(node)
    
    '''###################
        has subnodes        
    ###################'''
    if lenOf_Node > 0 :
        
        '''###################
            numbering : subnodes        
        ###################'''
        cnt = 0
        
        for i in range(lenOf_Node):
#         for item in node:
            '''###################
                validate : 'node' node ?        
            ###################'''
            node_New = node[i]
            
            if node_New.tag == 'arrowlink' \
                or  node_New.tag == 'attribute' \
                or  node_New.tag == 'attribute_layout' :
                              
                continue
            
            #/if node_New.tag == 
            
            #debug
            print()
            print ("[%s:%d] node_New.tag = '%s'\nnode_New.attrib = '%s'" % \
                   (os.path.basename(libs.thisfile()), libs.linenum()
                    , node_New.tag, node_New.attrib))

            
            '''###################
                exec numbering        
            ###################'''
            txt_Prev = node_New.get('TEXT')
            
            txt_New = "%d) %s" % (cnt + 1, txt_Prev)
            
            node_New.set('TEXT', txt_New)
            
            ### increment
            cnt += 1
            
#             '''###################
#                 child nodes ?        
#             ###################'''
#             if len(node_New) > 0 : #if len(node[i]) > 0
#             
#                 _add_Numbering(node_New)

    '''###################
        further        
    ###################'''
    if lenOf_Node > 0 :
        
        for i in range(lenOf_Node):
            
            node_New = node[i]

            '''###################
                subnode has subnodes ?        
            ###################'''
            if len(node_New) > 0 : #if len(node[i]) > 0
                
                add_Number(node_New)
#                 _add_Numbering(node_New)


    '''###################
        return        
    ###################'''
    return
    
#/def _add_Numbering(tree) :

def add_Number__Through(node, num_Str) :
# def _add_Numbering(node) :
    
    #debug
    print()
    print ("[%s:%d] node.tag = '%s'\nnode.attrib = '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), node.tag, node.attrib))
    
    lenOf_Node = len(node)
    
    '''###################
        has subnodes        
    ###################'''
    if lenOf_Node > 0 :
        
        '''###################
            numbering : subnodes        
        ###################'''
        cnt = 0
        
        for i in range(lenOf_Node):
#         for item in node:
            '''###################
                validate : 'node' node ?        
            ###################'''
            node_New = node[i]
            
            if node_New.tag in cons_mm.MM.MM_NUMBERING_OMIT_NODES.value \
                or node_New.attrib['TEXT'] \
                        in cons_mm.MM.MM_NUMBERING_OMIT_LABELS.value :
#                 or node_New.tag in cons_mm.MM.MM_NUMBERING_OMIT_LABELS.value :
#             if node_New.tag == 'arrowlink' \
#                 or  node_New.tag == 'attribute' \
#                 or  node_New.tag == 'attribute_layout' \
#                 or  node_New.tag == 'cloud' \
#                 or  node_New.tag == 'icon' \
#                 or  node_New.tag == 'font' \
#                 or  node_New.tag == 'linktarget' :
                              
                continue
            
            #/if node_New.tag == 
            
            #debug
            print()
            print ("[%s:%d] node_New.tag = '%s'\nnode_New.attrib = '%s'" % \
                   (os.path.basename(libs.thisfile()), libs.linenum()
                    , node_New.tag, node_New.attrib))

            
            '''###################
                exec numbering        
            ###################'''
            txt_Prev = node_New.get('TEXT')
            
            txt_New = ""
            
            if num_Str == "" : txt_New = "%d) %s" % (cnt + 1, txt_Prev)
            else : txt_New = "%s-%d) %s" % (num_Str, cnt + 1, txt_Prev)

#             txt_New = "%s-%d) %s" % (num_Str, cnt + 1, txt_Prev)
            
            node_New.set('TEXT', txt_New)
            
            '''###################
                child nodes ?        
            ###################'''
            if len(node_New) > 0 : #if len(node[i]) > 0
             
                ### num string
                num_Str_New = ""
                
                if num_Str == "" : num_Str_New = "%d" % (cnt + 1)
                else : num_Str_New = "%s-%d" % (num_Str, cnt + 1)
                
                ## recursive
                add_Number__Through(node_New, num_Str_New)
#                 _add_Numbering__(node_New)

            '''###################
                counter        
            ###################'''
            ### increment
            cnt += 1
            
    '''###################
        return        
    ###################'''
    return
    
#/add_Number__Through(node)

def add_Numbering(tree) :
    '''###################
        root        
    ###################'''
    root = tree.getroot()
    
    '''###################
        nodes : g-1        
    ###################'''
    g1 = root[0]
    
    ### add number
    add_Number(g1)
    
#     for item in g1:
#         
#         add_Number(g1)
#         _add_Numbering(g1)
        
    #/for item in g1:
    
    '''###################
        return        
    ###################'''
    return tree
    
#/add_Numbering(tree)

def add_Numbering__Through(tree):
    '''###################
        root        
    ###################'''
    root = tree.getroot()
    
    '''###################
        nodes : g-1        
    ###################'''
    g1 = root[0]
    
    ### add number
    num_Str = ""
#     num_Str = "0"
    
    add_Number__Through(g1, num_Str)
    
    '''###################
        return        
    ###################'''
    return tree
    
#/add_Numbering__Through(node, num_Str)

def get_Node_Self(node):
    
    
    
    return node
#/def get_Node_Self(node):
    
def _get_Histories(node, lo_Histories) :
    
    '''###################
        validate : special node or text?        
    ###################'''
    if node.tag in cons_mm.MM.MM_NUMBERING_OMIT_NODES.value \
                or node.attrib['TEXT'] \
                        in cons_mm.MM.MM_NUMBERING_OMIT_LABELS.value :
        
        return
    
    '''###################
        append : self        
    ###################'''
    node_Copy = copy.deepcopy(node)
   
#     node_Self = node_Copy
    node_Self = remove_Subnodes(node_Copy)
#     node_Self = get_Node_Self(node_Copy)
    
    #debug
    print()
    print("[%s:%d] node_Self.attrib => %s" % \
              (os.path.basename(libs.thisfile()), libs.linenum()
              , node_Self.attrib
              ), file=sys.stderr)

    
    ### modify ID
    if 'ID' in node_Self.attrib : #if 'ID' in node_Self.attrib
                         
        id_Orig = node_Self.attrib['ID']
         
        id_New = id_Orig + "." + "COPY"
         
    else:#/if 'ID' in node_Self.attrib
        
        #ref millseconds https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python
        mill = int(round(time.time() * 1000))
        
        id_New = "ID_%s" % (str(mill)[-11:-1])
        
    #/if 'ID' in node_Self.attrib
                         
                         
#     id_Orig = node_Self.attrib['ID']
#     
#     id_New = id_Orig + "." + "COPY"
    
    node_Self.attrib['ID'] = id_New
   
   
    lo_Histories.append(node_Self)
#     lo_Histories.append(node)
    
    for subnode in node :
        
        _get_Histories(subnode, lo_Histories)
    
    #/for subnode in node :
    
#/_get_Histories(node)

def build_History__Exec(node) :
# def _add_Numbering(node) :
    
    #debug
    print()
    print ("[%s:%d] node.tag = '%s'\nnode.attrib = '%s'" % \
           (os.path.basename(libs.thisfile()), libs.linenum(), node.tag, node.attrib))
    
    lenOf_Node = len(node)
    
    '''###################
        history        
    ###################'''
    lo_Histories = []
    
    _get_Histories(node, lo_Histories)
    
    '''###################
        return        
    ###################'''
    return lo_Histories
    
#/def build_History__Exec(node, num_Str) :

def _test_Remove_Subnodes(node):
    
    lenOf_Node = len(node)
    
    print()
    print("[%s:%d] lenOf_Node => %d" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , lenOf_Node
            ), file=sys.stderr)

    '''###################
        remove        
    ###################'''
    node_Copy = copy.deepcopy(node)
    
    print()
    print("[%s:%d] len(node_Copy) => %d (%s)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(node_Copy), node_Copy
            ), file=sys.stderr)
    
    print()
    print("[%s:%d] node[1] => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , node[1]
        ), file=sys.stderr)
    
    print()
    print("[%s:%d] node_Copy[1] => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , node_Copy[1]
        ), file=sys.stderr)
    
    '''###################
        build : list of target nodes        
    ###################'''
    lo_Target_Nodes = []
    
    for item in node_Copy:
               
       lo_Target_Nodes.append(item)
       
    #/for item in node_Copy:
    
    print()
    print("[%s:%d] len(lo_Target_Nodes) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Target_Nodes)
        ), file=sys.stderr)

    ### remove
    for item in lo_Target_Nodes:

        print()
        print("[%s:%d] removing... => %s" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , item
            ), file=sys.stderr)

        node_Copy.remove(item)
        
    #/for item in lo_Target_Nodes:

    
    
#     for item in node:
# 
#         print()
#         print("[%s:%d] removing item => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , item
#             ), file=sys.stderr)
#  
#         node_Copy.remove(item)
#         
#     #/for item in node():

    print()
    print("[%s:%d] len(node_Copy) => %d (%s)" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , len(node_Copy), node_Copy
            ), file=sys.stderr)
    
    print(node_Copy.attrib)

#     subnodes = node.findall('')
#     
#     print()
#     print("[%s:%d] len(subnodes) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(subnodes)
#             ), file=sys.stderr)
#/def _test_Remove_Subnodes(node):

def remove_Subnodes(node):
    
#     lenOf_Node = len(node)
#     
#     print()
#     print("[%s:%d] lenOf_Node => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , lenOf_Node
#             ), file=sys.stderr)

    '''###################
        remove        
    ###################'''
    node_Copy = copy.deepcopy(node)
    
#     print()
#     print("[%s:%d] len(node_Copy) => %d (%s)" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(node_Copy), node_Copy
#             ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] node[1] => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , node[1]
#         ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] node_Copy[1] => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , node_Copy[1]
#         ), file=sys.stderr)
    
    '''###################
        build : list of target nodes        
    ###################'''
    lo_Target_Nodes = []
    
    for item in node_Copy:
               
       lo_Target_Nodes.append(item)
       
    #/for item in node_Copy:
    
#     print()
#     print("[%s:%d] len(lo_Target_Nodes) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(lo_Target_Nodes)
#         ), file=sys.stderr)

    ### remove
    for item in lo_Target_Nodes:

#         print()
#         print("[%s:%d] removing... => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , item
#             ), file=sys.stderr)

        node_Copy.remove(item)
        
    #/for item in lo_Target_Nodes:

    
    
#     for item in node:
# 
#         print()
#         print("[%s:%d] removing item => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , item
#             ), file=sys.stderr)
#  
#         node_Copy.remove(item)
#         
#     #/for item in node():

#     print()
#     print("[%s:%d] len(node_Copy) => %d (%s)" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(node_Copy), node_Copy
#             ), file=sys.stderr)
#     
#     print(node_Copy.attrib)

#     subnodes = node.findall('')
#     
#     print()
#     print("[%s:%d] len(subnodes) => %d" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(subnodes)
#             ), file=sys.stderr)

    return node_Copy

#/def _test_Remove_Subnodes(node):

def remove_Subnodes__Self(node):
    

    '''###################
        remove        
    ###################'''
    lo_Target_Nodes = []
    
#     node_Copy = copy.deepcopy(node)
    for item in node:
        
        lo_Target_Nodes.append(item)
        
    #/for item in node:
    
    ### remove
#     for item in node_Copy:
    for item in lo_Target_Nodes:


        node.remove(item)
#         node_Copy.remove(item)
        
    #/for item in lo_Target_Nodes:

    return node
#     return node_Copy

#/def _test_Remove_Subnodes(node):

'''###################
    @return: 
        -1    find 'HISTORY' tag ==> returned None
        0    histories ==> appended
###################'''
def sort_Histories__Modified(lo_Histories):
    
#     print()
#     print("[%s:%d] before sorted ---> %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , lo_Histories
#             ), file=sys.stderr)
    
    #ref https://stackoverflow.com/questions/25338817/sorting-xml-in-python-etree answered Aug 16 '14 at 11:29
    #ref sorting https://docs.python.org/3.5/howto/sorting.html#sortinghowto
    res = sorted(lo_Histories, key=lambda child: child.get("CREATED"), reverse=True)
#     res = sorted(lo_Histories, key=lambda child: child.get("CREATED"))
#     res = sorted(lo_Histories, key=lambda child: child.get("MODIFIED"))
#     sorted(lo_Histories, key=lambda child: child.get(attr))
    
#     print()
#     print("[%s:%d] sorted ---> %s" % \
#                 (os.path.basename(libs.thisfile()), libs.linenum()
#                 , res
#                 ), file=sys.stderr)
     
    return res
    
#/def sort_Histories__Modified(lo_Histories):

def groupize_HISTORY_Entries(lo_Histories_Modified, sizeOf_Group):
    
    lo_Histories_Modified_Groupized = []
    
#     index = 0
    
    '''###################
        prep : group header nodes        
    ###################'''
    sizeOf_Histories = len(lo_Histories_Modified)
    
    for item in range(math.ceil(sizeOf_Histories / sizeOf_Group)):
#     for item in range(int(sizeOf_Histories / sizeOf_Group)):

        #ref millseconds https://stackoverflow.com/questions/5998245/get-current-time-in-milliseconds-in-python answered May 13 '11 at 22:21
#         millsec = int(round(time.time() * 1000))
        mill_Seconds = str(int(round(time.time() * 1000)))
        
#         millsec = str(millsec)
        
        #ref random int https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9 answered Oct 22 '10 at 12:51
        id = "00000" + "".join([str(randint(0,9)) for x in range(5)])

#         str_Node = "<node CREATED=\"%s\"" \    #=> workds
#                     % (mill_Seconds)
#         str_Node = "<node CREATED=\"%s\" ID=\"ID_%s\" " \    #=> works
#                     % (mill_Seconds, id)

#         str_Node = "<node CREATED=\"%s\" ID=\"ID_%s\" " \    #=> not working
#                 + "LINK=\"Projects.mm\" MODIFIED=\"%s\" " \
#                     % (mill_Seconds, id, mill_Seconds)
#         str_Node = "<node CREATED=\"%s\" ID=\"ID_%s\" " \
#                     + "LINK=\"Projects.mm\" MODIFIED=\"%s\" " #=> workds
        str_Node = "<node CREATED=\"%s\" ID=\"ID_%s\" " \
                    + "MODIFIED=\"%s\"  "\
                    + "FOLDED=\"true\"  "\
                    + "TEXT=\"%s\"></node>" #=> 
#                     + "LINK=\"Projects.mm\" MODIFIED=\"%s\"  "\
        
        text_Node = str_Node % (mill_Seconds, id, mill_Seconds, str(item + 1))
#         text_Node = str_Node % (mill_Seconds, id, mill_Seconds, str(item))

#         str_Node = "<node CREATED=\"%s\" ID=\"ID_%s\" " \
#                 + "LINK=\"Projects.mm\" MODIFIED=\"%s\" " \
#                 + "TEXT=\"%s\"></node>" \
#                     % (mill_Seconds, id, mill_Seconds, str(item))
                    
        print()
        print("[%s:%d] header node => '%s'" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , text_Node
#         , str_Node
        ), file=sys.stderr)
        
        '''###################
            append header node to the list        
        ###################'''
        node_Header = ET.fromstring(text_Node)
        
        print()
        print("[%s:%d] node_Header => %s" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , node_Header
        ), file=sys.stderr)
        
        lo_Histories_Modified_Groupized.append(node_Header)

    
    #debug
#    print()
#    print("[%s:%d] lo_Histories_Modified_Groupized[1] => %s" % \
#        (os.path.basename(libs.thisfile()), libs.linenum()
#        , lo_Histories_Modified_Groupized[1]
#        ), file=sys.stderr)

    '''###################
        test        
    ###################'''
#     lo_Histories_Modified_Groupized[1].append()

    '''###################
        append : history items to headers        
    ###################'''
    index = 0
    
    cnt = 0
    
    for item in lo_Histories_Modified:
#     for item in lo_Histories_Modified_Groupized:
      
        ### judge : entires in one group
#         if len(lo_Histories_Modified_Groupized[index]) \
#                 % sizeOf_Group == 0 : #if len(lo_Histories_Modified_Groupized) % sizeOf_Group
 
        if not cnt == 0 and cnt % sizeOf_Group == 0 : #if cnt % sizeOf_Group == 0
             
               index += 1
                 
           #/if cnt % sizeOf_Group == 0
             
             
#             index += 1
          
        ### append
        lo_Histories_Modified_Groupized[index].append(item)
          
        cnt += 1
         
    #/for item in lo_Histories_Modified_Groupized:

#/for item in range(int(sizeOf_Histories / sizeOf_Group)):

    
#     str_Node = "<node CREATED=\"1517542212333\" ID=\"ID_232518330.COPY\" LINK=\"Projects.mm\" MODIFIED=\"1517542358887\" TEXT=\"Dessins\"></node>"
#     
#     node_New = ET.fromstring(str_Node)
    
#     for item in lo_Histories_Modified:
    
#         ### judge : entires in one group
#         if len(lo_Histories_Modified_Groupized[index]) \
#                 % sizeOf_Group == 0 : #if len(lo_Histories_Modified_Groupized) % sizeOf_Group
#         
#             index += 1
#             
#         #/if len(lo_Histories_Modified_Groupized) % sizeOf_Group
#         
#         lo_Histories_Modified_Groupized[index].append(item)
#         
#     #/for item in lo_Histories_Modified:
# 
    return lo_Histories_Modified_Groupized
    
#/def groupize_HISTORY_Entries(lo_Histories_Modified):

'''###################
    Ops
    1. nodes in the list ---> group-ize by 10 (or, any number given from the template)
    2. append groups to ---> "HISTORY" node        
###################'''
def build_HISTORY_Branch(node, lo_Histories):
    
    #ref find https://stackoverflow.com/questions/27810825/find-all-nodes-by-attribute-in-xml-using-python-2 answered Jan 7 '15 at 3:14
    his = node.find('./*[@TEXT="HISTORY"]')
#     his = node.find('./*[@TEXT="HISTORY"')
    
    print()
    print("[%s:%d] node.find('./*[@TEXT=\"HISTORY\"]') => '%s'" % \
                (os.path.basename(libs.thisfile()), libs.linenum()
                , his
                ), file=sys.stderr)
            #     libmt.py:636] node.find('./*[@TEXT="HISTORY"]') => '<Element 'node' at 0x000000
            # 009399D18>'
            
    '''###################
        validate        
    ###################'''
    if his == None : #if his == None
                              
        print()
        print("[%s:%d] find 'HISTORY' tag ==> returned None" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)
        
        return -1
    
    else:
        
        print()
        print("[%s:%d] len(his) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(his)
        ), file=sys.stderr)
    #/if his == None
    
    '''###################
        histories --> sort        
    ###################'''
    lo_Histories_Modified = sort_Histories__Modified(lo_Histories)
    
    sizeOf_Group = 10
    
    lo_Histories_Modified_Groupized = \
                groupize_HISTORY_Entries(lo_Histories_Modified, sizeOf_Group)
    
    '''###################
        HISTORY ---> folded        
    ###################'''
    #FOLDED="true"
    his.attrib['FOLDED'] = "true"

    '''###################
        remove existing nodes        
    ###################'''
    print()
    print("[%s:%d] len(his) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(his)
        ), file=sys.stderr)

    print()
    print("[%s:%d] removing..." % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        
        ), file=sys.stderr)

    remove_Subnodes__Self(his)

    print()
    print("[%s:%d] len(his) is now => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(his)
        ), file=sys.stderr)
        
#     print()
#     print("[%s:%d] len(his) => %d" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , len(his)
#         ), file=sys.stderr)
#     
#     print()
#     print("[%s:%d] his[1] => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , his[1]
#         ), file=sys.stderr)
    
# #     his = remove_Subnodes(his)
#     lenOf_His = len(his)
#     
#     for index in range(lenOf_His):
#         
#         print()
#         print("[%s:%d] his[%d].attrib => %s" % \
#         (os.path.basename(libs.thisfile()), libs.linenum()
#         , index, his[index].attrib
#         ), file=sys.stderr)
#         
#         print()
#         print("[%s:%d] removing his[%d] => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , index, his[index]
#             ), file=sys.stderr)
#      
#         his.remove(his[0])
# #         his.remove(his[index])
#  
#         print()
#         print("[%s:%d] removed his[%d] => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , index, his[index]
#             ), file=sys.stderr)        
#         
#         print()
#         print("[%s:%d] len(his) is now => %s" % \
#             (os.path.basename(libs.thisfile()), libs.linenum()
#             , len(his)
#             ), file=sys.stderr)        
        
    #/for index in range(lenOf_His):

    
#     for item in his:
#                
#         his.remove(item)
#         
#     #/for item in his:


    print()
    print("[%s:%d] len(his) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(his)
        ), file=sys.stderr)
        
    '''###################
        append        
    ###################'''
    for item in lo_Histories_Modified_Groupized:
#     for item in lo_Histories_Modified:
#     for item in lo_Histories:

        his.append(item)
        
    #/for item in lo_Histories:

                              
            
#/ def build_HISTORY_Branch(tree, lo_Histories):

def build_History(tree):
    '''###################
        root        
    ###################'''
    root = tree.getroot()
    
    '''###################
        nodes : g-1        
    ###################'''
    g1 = root[0]
    
    ### add number
#     num_Str = ""
#     num_Str = "0"
    
    lo_Histories = build_History__Exec(g1)
    
    print()
    print("[%s:%d] len(lo_Histories) => %d" % \
        (os.path.basename(libs.thisfile()), libs.linenum()
        , len(lo_Histories)
        ), file=sys.stderr)
    print()
    
#     print(lo_Histories)
    for item in lo_Histories :
        
        print(item.tag + " / " \
              + item.attrib['TEXT'] \
              + " / " + item.attrib['MODIFIED'] \
              + " / len = " + str(len(item)))
#         print(item.tag + " / " + item.attrib['TEXT'])

    #/for item in lo_Histories :
    
    '''###################
        append : history        
    ###################'''
    ### remove subnodes
    
    print()
    print("[%s:%d] showing '%s' (TEXT = '%s' / len = %d) :" % \
            (os.path.basename(libs.thisfile()), libs.linenum()
            , lo_Histories[1].tag
            , lo_Histories[1].attrib['TEXT']
            , len(lo_Histories[1])
            ), file=sys.stderr)
    
    '''###################
        build : HISTORY branch        
    ###################'''
    build_HISTORY_Branch(g1, lo_Histories)
    
    '''###################
        return        
    ###################'''
    return tree
    
#/build_History(node, num_Str)



