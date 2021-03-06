/**
 * X   => stream
 * Y   => term
 * Z   => counter
 */
%! read_data() :-
read_data(X) :-
%    Z is 0,
%    see("C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/25_prolog/25_6/t-1.fx.pro"),
%
%    see('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/25_prolog/25_6/t-1.fx.pro'),
%
%    see('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\25_prolog\\25_6\\rate.u-j.dat'),
%
    see(X),
%    read(Y),
%    write("file read : "),write(Y),write("\n"),
%    seen,
    repeat,   %! ;;; unless (...
    read(Y),
    %ref http://www.swi-prolog.org/pldoc/man?predicate=split_string/4
    split_string(Y, "\t", "", L),
    length(L,N),
    write(L),write(" --> "),write(N),write("\n"),
    %ref https://stackoverflow.com/questions/12939425/prolog-access-specific-member-of-list 'answered Oct 17 '12 at 17:06'
    nth0(0,L,Elem),
    format('0th --> \'~a\'~n',Elem),

%    nth0(
%    write("file read : "),write(Y),write("\n"),
%    write(Y),write("\n"),

    Y == end_of_file, %! ;;; );unless
    !,
    seen,     %! ;;; close(file) ===> told

    format('done~n')
    .

write_char(-1).
write_char(C) :- put(C).
/**
 * Z   => appended list
 * Y   => atom to list
 */
read_chars(_) :-
    append([],_),
    see('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\25_prolog\\25_6\\rate.u-j.dat'),
    repeat,
    get0(C),
%    put(C),
/**
ERROR: Type error: `character' expected, found `-1' (an integer)
ERROR: In:
ERROR:    [9] put(-1)
*/
%    append(C,Z),
%
%    atom_concat(C,Z),
%    atom_codes(C,Y),
%    append(Y,Z
    write_char(C),
    C == -1,
    put('\n'),
    format("C --> -1~n"),
%    write("C ==> -1"),
    !,
    seen
    .


% ! ref
% https://stackoverflow.com/questions/10538037/prolog-transform-and-separate-term-atom-into-a-list
% "answered May 10 '12 at 18:39"
% ands((A,B)) :- !, ands(A), ands(B).
% ands(X) :- [X].

%conv_atom_to_chars(X) :-
%    [X].

/**
 * atom to list
 *
?- atol('a',Z).
a ==> [97]
Z = [97].

 */
atol(X, Y) :-
    atom_codes(X,Y),
%    format('~c ==> ~c~n', [X,Y])
    format('~a ==> ', X),
    write(Y)
    .
/**
 *
 * <result>
?- stol("char",Z).
Z = ["char"].
 */
stol(Str,[Str]).


/**
 * ref https://stackoverflow.com/questions/25633690/copy-certain-characters-from-a-list-to-another-on-prolog
 *
 * length([a,b,c,d,e],N),first_n([a,b,c,d,e], N, X).
 N is 5
 N = 5,
 X = [a, b, c, d, e].
 *
 */
first_n(List, N, Xs) :-
    write("X --> "),write(X),write("\n"),

    length(Xs, N),
    write("Xs --> "),write(Xs),write("\n"),   %=> 'Xs --> [_580,_586]'

    format('N is ~d~n', N),

    write("X --> "),write(X),write("\n"),
    write("_ --> "),write(_),write("\n"),   %=> X --> _305
                                            %_ --> _323
    append(Xs, _, List),
    write("Xs --> "),write(Xs),write("\n"),

%    append(Xs, 1, List),   %=> false
    append(Xs, _, List),
    write("Xs --> "),write(Xs),write("\n")
    .
/**
 * ref https://stackoverflow.com/questions/1911758/prolog-copying-lists
 *
?- copy([a,b,c],Z).
Z = [a, b, c].

 */
copy(L,R) :- accCp(L,R).
accCp([],[]).
accCp([H|T1],[H|T2]) :- accCp(T1,T2).


/**
 * https://stackoverflow.com/questions/20765479/create-a-sublist-from-a-list-given-an-index-and-a-number-of-elements-prolog
 * "answered Dec 24 '13 at 21:51"
 */
/**
sublist([X|Xs], 1, K, [X|Ys]) :-
    write([X|Xs]),write("\n"),
    K > 1,
    K1 is K - 1,
%    write([X|Xs]),write("\n"),
    sublist(Xs, 1, K1, Ys).
*/  %=> not working

/** => this works.
 * ref https://stackoverflow.com/questions/20765479/create-a-sublist-from-a-list-given-an-index-and-a-number-of-elements-prolog
 * 'answered Dec 25 '13 at 0:04'
 *
 * <memo>
 * 1. 'I' is determined by the program itself, setting it to the length
 * of the given list, i.e. 'List' (so I surmise).
 *
 * <result>
?- sublist2([a,b,c,d,e],1,2,Z).
Z = [a, b].
 *
 */
sublist2(List, From, Count, SubList) :-
    findall(E, (nth1(I, List, E), I >= From, I < From + Count), SubList).

/**
 * https://stackoverflow.com/questions/20765479/create-a-sublist-from-a-list-given-an-index-and-a-number-of-elements-prolog
 * "answered Dec 24 '13 at 22:11"
 *
sublist3([a,b,c,d,e],1,2,Z).
 *
 * <result>
?- sublist3([a,b,c,d,e],1,2,Z).
Z = [b, c] ;
false.
 */
sublist3( Xs , Offset , Count , Ys ) :-
  split(Xs,Offset,_,X1) ,               % extract the first 'offset' items from the lsit and toss them
  split(X1,Count,Ys,_)                  % extract the first 'count' items from the remainder to get the result.
  .

/**
 * https://stackoverflow.com/questions/20765479/create-a-sublist-from-a-list-given-an-index-and-a-number-of-elements-prolog
 * "answered Dec 24 '13 at 22:11"
 */
split( []     , 0 , []     , []     ) .  % splitting a zero-length prefix from an empty list yields a zero-length prefix and a zero length suffix.
split( [X|Xs] , 0 , []     , [X|Xs] ) .  % splitting a zero-length prefix from a non-empty list yields a zero-length prefix and the non-empty list.
split( [X|Xs] , N , [X|Ps] , Qs     ) :- % Otherwise...
  N > 0 ,                                % - if the count is positive
  N1 is N-1 ,                            % - we decrement count
  split( Xs , N1 , Ps , Qs )             % - and recurse down, prepending the head of the source list to the prefix
  .                                      % Easy!

/**
 * <result>
?- append_str2list("a",[b,c,d],Z).
Z = ["a", b, c, d].

?- append_str2list(a,[b,c,d],Z).
Z = [a, b, c, d]
 */
append_str2list(Str, Xs, [Str|Xs]).


%! append_str2list(Str,[Str]).
%

echo2 :-
    write("any message? (End with a '.') --> : "),
    read(X),
    X == end_of_file,
    write("end"),
    write(X)
    .

/**
 * ref http://www.geocities.jp/m_hiroi/prolog/prolog04.html
 *
 * <result>
?- echo.
|: end of file!
true.
 */
echo :- repeat, read(X), echo_sub(X), !.
echo_sub(X) :- X == end_of_file, write("end of file!"), !.
echo_sub(X) :- write(X), nl, fail.




