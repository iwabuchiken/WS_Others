my_length([], 0). %! ======================] my_length
my_length([X|Xs], N ) :-
        my_length(Xs, N1),
        write("X is "),write(X),write(" / "),
        write("Xs is "),write(Xs),write(" / "),
%!        format("~a", X),
        N is N1 + 1,
        write("N is "),write(N),write("\n").


        %! ?- my_length([1,2,3,4],N).
        %! X is 4 / Xs is [] / N is 1
        %! X is 3 / Xs is [4] / N is 2
        %! X is 2 / Xs is [3,4] / N is 3
        %! X is 1 / Xs is [2,3,4] / N is 4
        %! N = 4.


%! ;; my_increment(1, 1).
%! ;; my_increment(X, N) :-
%! ;;    my_increment(X - 1, N1),
%! ;;    N is N1 + 1.

my_append([],Xs,Xs). %! ======================] my_append
my_append([X|Ls], Ys, [X|Zs]) :-
%!       write("yes").
%!       my_append(Ls, Ys, Zs).
      write("> appending : "),write("X is "),write(X),
      write(" / "),write("Ls is "),write(Ls),
      write(" / "),write("Zs is "),write(Zs),write("\n"),
      my_append(Ls, Ys, Zs),
%!       my_append(Ls, Ys, Zss),
      write("> returning : "),
      write("X is "),write(X),write(" / "),
      write("Zs is "),write(Zs),write(" / "),
      write("Z is "),write([X|Ls]),write("\n").

      %! 'Zss' instead of 'Zs' then:
      %! X is c
      %! returning...
      %! Zs is _370X is b
      %! returning...
      %! Zs is _364X is a
      %! returning...
      %! Zs is _358
      %! Z = [a|_358].

      %! 'Zs' instead of 'Zss' then:
      %! X is c
      %! returning...
      %! Zs is [d,e,f]X is b
      %! returning...
      %! Zs is [c,d,e,f]X is a
      %! returning...
      %! Zs is [b,c,d,e,f]
      %! Z = [a, b, c, d, e, f].

my_reverse([],[]):-  %! ======================] my_reverse
   write("> reached! : [],[]"),write("\n").
my_reverse([X|Xs], Ys) :-
   write("> Reverseing : "),
   write("X is "),write(X),write(" / "),
   write("Xs is "),write(Xs),write(" / "),
   write("Ys is "),write(Ys),write("\n"),

   my_reverse(Xs,Zs),
   write("======================\n"),
   write("> Returning : "),
   write("\n"),
%!    write("Xs is "),write(Xs),write(" / "),
%!    write("Zs is "),write(Zs),write("\n"),

%!    write("======================\n"),
   write("> Appending : "),
   write("Zs Is "),write(Zs),write(" / "),
   write("X Is "),write(X),write(" / "),
   write("Ys is "),write(Ys),write("\n"),
   append(Zs,[X],Ys),

%!    write("======================\n"),
   write("> Appended : "),
   write("Zs Is "),write(Zs),write(" / "),
   write("X Is "),write(X),write(" / "),
   write("Ys is "),write(Ys),write("\n").


 %! ====================== EOF 
