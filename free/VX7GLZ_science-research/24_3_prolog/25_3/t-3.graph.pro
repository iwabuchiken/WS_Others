edge(1,2).
edge(1,3).
edge(1,4).

edge(2,3).
edge(2,5).

edge(3,4).
edge(3,5).

edge(4,5).

%! edge(X,Y) :- edge(Y,X).

%! connected(X,Y) :- edge(X,Y).
connected(X,Y) :- edge(X,Y) ; edge(Y,X).

%! ===============================] SEG-1
p(1,3,5).
p(2,4,1).
p(3,5,2).
p(4,3,1).
p(5,2,4).

consult("libs.20170523_134432.pro").

%! ===============================] EXPERI-2
%! dependency : C:/WORKS_2/WS/WS_Others/free/VX7GLZ_science-research/24_3_prolog/libs.20170523_134432.pro
%! <Usage>
%! - Open this file with SWI-Prolog.
%! - Execute "['LIBS-FULL-PATH']"
%! - Execute "sumofbag(Sum)."
%! 
sumofbag(Sum) :-
%!   findall(Z,p(X,Y,Z),Bag),
   findall(Z,p(_,_,Z),Bag),
   format('~a~n',Bag),
   write(Bag),write("\n"),
   sum(Bag,Sum).

