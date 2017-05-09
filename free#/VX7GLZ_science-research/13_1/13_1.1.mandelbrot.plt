#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\13_1\13_1.1.mandelbrot"
#	
#       2017/05/07 09:36:54
#
############################
#
# includes
#
############################
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/lib.plt"
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/cons.plt"


############################
#
# variables
#
############################

############################
#
# operations
#
############################
#ref http://www.gnuplot-cmd.com/plot/replot.html

#set isosamples samples_value

############################
#
# animation: setup
#
############################
if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»


############################
#
# params setup
#
############################
numof_samples = 60 + count * 10
set isosamples numof_samples

set title sprintf("Mandelbrot function (samples = %03d)", numof_samples)
#set title "Mandelbrot function"

#set isosamples 60
#set isosamples 120

compl(a,b)=a*{1,0}+b*{0,1}
mand(z,a,n) = n<=0 || abs(z)>100 ? 1:mand(z*z+a,a,n-1)+1
splot [-2:1][-1.5:1.5] mand({0,0},compl(x,y),30) 
set pm3d map
replot

replot
set palette defined (0 "white", 6 "blue", 12 "green", 18 "yellow", 24 "red", 30 "black")
replot

############################
#
# animation: loop
#
############################
wait = 0.1
count_max = 30

if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (sequece < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#if (sequence < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#count = count_init
#sequence = sequence_init


