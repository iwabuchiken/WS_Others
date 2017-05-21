fact(0, 1).
fact(X, Sum) :-
%	X > 0, Sum is X.
%	X > 0, X1 is X - 1, Sum is X * X1.
	X > 0, X1 is X - 1, fact(X1, Sum1), Sum is X * Sum1.
