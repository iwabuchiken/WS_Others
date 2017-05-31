% Copyright


implement taskWindow
    inherits applicationWindow
    open core, vpiDomains

%%%%%%%%%%%%%%%%%%%%%%%%%%%
domains
    gender = female(); male().

class facts - familyDB
    person : (string Name, gender Gender).
    parent : (string Person, string Parent).

class predicates
    father : (string Person, string Father) nondeterm anyflow.
clauses
    father(Person, Father) :-
        parent(Person, Father),
        person(Father, male()).

class predicates
    grandFather : (string Person, string Grandfather) nondeterm anyflow.
clauses
    grandfather(Person, Grandfather) :-
        parent(Person, Parent),
        father(Parent, Grandfather).

class predicates
    ancestor : (string Person, string Ancestor) nondeterm anyflow.
clauses
    ancestor(Person, Ancestor) :-
        parent(Person, Ancestor).
    ancestor(Person, Ancestor) :-
        parent(Person, P1),
        ancestor(P1, Ancestor).

class predicates
    reconsult : (string FileName).
clauses
    reconsult(Filename) :-
        retractFactDB(familyDB),
        file::consult(Filename, familyDB).


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

constants
    mdiProperty : boolean = true.

clauses
    new() :-
        applicationWindow::new(),
        generatedInitialize().

predicates
    onShow : window::showListener.
clauses
    onShow(_, _CreationData) :-
        _MessageForm = messageForm::display(This).

class predicates
    onDestroy : window::destroyListener.
clauses
    onDestroy(_).

class predicates
    onHelpAbout : window::menuItemListener.
clauses
    onHelpAbout(TaskWin, _MenuTag) :-
        _AboutDialog = aboutDialog::display(TaskWin).

predicates
    onFileExit : window::menuItemListener.
clauses
    onFileExit(_, _MenuTag) :-
        close().

predicates
    onSizeChanged : window::sizeListener.
clauses
    onSizeChanged(_) :-
        vpiToolbar::resize(getVPIWindow()).

predicates
    onFileOpen : window::menuItemListener.
clauses
    onFileOpen(_Source, _MenuTag).

% This code is maintained automatically, do not update it manually. 13:28:53-31.5.2017
predicates
    generatedInitialize : ().
clauses
    generatedInitialize():-
        setText("ch01_p03"),
        setDecoration(titlebar([closeButton,maximizeButton,minimizeButton])),
        setBorder(sizeBorder()),
        setState([wsf_ClipSiblings]),
        whenCreated({ :- projectToolbar::create(getVpiWindow()) }),
        addSizeListener({ :- vpiToolbar::resize(getVpiWindow()) }),
        setMdiProperty(mdiProperty),
        menuSet(resMenu(resourceIdentifiers::id_TaskMenu)),
        addShowListener(onShow),
        addSizeListener(onSizeChanged),
        addDestroyListener(onDestroy),
        addMenuItemListener(resourceIdentifiers::id_help_about, onHelpAbout),
        addMenuItemListener(resourceIdentifiers::id_file_exit, onFileExit),
        addMenuItemListener(resourceIdentifiers::id_file_open, onFileOpen).
% end of automatic code
end implement taskWindow