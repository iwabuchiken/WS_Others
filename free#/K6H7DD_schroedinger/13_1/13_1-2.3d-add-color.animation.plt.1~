#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/13_1/13_1-1.3d-add-color.plt"
#	
#	2017/04/20 12:04:19
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

set isosamples samples_value


############################
#
# graph: 1
#
############################
set title title_session("13-1 3d surface color")
#set title title_session("sin(x)*sin(y)")

set xlabel "x"
set ylabel "y"

a = 2

set xrange [-a*pi:a*pi]
set yrange [-a*pi:a*pi]

set grid lw 1

splot sin(x)*sin(y) with pm3d

############################
#
# graph: 2
#
############################

#set title title_session("sin(x)^2*sin(y)")

#replot (sin(x))**2*sin(y) with pm3d
#splot (sin(x))**2*sin(y) with pm3d

