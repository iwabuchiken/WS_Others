%! edit(File) :-
%!    name(File,FileString),
%!    name('open -e ', 'C:/Program Files (x86)/sakura/sakura.exe'), %% Edit this line for your favorite editor
%!   name('open -e ', TextEditString), %% Edit this line for your
%   favorite editor
%!    append(TextEditString,FileString,EDIT),
%!   name(E,EDIT).
%!   shell(E).

%!==============================] test/1
% ref https://www.cpp.edu/~jrfisher/www/prolog_tutorial/2_4.html "Many prolog systems rely upon the programmer "
%
test(File) :-
    name(File,FileString),
    write("FileString => "),write(FileString),
    write("\n"),
%!    name('open -e ', 'C:/Program Files (x86)/sakura/sakura.exe ')
    name( '\"C:/Program Files (x86)/sakura/sakura.exe\" ', TextEditString),
    append(TextEditString,FileString,EDIT),
    write("EDIT => "),write(EDIT),
    write("\n"),
    name(E,EDIT),
    write("E => "),write(E),
    write("\n"),
    shell(E)
    .

