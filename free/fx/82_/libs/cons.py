#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

TypeOf_Data_OpenClose   = "OpenClose"

'''###################
    Used in :
        libfx : def get_HighLowDiffs(aryOf_BarDatas, id_Start, id_End)
###################'''
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

HighLowDiff_ID_Start    = 1
HighLowDiff_ID_End      = 5
# HighLowDiff_ID_Start    = 195
# HighLowDiff_ID_End      = 202

class FPath(Enum):
    
    fname_In_CSV = "../data/49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"
    
