# -*- coding: utf-8 -*-

import inspect
import os

import sys

#ref https://stackoverflow.com/questions/415511/how-to-get-current-time-in-python "answered Jan 6 '09 at 4:59"
from time import gmtime, strftime, localtime, time
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



