sines(0,_).
sines(Start,Tick) :-
%!    Start >= 0,
    X is sin(Start),
%!    format("Start = ~5f / X = ~5f / ", [Start,X]),
    format('sin(~5f) is ~5f~n', [Start, X]),
    Y is Start - Tick,
    sines(Y,Tick)
    .

sines_to_file_then(Start,Tick, Handle) :-
%    Start >= 0,
    X is sin(Start),

    %! ref http://www.swi-prolog.org/pldoc/doc_for?object=format/3
    format(Handle, 'sin(~5f) is ~5f~n', [Start, X])
%    told,
%    Y is Start - Tick,
%    sines(Y,Tick)
    .

sines_to_file(0,_,_).
sines_to_file(Start,Tick, Handle) :-
%    Start >= 0,
    X is sin(Start),
%!    format("Start = ~5f / X = ~5f / ", [Start,X]),


    %! ref http://www.swi-prolog.org/pldoc/doc_for?object=format/3
    format(Handle, 'sin(~5f) is ~5f~n', [Start, X]),
%    told,
    Y is Start - Tick,
    sines_to_file(Y,Tick,Handle)
%    sines(Y,Tick)
    .

%!  ==================================]
% ref append to file
% https://stackoverflow.com/questions/6455531/prolog-adding-text-to-the-end-of-a-file
% "answered Jun 23 '11 at 15:12"
%
sines_to_file_exec(Start,Tick,Fpath) :-
%    Start >= 0,
    open(Fpath, append, Handle),
    sines_to_file(Start,Tick,Handle),
    close(Handle),
    write("done"),write("\n")
    .

then(X) :-
    write("Variable is "),
    write(X).

else(X) :-
    write("Variable is "),
    write(X).

ifthenelse(X,Y,Z) :-
    (   X =< Y
    ->  then(X)
    ;   else(Z)
%    ->  write(Z)
%    ;   write(X)
    )
    .

% ! ref
% https://stackoverflow.com/questions/22885622/how-can-i-simulate-a-while-loop-in-prolog-with-unchangeable-conditions
% "Prolog code:"
%  prolog_while(0) :- !.
prolog_while(0, _) :- !.
prolog_while(N, A) :-
   N1 is N -1,
   A1 is A + 1,
   prolog_while(N1, A1).


%!  ==========================]
ite_then(X) :-
%    write(X)
    format('X is ~d~n', X),
    ite(X - 1)
    .

ite_else :-
    write("less than 0")
    .

ite(X) :-
    (   X >= 0
    ->  ite_then(X)
    ;   ite_else
    )
    .

%!  ==========================]
save_sines_then(Start,Tick,Handle) :-
    X is sin(Start),
%    format('sin(~5f) = ~5f~n', [Start, X]),
    format(Handle, 'sin(~5f) = ~5f~n', [Start, X]),
    save_sines(Start - Tick, Tick, Handle)
    .

save_sines_else :-
    write("Start is less than 0"),
    write("\n"),
    !
    .

save_sines(Start, Tick, Handle) :-
    (   Start >= 0
    ->  save_sines_then(Start,Tick,Handle)
    ;   save_sines_else
    )
    .

save_sines_exec(Start,Tick,Fpath) :-
    open(Fpath, append, Handle),
    write(Handle,"sines\n"),
    save_sines(Start,Tick,Handle),
    close(Handle),
    write("done"),write("\n")
    .

