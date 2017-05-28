%! ===========================] write_code(-1)
write_code(-1).
write_code(C) :- put(C).

type_file(X) :-
    see(X),
    repeat,
    get0(C),
    write_code(C),
    C == -1,
    !,
    seen.



%! ******************************] EOF
