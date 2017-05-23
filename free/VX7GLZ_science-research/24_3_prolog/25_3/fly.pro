%! fly(taro).

fly(X) :- airplane(X).
fly(X) :- superperson(X).

airplane(jet_plane).
airplane(helicopter).

superperson(taro).

%! fact(X) :- true.
fact(_) :- true.
