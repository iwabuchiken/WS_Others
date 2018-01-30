#!C:\WORKS_2\Programs\Python\Python_3.5.1\python.exe
from enum import Enum

class ImOp(Enum):
    
    OP_0_1 = "0-1"      # 0-1) start xampp, filezilla, open folder, open files.bat
    OP_1 = "1"          # 1) change_file_names.bat
    OP_1_2 = "1-2"      # 1-2) Delete_in-db-existing-files.bat
    
    OP_2_0 = "2-0"      # 2-0) edit_memos.9-0.bat
    OP_4 = "4"          # 4) edit_memos.8.open-csv-file.bat - ショートカット
    OP_5 = "5"          # 5) edit_memos.3.insert-to-db.bat - ショートカット
    
    OP_7 = "7"      # 7) edit_memos.12.delete-image-files.bat - ショートカット
    OP_8 = "8"      # 8) edit_memos.4.delete-photos.bat - ショートカット
    OP_9 = "9"      # 9) edit_memos.13.validate-admin-value.bat - ショートカット
    OP_9_1 = "9-1"      # 9) edit_memos.13.validate-admin-value.bat - ショートカット

    lo_Commands = [
        
        [OP_0_1, "0-1) start xampp, filezilla, open folder, open files.bat"],
        [OP_1, "1) change_file_names.bat"],
        [OP_1_2, "1-2) Delete_in-db-existing-files.bat"],

        [OP_2_0, "2-0) edit_memos.9-0.bat"],
        [OP_4, "4) edit_memos.8.open-csv-file.bat - ショートカット"],
        [OP_5, "edit_memos.3.insert-to-db.bat"],
#         [OP_5, "5) edit_memos.3.insert-to-db.bat - ショートカット"],
               
        [OP_7, "edit_memos.12.delete-image-files.bat"],
#         [OP_7, "7) edit_memos.12.delete-image-files.bat - ショートカット"],
        [OP_8, "edit_memos.4.delete-photos.bat"],
#         [OP_8, "8) edit_memos.4.delete-photos.bat - ショートカット"],
               
        [OP_9, "edit_memos.13.validate-admin-value.bat"],
#         [OP_9, "9) edit_memos.13.validate-admin-value.bat - ショートカット"],

        [OP_9_1, "9-1) upload db file.txt"],
    
    ]
    
#     do_Commands = {
#         
#         OP_0_1 : "0-1) start xampp, filezilla, open folder, open files.bat",
#         OP_1 : "1) change_file_names.bat",
# 
#         OP_2_0 : "2-0) edit_memos.9-0.bat",
#                
#         OP_4 : "4) edit_memos.8.open-csv-file.bat - ショートカット",
#         OP_5 : "5) edit_memos.3.insert-to-db.bat - ショートカット",
#                
#         OP_7 : "7) edit_memos.12.delete-image-files.bat - ショートカット",
#         OP_8 : "8) edit_memos.4.delete-photos.bat - ショートカット",
#                
#         OP_9 : "9) edit_memos.13.validate-admin-value.bat - ショートカット",
#     
#     }
#     lo_Commands = {
#         
#         OP_0_1 : "0-1) start xampp, filezilla, open folder, open files.bat",
#         OP_2_0 : "2-0) edit_memos.9-0.bat",
#         
#         OP_4 : "4) edit_memos.8.open-csv-file.bat - ショートカット",
#         OP_5 : "5) edit_memos.3.insert-to-db.bat - ショートカット",
#         
#         OP_7 : "7) edit_memos.12.delete-image-files.bat - ショートカット",
#         OP_8 : "8) edit_memos.4.delete-photos.bat - ショートカット",
#         
#         OP_9 : "9) edit_memos.13.validate-admin-value.bat - ショートカット",
#     
#     }
    
#/class ImOp(Enum):

class FPath(Enum):
    
    '''###################
        @USED
        viwes :: _im_actions__Ops_4()
                _im_actions__Ops_5(action)
                
    ###################'''
    DPATH_CMD_LIB_OTHERS = "C:\\WORKS_2\\WS\\Eclipse_Luna\\Cake_IFM11\\lib\\others"
    
    DPATH_CMD_LIB_WS_CAKE_IFM11 = "C:\\WORKS_2\\WS\\WS_Cake_IFM11\\commands"
    
    