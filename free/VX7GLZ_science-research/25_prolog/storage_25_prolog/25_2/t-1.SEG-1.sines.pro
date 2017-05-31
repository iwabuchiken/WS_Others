sines(Start,Tick) :-
    X is sin(Start),
    format('sin(~5f) is ~5f~n', [Start, X]),
    Y is X - Tick,
    sines(Y,Tick)
    .

