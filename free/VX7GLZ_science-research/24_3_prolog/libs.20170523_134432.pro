sum([],0).
sum([X|Xs],Sum) :-
   sum(Xs,Sum1), Sum is X + Sum1.
