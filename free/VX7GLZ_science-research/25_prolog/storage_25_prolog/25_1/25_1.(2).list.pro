first([X | Ys], X).
rest([X | Ys], Ys).

add_to_list(X, Ls, [X | Ls]).
