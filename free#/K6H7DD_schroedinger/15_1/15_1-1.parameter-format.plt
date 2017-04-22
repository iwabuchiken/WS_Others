#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/15_1/15_1-1.parameter-format.plt.plt"
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
# graph: 1
#
###########################
name = sprintf("14-1-1 (%02d) parameter")

set title title_session(name)

set isosamples samples_value
set samples samples_value

set parametric
set urange [0:pi]
set vrange [0:2*pi]
set isosamples 50
set pm3d depthorder
#set view 75,45
#set view 25,45
set view 25,15

set xrange [-1:1]
set yrange [-1:1]
set zrange [-1:1]
splot sin(u)*cos(v),sin(u)*sin(v),cos(u) with pm3d

############################
#
# save image
#
############################

############################
#
# animation: loop
#
############################
if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

count = count_init


