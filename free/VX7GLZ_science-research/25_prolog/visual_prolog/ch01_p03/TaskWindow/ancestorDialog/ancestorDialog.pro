% Copyright 

implement ancestorDialog
    inherits dialog
    open core, vpiDomains


clauses
    display(Parent) = Dialog :-
        Dialog = new(Parent),
        Dialog:show().

clauses
    new(Parent) :-
        dialog::new(Parent),
        generatedInitialize().

% This code is maintained automatically, do not update it manually. 12:45:57-31.5.2017
facts
    ok_ctl : button.
    cancel_ctl : button.
    idc_ancestordialog_personname : editControl.

predicates
    generatedInitialize : ().
clauses
    generatedInitialize():-
        setFont(vpi::fontCreateByName("Tahoma", 8)),
        setText("ancestorDialog"),
        setRect(rct(50,40,290,160)),
        setModal(true),
        setDecoration(titlebar([closeButton])),
        setState([wsf_NoClipSiblings]),
        idc_ancestordialog_personname := editControl::new(This),
        idc_ancestordialog_personname:setText("Edit"),
        idc_ancestordialog_personname:setPosition(88, 23),
        idc_ancestordialog_personname:setWidth(100),
        ok_ctl := button::newOk(This),
        ok_ctl:setText("&OK"),
        ok_ctl:setPosition(64, 96),
        ok_ctl:setSize(56, 16),
        ok_ctl:defaultHeight := false,
        ok_ctl:setAnchors([control::right,control::bottom]),
        cancel_ctl := button::newCancel(This),
        cancel_ctl:setText("Cancel"),
        cancel_ctl:setPosition(128, 96),
        cancel_ctl:setSize(56, 16),
        cancel_ctl:defaultHeight := false,
        cancel_ctl:setAnchors([control::right,control::bottom]),
        StaticText_ctl = textControl::new(This),
        StaticText_ctl:setText("Person"),
        StaticText_ctl:setPosition(24, 21),
        StaticText_ctl:setSize(52, 13).
% end of automatic code
end implement ancestorDialog 