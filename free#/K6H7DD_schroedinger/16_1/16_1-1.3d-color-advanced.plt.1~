#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/15_1/15_1-3.parameter-format.change-urange,vrange.plt"
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
#name = sprintf("14-1-1 (%02d)", sequence)
#name = sprintf("15-1-1 parameter")

#set title title_session(name)

set isosamples samples_value
set samples samples_value

set parametric

#set urange [0:pi]

diff = 3.1415 / (count_max / count_tick)

end = diff * sequence
if (end > 3.1415 * 2) end = 3.1415

#name = sprintf("15-1-1 (%02d) [0:%04f]"\
#     , sequence, end)

#set title title_session(name)

set urange [0:end]

#set vrange [0:2*pi]
set vrange [0:2 * end]

############################
#
# labels, ranges, frame setups
#
############################
#set isosamples 50
set pm3d depthorder
#set view 65,45
view_x = 110
view_y = 45
set view 110,45

##### title
name = sprintf("15-1-1 (%02d) urange=[0:%04f] (view = %d,%d)"\
     , sequence, end, view_x, view_y)

set title title_session(name)

##### axis labels
set xlabel "x"
set ylabel "y"

set xrange [-1:1]
set yrange [-1:1]
set zrange [-1:1]

splot sin(u)*cos(v),sin(u)*sin(v),cos(u) with pm3d

############################
#
# save image
#
############################


#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
set terminal gif

time_label = "20170422_160332"

#system "mkdir "."image2_".time_label

set output sprintf("image_%s/15_1-1.%s.%002d.gif", time_label, time_label, sequence)


############################
#
# animation: loop
#
############################
if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

count = count_init


