write_data(end_of_file). %! ===============] write_data
write_data(X) :- format('~a.~n', X).

read_data(X) :- %! ===============] read__data
    see(X),   %! ;;; open(X,"r")
              %! ;;; ==> tell(X) : open(..., "w")
    repeat,   %! ;;; unless (...
    read(Y),
    write("file read : "),write(Y),write("\n"),
    write_data(Y),
    Y == end_of_file, %! ;;; );unless
    !,
    seen.     %! ;;; close(file) ===> told

write_elements([],[]) :- %! ===============] write_elements
   write("reached [][]"),write("\n").
write_elements([X|Xs],Z) :-
   format("elem is '~a'~n", X),
   write_elements(Xs,Z),
   append(X,[Z],Ys),
   write("Z is "),write(Z),write("\n").

%! ==============================] write_to_file
write_to_file(X) :-
   tell(X),
   write_data("abcdefg"),
   told,
   format("file written~n").

%! ==============================] copy_data(X,Y)
copy_data(X,Y) :-
   see(X),
   tell(Y),
   repeat,
   read(Z),
   write_data(Z),
   Z == end_of_file,
   !,
   seen,
   told,
   format("all done~n").

%! if the source file is being open, the error:
%! ERROR: t-2.file-io.pro:1:
%!         Illegal argument to format sequence ~a: write_data(end_of_file)
%!         In:
%!           [10] format('~a.~n',write_data(end_of_file))
%!            [8] copy_data('t-2.file-io.pro','t-2.file-io.pro.copy') at c:/works_2/ws/ws_others/free/vx7glz_science-research/24_3_prolog/25_2/t-2.file-io.pro:36
%!            [7] <user>
%!         
%!         Note: some frames are missing due to last-call optimization.
%!         Re-run your program in debug mode (:- debug.) to get more detail.



%! ==============================] EOF
