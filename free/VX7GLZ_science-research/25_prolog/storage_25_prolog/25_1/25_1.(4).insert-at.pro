insert_at(1, X, Ls, [X | Ls]).
insert_at(N, X, [Y | Ls], [Y | Zs]) :-
    N > 1, N1 is N - 1, insert_at(N1, X, Ls, Zs).
