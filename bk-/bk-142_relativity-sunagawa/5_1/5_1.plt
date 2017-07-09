set xrange [0:pi]
set yrange [0:2*pi]

set samples 100
set isosamples 100
set pm3d depthorder

set table "table2.dat"
splot 0
unset table

set xrange [-1:1]
set yrange [-1:1]
set zrange [-1:1]

#splot "table2.dat" using (sin($1)*cos($2)):(sin($1)*sin($2)):(cos($1)):(sin($2*2)) with pm3d
#splot "table2.dat" using (cos($1)*cos($2)):(sin($1)*sin($2)):(cos($1)):(sin($2*2)) with pm3d
#splot "table2.dat" using ($1)**2 : ($2)**2 : ($1)**2 + ($2)**2 with pm3d
#splot "table2.dat" using sqrt(1 - ($2)**2) : ($2)**2 : ($1)**2 + ($2)**2 with pm3d
f1(x) = sqrt(x)
#splot "table2.dat" using (sqrt(1 - ($2)**2)) : (sqrt(1 - ($1)**2)) : ($1)**2 + ($2)**2 with pm3d #=> w.
#splot "table2.dat" using (f1($2)) : ($2)**2 : ($1)**2 + ($2)**2 with pm3d #=> w.
#splot "table2.dat" using f1(($2)) : (($2))**2 : ($1)**2 + ($2)**2 with pm3d #=> n.w.
#splot "table2.dat" using sqrt($1)*cos($2) : (sin($1)*sin($2)):(cos($1)):(sin($2*2)) with pm3d

splot "table2.dat" using (sin($1)) : (cos($2)) : (sin($1) * cos($2)) with pm3d
