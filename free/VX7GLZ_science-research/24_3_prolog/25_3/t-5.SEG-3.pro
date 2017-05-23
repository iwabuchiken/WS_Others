factorial(0,1).

factorial(N,F) :-
   N>0,
   N1 is N-1,
   factorial(N1,F1),
   F is N * F1.


%! ========================
factorial(0,F,F).

factorial(N,A,F) :-
    N > 0,
    A1 is N*A,
    N1 is N -1,
    factorial(N1,A1,F).

%! =========================
countdown(X,Y) :-
   X >= 0,
   format('X is ~d', X),
   factorial(X,F),
   format(' / factorial is ~d~n', F),
   countdown(X-1,Y).

%! =========================]
countup(X,Y) :-
   X =< Y,
   format('X is ~d', X),
   factorial(X,F),
   factorial(X,X,F2),
   format(' / fact is ~d / f2 is ~d~n', [F,F2]),
   countup(X+1,Y).

%! =========================]
countup(X,Y,Z) :-
   X =< Y,
   format('X is ~d', X),
   factorial(X,F),
   factorial(X,X,F2),
   format(' / fact is ~d / f2 is ~d~n', [F,F2]),
%!   write("Z is "),write(Z),write("\n"),
   write("Z is "),write([F2|Z]),write("\n"),
   countup(X+1,Y,[F2|Z])
%!   write("Z is "),write([F2|Z]),write("\n")
   .

%! =========================]
% error => 'Undefined procedure: man/1'
program :-
    open('file.txt',write, Stream),
    (   man(Man), write(Stream, Man), fail
    ;   true
    ),
    close(Stream).

