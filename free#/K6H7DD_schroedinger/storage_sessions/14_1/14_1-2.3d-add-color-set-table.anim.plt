#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/14_1/14_1-2.3d-add-color-set-table.plt"
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
name = sprintf("14-1-2 (%02d)", sequence)

set title title_session(name)

set xlabel "x"
set ylabel "y"

a = 3

set xrange [-a*pi:a*pi]
set yrange [-a*pi:a*pi]

set isosamples samples_value
set samples samples_value

set grid lw 1

set table "table.dat"
splot sin(x)*sin(y)
unset table

#splot "table.dat" using 1:2:3:(sin($1+$2*2)) with pm3d
#splot "table.dat" using 1:2:(sin($1 + count * 3)):(sin($1+$2*2)) with pm3d
#splot "table.dat" using 1:2:(exp(sin($1 + count * 3))):(sin($1+$2*2)) with pm3d
#splot "table.dat" using 1:2:(exp(sin($1 + count * 3))):($3) with pm3d
#splot "table.dat" using 1:2:(exp(sin($1 + count * 3))):(exp(sin($1 + count * 3))) with pm3d   #=> y axis --> no change
#splot "table.dat" using 1:2:(exp(sin($1 + count * 3)) + exp(sin($2 + count * 3))):(exp(sin($1 + count * 3))) with pm3d   #=> 
#splot "table.dat" using 1:2:(exp(sin($1 + count * 3)) + exp(sin($2 + count * 3))):(exp(sin($1 + count * 3)) + exp(sin($2 + count * 3))) with pm3d   #=> 
#splot "table.dat" using 1:2:(exp(sin($1 + count * 3)) + exp(sin($2 + count * 3))):(exp(sin($1 + count * 3)) + exp(sin($2 + count * 3))) with pm3d   #=> 
splot "table.dat" \
     using 1:2\
          :(exp(sin($1 + count * 3)**3) + exp(sin($2 + count * 3)**3))\
          :(exp(sin($1 + count * 3)**3) + exp(sin($2 + count * 3)**3)) \
          with pm3d   #=> 


############################
#
# save image
#
############################
set terminal gif

time_label = "20170421_153427"

set output sprintf("image_%s/14_1-2.%s.%002d.gif", time_label, time_label, sequence)


############################
#
# animation: loop
#
############################
#if (count < count_max) pause wait;  count = count + count_tick; reread
if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (count < count_max) pause wait;  count = count + count_tick, sequence = sequence + 1; reread   #=> animation doesn't start

count = count_init


