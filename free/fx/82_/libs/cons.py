#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

TypeOf_Data_OpenClose   = "OpenClose"

'''###################
    Used in :
        libfx : def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
###################'''
class BarData(Enum):
    
    LABEL_OC        = "OC"
    LABEL_HL        = "HL"
    LABEL_RSI = "RSI"
    LABEL_MFI = "MFI"
    
    LABEL_BB_MAIN = "BB_Main"
    LABEL_BB_1S = "BB_1S"
    LABEL_BB_2S = "BB_2S"
    LABEL_BB_M1S = "BB_M1S"
    LABEL_BB_M2S = "BB_M2S"
    
    ROUND_BB    = 4
    ROUND_RSI   = 4
    ROUND_MFI   = 4
    
#     HighLowDiff_ID_Start    = 1
#     HighLowDiff_ID_End      = 5
#    HighLowDiff_ID_Start    = 195
#    HighLowDiff_ID_End      = 202
#    HighLowDiff_ID_Start    = 219	# 2017.12.18 13:00
#    HighLowDiff_ID_End      = 226	# 2017.12.16 06:00
    HighLowDiff_ID_Start    = 243	# 2017.12.15 13:00
    HighLowDiff_ID_End      = 250	# 2017.12.15 06:00

class FPath(Enum):
    
    fname_In_CSV = "49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"
    dpath_In_CSV = "../data"
#     fpath_In_CSV = dpath_In_CSV + "/" + fname_In_CSV
    
    fpath_Out_HighLowDiff = "outputs"

    ### file : output
    
    

class Label_ColNames(Enum):
    
    PAIR    = 'PAIR'
    PERIOD  = 'PERIOD'
    DAYS    = 'DAYS'
    SHIFT   = 'SHIFT'
    
