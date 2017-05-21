[libs].

add_to_list(X, Ls, [X | Ls]).

/***************************
#1	msg(Float) :-
*****************************/
msg(Float) :-
%! 	writef('%15L%w', ['Hello', 'World']).
%! 	writef("num is %s", ["yyyyy"]).
%! 	writef('num is %s', ['yyyyy']).
%! 	writef('num is %w', ['yyyyy']).   %! works
%! 	writef("num is %w", ['yyyyy']).   %! works
%! 	writef("num is %w", ["yyyyy"]).   %! works
% 	writef("num is %w", [Float]).   %! "num is 0.34"
% *** ref http://www.swi-prolog.org/pldoc/man?section=format "format(+Format, :Arguments)"
	format('~10f', Float).


/***************************
#2	comp_char([X | Ls], Char, Z)
*****************************/
comp_char([X | Ls], Char, Z) :-
	write(X),write("\n"),
	write("Z is : "),write(Z),write("\n"),
%! 	comp_char(Ls, Char, Z).
%! 	comp_char(Ls, Char, add_to_list(X, Z, Ls)).   %! => 'add_to_list(c,add_to_list(b,add_to_list(a,_112,[b,c,d]),[c,d]),[d])'
%! 	comp_char(Ls, Char, [Z|X]).
		%! a
		%! Z is : _112
		%! b
		%! Z is : [_112|a]
		%! c
		%! Z is : [[_112|a]|b]
		%! d
		%! Z is : [[[_112|a]|b]|c]
		%! false.

	comp_char(Ls, Char, [X|Z]).
		%! a
		%! Z is : _112
		%! b
		%! Z is : [a|_112]
		%! c
		%! Z is : [b,a|_112]
		%! d
		%! Z is : [c,b,a|_112]
		%! false.

/***************************
#3	rdiv(X,Y)
*****************************/
rdiv(X,Y) :-
	format("~3f", [X rdiv Y]).   %! => 1.667
%! 	format("~~df", [4, "X rdiv Y"]).   %! => '~df'

/***************************
#4	echo([X|Ls], Z)
*****************************/
echo([X|Ls], Z) :-
	format("X is ~s\n", [X]),
	echo(Ls,Z).
		%! X is a
		%! X is b
		%! X is c
		%! false.

/***************************
#4	echo_2([X|Ls], Z)
*****************************/
%! echo_2(1, [X|Ls], Ls).
echo_2(1, [X|Ls], Ls) :-
	write("N is 1\n"),
	format("X is ~s / Ls is ~s", [X, Ls]).

echo_2(N, [X|Ls], [X|Zs]) :-
	N > 0, N1 is N - 1,
%! 	format("X is ~s\n", [X]),
%! 	format("X is ~s / [X|Ls] = ~s / [X|Zs] = ~s\n", [X, [X|Ls], [X|Zs]]),
	format("X is ~s / [X|Ls] = ~s\n", [X, [X|Ls]]),
	write("Zs = "), write(Zs), write("\n"),
	write(X), write("|"),write(Zs),write("\n"),
%! 	format("Zs is ~s\n", [Zs]),
	echo_2(N1, Ls,Zs).

/***************************
#5	echo_3([X|Ls], Z)
*****************************/
%! echo_2(1, [X|Ls], Ls).
echo_3(1, [X|Ls], Ls) :-
	write("N is 1\n"),
	format("X is ~s / Ls is ~s", [X, Ls]).

%! echo_3(N, [X|Ls], [format("~s~s",[X, "-done"]) | Zs]) :-
echo_3(N, [X|Ls], [X | Zs]) :-
	N > 0, N1 is N - 1,
%! 	format("X is ~s\n", [X]),
%! 	format("X is ~s / [X|Ls] = ~s / [X|Zs] = ~s\n", [X, [X|Ls], [X|Zs]]),
	format("X is ~s / [X|Ls] = ~s\n", [X, [X|Ls]]),
	write("Zs = "), write(Zs), write("\n"),
	write(X), write("|"),write(Zs),write("\n"),
%! 	format("Zs is ~s\n", [Zs]),
	echo_3(N1, Ls,Zs).

/***************************
#6	conc(X, Ls)
*****************************/
conc(X, Ls) :-
	[libs],
%! 	format("~s\n", [[X|Ls]]).
	format("~s\n", [[X|Ls]]),
	rest(Ls, Z),
	write(Z).
		%! ?- conc(a,[b,c,d]).
		% abcd
		% [c,d]
%! 	format("~s\n", [rest(Ls, Z)]).
		%! ERROR: Illegal argument to format sequence ~s: rest([b,c,d],_3650)
		% ERROR: In:
		% ERROR:    [9] format("~s\n",[rest(...,_3726)])


/***************************
#7	split(X,Z)
*****************************/
split([X|Ls],Z) :-
	write("X is "),
	write(X).
