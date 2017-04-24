#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/14_1/14_1-1.3d-add-color-++.plt"
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
if (exist("count") == 0 || count < 0) count = count_init #�ϐ��̏�����

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #�ϐ��̏�����

############################
#
# graph: 1
#
###########################
name = sprintf("14-1-1 (%02d)", sequence)

set title title_session(name)

set xlabel "x"
set ylabel "y"

a = 3

set xrange [-a*pi:a*pi]
set yrange [-a*pi:a*pi]

set isosamples samples_value
set samples samples_value

set grid lw 1

#splot "++" using 1:2:(sin($1)*sin($2)):(sin($1+$2*2)) with pm3d
#splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(sin($1+$2*2)) with pm3d
#splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(cos($1+$2*2)) with pm3d

splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(sin($1 + count * 3)*sin($2 + count * 3)) with pm3d

#value = $1 + $2

#if (value > 200) value = ($1 + $2) % 200

#splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(($1 + $2) % 200) with pm3d
#splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(sin($1)) with pm3d
#splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(sin($2)) with pm3d
#splot "++" using 1:2:(sin($1 + count * 3)*sin($2 + count * 3)):(sin($2)) with pm3d

#splot (sin(x + count * 5)) * cos(y + count * 5) with pm3d


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
#if (count < count_max) pause wait;  count = count + count_tick; reread
if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (count < count_max) pause wait;  count = count + count_tick, sequence = sequence + 1; reread   #=> animation doesn't start

count = count_init


