#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

class ImOp(Enum):
    
    lo_Commands = [
        
        [0, "Numbering"],
        [1, "De-numbering"],
#         [1, "Numbering"],
#         [2, "De-numbering"],
    
    ]
    
    
#/class ImOp(Enum):

class FPath(Enum):
    
    '''###################
        @USED
                
    ###################'''
    DPATH_MM_PROJECTS   = "C:\WORKS_2\WS\FM_2_20171104_225946\Projects"
    
class Numbering(Enum):
    
    ID_BT_EXEC_NUMBERING_0 = "bt_Exec_Numbering_0"
    
    
class ExecNumbering(Enum):

    DICKEY_MSG      = "msg"
    DICKEY_DPATH      = "dpath"
    DICKEY_FNAME      = "fname"


class RetVal(Enum):
    
    RET_OK      = "OK"
    
#/class RetVal(Enum):

# C:\\WORKS_2\\WS\\FM_2_20171104_225946\\Projects