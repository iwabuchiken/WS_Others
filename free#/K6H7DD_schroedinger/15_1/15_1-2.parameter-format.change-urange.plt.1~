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
#name = sprintf("14-1-1 (%02d)", sequence)
#name = sprintf("15-1-1 parameter")

#set title title_session(name)

set isosamples samples_value
set samples samples_value

set parametric
set urange [0:pi]

#set vrange [0:2*pi]
#set vrange [0:1 * pi]

#diff = pi / (count_max * count_tick)
#diff = 3.1415 / (count_max * count_tick)
diff = 3.1415 / (count_max / count_tick)

#name = sprintf("15-1-1 (%02d) (pi = %04f / diff = %04f / diff * sequence = %04f) "\
#name = sprintf("15-1-1 (%02d) (pi = %04f / diff = %04f / diff * sequence = %04f) " \
#     , pi\
#     , sequence, diff, (diff * sequence))
#name = sprintf("15-1-1 (%s)", diff)

#name = sprintf("15-1-1 (%02d) diff = %04f", sequence, diff)
#name = sprintf("15-1-1 (%02d) diff = %04f diff * sequence = %04f"\
#     , sequence\
#     , diff\
#     , diff * sequence)
#     , sequence, diff)

name = sprintf("15-1-1 (%02d) [0:%04f]"\
     , sequence, diff * sequence)

set title title_session(name)

#set title name
#set title "15-1-1"

#set vrange [0: diff * sequence]

#set vrange [0: diff * sequence]

end = diff * sequence * 2
if (end > 3.1415 * 2) end = 3.1415 * 2

set vrange [0: end]
#set vrange [0: diff * sequence * 2]
#set vrange [0: 0.5 * pi]

set isosamples 50
set pm3d depthorder
set view 65,45
#set view 75,45
#set view 25,45
#set view 25,15
#set view 85 - sequence, 45
#set view 75, 45 - sequence / 2
#set view 75, 45 - sequence
#set view 75, abs(45 - sequence)

set xlabel "x"
set ylabel "y"

set xrange [-1:1]
set yrange [-1:1]
set zrange [-1:1]

splot sin(u)*cos(v),sin(u)*sin(v),cos(u) with pm3d
#splot sin(u)*cos(v),sin(u)*sin(v),cos(v) with pm3d
#splot sin(u)*cos(v),sin(u)*sin(v), sin(u) with pm3d
#splot sin(u)*cos(v),sin(u)*sin(v), cos(u)**2 with pm3d

############################
#
# save image
#
############################


#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
set terminal gif

time_label = "20170422_153748"

#system "mkdir "."image2_".time_label

set output sprintf("image_%s/15_1-1.%s.%002d.gif", time_label, time_label, sequence)


############################
#
# animation: loop
#
############################
if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

count = count_init


