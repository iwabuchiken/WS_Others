% Copyright 

implement projectToolbar
    open core, vpiDomains, vpiToolbar, resourceIdentifiers

clauses
    create(Parent) :-
        StatusBar = statusBar::newApplicationWindow(),
        StatusCell = statusBarCell::new(StatusBar, 0),
        StatusBar:cells := [StatusCell],
        Toolbar = vpiToolbar::create(style, Parent, controlList),
        setStatusHandler(Toolbar, {(Text) :- StatusCell:text := Text}).

% This code is maintained automatically, do not update it manually. 13:16:40-31.5.2017
constants
    style : vpiToolbar::style = tb_top.
    controlList : vpiToolbar::control_list =
        [
        tb_ctrl(id_file_new,pushb,resId(idb_NewFileBitmap),"New;New File",1,1),
        tb_ctrl(id_file_open,pushb,resId(idb_OpenFileBitmap),"Open;Open File",1,1),
        tb_ctrl(id_file_save,pushb,resId(idb_SaveFileBitmap),"Save;Save File",1,1),
        vpiToolbar::separator,
        tb_ctrl(id_query_mother,pushb,resId(idb_UndoBitmap),"Query mothers;List of all mothers listed in the database",1,1),
        tb_ctrl(id_query_father,pushb,resId(idb_RedoBitmap),"Query fathers;List of all fathers listed in the database",1,1),
        vpiToolbar::separator,
        vpiToolbar::separator,
        tb_ctrl(id_help_contents,pushb,resId(idb_HelpBitmap),"Help;Help",1,1)
        ].
% end of automatic code
end implement projectToolbar