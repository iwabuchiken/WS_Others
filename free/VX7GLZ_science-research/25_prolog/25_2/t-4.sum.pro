sum([X|Ls],Z) :-
   Z1 is Z + X,
   format('X is ~d / Z is ~d / Z1 is ~d~n', [X, Z, Z1]),
   sum(Ls, Z1).
%!    sum(Ls, Z1),
%!    Z is Z1.
