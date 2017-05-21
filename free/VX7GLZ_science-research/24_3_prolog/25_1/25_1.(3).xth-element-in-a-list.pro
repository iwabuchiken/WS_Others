/** 
%! retrieve(1, [X | Ls], X).
%! retrieve(1, [X | Ls], Y) :-
retrieve(1, [X | Ls]) :-
	X.


%! retrieve(N, [Y | Ls], X)
*/

%!  retrieve(1, [X | Ls]) :-
%! 	write ("yes").

%! retrieve(1,  [X | Ls], X). %! => X = a.

retrieve(1, [X | Ls], X).
%! retrieve(1, [X | Ls], X) :-
%! 	write("processing...").   %! => works.
%! 	write("yes\t"), X.   %! => 'Undefined procedure: a/0'
%! 	write("yes\t"), write(X).   %! => 'yes     a'

retrieve(N, [Y | Ls], X) :-
    N > 1, write("processing..."), N1 is N - 1, retrieve(N1, Ls, X).

%! ref comment http://www.swi-prolog.org/pldoc/man?section=format
/** ***** console memos *****
write(retrieve(3, ["Formatted", "write.", "Format", "is", "an", "atom", "whose", "characters", "will"], X).
=>		retrieve(3,[Formatted,write.,Format,is,an,atom,whose,characters,will],_11006)
		true.

*/
