% Copyright

implement main
    open core

%%%%%%%%%%%%%%%%%%%%%%%

class predicates
    str2list : (string X) nondeterm anyflow.

clauses
    str2list(X) :-
%        [X].
%        format('~a~%' X).
        write(X).

%%%%%%%%%%%%%%%%%%%%%%%%%

clauses
    run() :-
        succeed. % place your own code here


end implement main

goal
    console::runUtf8(main::run).