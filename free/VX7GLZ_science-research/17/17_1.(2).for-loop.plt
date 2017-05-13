set samples 1024

set grid lw 2

set xrange [-4*pi : 4*pi]
set yrange [-2 : 2]

#unset key

#plot for [i=1:5] sin(x*i); pause 0.1
plot for [i=1:5] sin(x*i)*exp(-i)

