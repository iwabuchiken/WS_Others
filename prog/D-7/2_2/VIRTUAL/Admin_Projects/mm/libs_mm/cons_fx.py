#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

from Admin_Projects.definitions import ROOT_DIR
from Admin_Projects.definitions import DPATH_ROOT_CURR

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
    
    fname_In_CSV = "44_1.14_file-io.EURUSD.Period-H1.Days-1900.Bars-45600.20180511_180935.csv"
#     fname_In_CSV = "44_1.14_file-io.AUDJPY.Period-H1.Days-1900.Bars-45600.20180511_181322.csv"
#     fname_In_CSV = "44_1.14_file-io.EURJPY.Period-H1.Days-1900.Bars-45600.20180511_181622.csv"
#     fname_In_CSV = "44_1.14_file-io.USDJPY.Period-H1.Days-1900.Bars-45600.20180511_181208.csv"
#     fname_In_CSV = "49_11_file-io" \
#                     + ".USDJPY" \
#                     + ".Period-H1" \
#                      + ".Days-100" \
#                      + ".Bars-17280" +\
#                       ".20171231_233726.csv"
#     fname_In_CSV = "49_11_file-io.USDJPY.Period-H1.Days-720.Bars-17280.20171231_233725.csv"
    
    dpath_In_CSV = DPATH_ROOT_CURR + "\\data\\csv"
#     dpath_In_CSV = DPATH_ROOT_CURR + "/data/csv"
#     dpath_In_CSV = "C:/WORKS_2/WS/WS_Others/prog/D-7/2_2/VIRTUAL/Admin_Projects/curr/data/csv"
#     dpath_In_CSV = "./csv"
#     dpath_In_CSV = "./data"
#     dpath_In_CSV = "../data"
#     fpath_In_CSV = dpath_In_CSV + "/" + fname_In_CSV
    
    fpath_Out_HighLowDiff = "outputs"

    ### file : output
    
    dpath_Data_Miscs = DPATH_ROOT_CURR + "/data/miscs"
    
    '''###################
        gen peak data        
    ###################'''
    fname_Gen_PeakData_Dflt = "49_20_file-io.USDJPY.Period-H1.Days-1200.Bars-28800.20180428_073251.csv"

class Label_ColNames(Enum):
    
    PAIR    = 'PAIR'
    PERIOD  = 'PERIOD'
    DAYS    = 'DAYS'
    SHIFT   = 'SHIFT'
    

class PatternMatch(Enum) :
    
    '''###################
        get_AryOf_BarDatas_PatternMatched__RSI__V2
    ###################'''
    PATTERNMATCH_NUMOFSEQUENCE_RSI = 3  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    RANGE_FLAT_RSI          = 1.0  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    FLAG_UPDOWN_UP          = 1  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    FLAG_UPDOWN_DOWN        = 0  # USED IN : get_AryOf_BarDatas_PatternMatched__RSI
    
    '''###################
        get_AryOf_BarDatas_PatternMatched__Body_UpDown()
    ###################'''
    VOLUMEOF_BODY       = 0.05   # JPY
#     VOLUMEOF_BODY       = 0.1   # JPY
#     VOLUMEOF_BODY       = 0.15   # JPY
#     VOLUMEOF_BODY       = 0.20   # JPY
#     VOLUMEOF_BODY       = 0.25   # JPY
#     VOLUMEOF_BODY       = 0.30   # JPY
#     VOLUMEOF_BODY       = 0.35   # JPY
#     VOLUMEOF_BODY       = 0.40   # JPY
#     VOLUMEOF_BODY       = 0.45   # JPY
#     VOLUMEOF_BODY       = 0.5   # JPY
    
    UPDOWN_PATTERN      = [1,1,1,0]
    
class PairName(Enum) :
    
    pair_Names = [
        
        "USDJPY",
        "EURJPY",
        "AUDJPY",
        "GBPJPY",
        
        "EURUSD",
        
    ]
