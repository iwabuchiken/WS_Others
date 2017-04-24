set xrange [-1*pi:1*pi]
set yrange [-1*pi:1*pi]

#set isosamples 50
set isosamples 100

splot sin(x)*sin(y) with pm3d

