sines(0,_).
sines(Start,Tick) :-
%!    Start >= 0,
    X is sin(Start),
%!    format("Start = ~5f / X = ~5f / ", [Start,X]),
    format('sin(~5f) is ~5f~n', [Start, X]),
    Y is Start - Tick,
    sines(Y,Tick)
    .

sines_to_file_then(Start,_, Handle) :-
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
%    format(Handle, 'sin(~5f) = ~5f~n', [Start, X]),
%    format(Handle, '~5f~t~5f~n', [Start, X]),
    format(Handle, '~5f\t~5f~n', [Start, X]),
    save_sines(Start - Tick, Tick, Handle)
    .

save_sines_then_2(Start,End,Tick,Handle) :-
    X is sin(Start),
%    format('sin(~5f) = ~5f~n', [Start, X]),
%    format(Handle, 'sin(~5f) = ~5f~n', [Start, X]),
%    format(Handle, '~5f~t~5f~n', [Start, X]),
    format(Handle, '~5f\t~5f~n', [Start, X]),
    save_sines_2(Start - Tick, End,Tick, Handle)
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

save_sines_2(Start, End, Tick, Handle) :-
    (   Start >= End
    ->  save_sines_then_2(Start,End,Tick,Handle)
    ;   save_sines_else
    )
    .


save_sines_exec(Start,Tick,Fpath) :-
    open(Fpath, append, Handle),
%    write(Handle,"sines\n"),
    save_sines(Start,Tick,Handle),
    close(Handle),
    write("done"),write("\n")
    .

save_sines_exec_2(Start,Tick,End,Fpath) :-
    open(Fpath, append, Handle),
%    write(Handle,"sines\n"),
    save_sines_2(Start,Tick,End,Handle),
    close(Handle),
    write("done"),write("\n")
    .

/**
 * ref http://qiita.com/1024jp/items/f0ccbab6422a6a64e130
plot_data('C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/24_3_prolog/25_4/sines.pi~-pi.(3).dat',
'C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\24_3_prolog\\25_4\\plot-data.plt').

plot_data('C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\25_prolog\\25_4\\sines.pi~-pi.(3).dat','C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\25_prolog\\25_4\\plot-data.plt').


* *
 */
plot_data(DataFilepath, SourceFilePath) :-
%    format(atom(CommandString),'~a',"C:\\WORKS_2\\Programs\\gnuplot_4.6.7\\bin\\gnuplot.exe"),
%
    format(atom(CommandString),'~a',"C:\\WORKS_2\\Programs\\gnuplot_4.6.7\\bin\\wgnuplot.exe"),
    format(atom(ParamsString),' -e \"fpath=\'~a\'\"',DataFilepath),
%    format(atom(SourceFilePath), '~a', SourceFilePath),
    format(atom(ShellString),
           '~a ~a ~a',

           [CommandString, ParamsString, SourceFilePath
%           '~a ~a ~a~n',
%            [CommandString, ParamsString, SourceFilePath


           ]),
    write(ShellString),
    write("shell executing...\n"),
    shell(ShellString),
    write("shell => done")
%    shell(E),

%    name(Fpath, FpathString),
%    name('C:/WORKS_2/Programs/gnuplot_4.6.7/bin/gnuplot',
%    CommandPathString),
%    format(atom(Params), ' -e "fpath=\'~a\'"', Fpath),
%    name(Params, ParamsString),
%    append(CommandPathString, ParamsString, EDIT),
%    name(E,EDIT),
%    format('~a~n',E)
%    shell(E),
%    format("shell => done~n")

%    name(Fpath, FpathString),
%    name( '\"C:/Program Files (x86)/sakura/sakura.exe\" ',
%    EditorPathString),
%    append(FpathString, EditorPathString,EDIT),
%    name(E, EDIT),
%    format('string => ~a~n',E)
    .

