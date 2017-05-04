#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\5_1\5_1-2.contour.plt"
#	
#       2017/04/25 12:13:53
#
#      ref: 
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
#if (exist("level") == 0 || level < -0.5) level = -0.5 #•Ï”‚Ì‰Šú‰»
if (exist("level") == 0 || level < 0) level = 0 #•Ï”‚Ì‰Šú‰»

############################
#
# graph: 1
#
###########################


############################
#
# params setup
#
############################


########## grid ##########


########## plot ##########
########## range ##########

########## plot: 2 ###########
#set xrange [-5 : 5]
#set yrange [-5 : 5]

#set ticslevel 0
#level = count

#set ticslevel level

#sample_level = 30 + count * 10
#set isosample sample_level

call "5_1-2.contour.A.plt"

#ref exit http://gnuplot.sourceforge.net/docs_4.2/node81.html
exit

########################################################

view_X = count * 10
view_Y = count * 10
set view view_X, view_Y

#set title sprintf(" ticslevel = %d", level)
set title sprintf(" ticslevel = %f / sample = %d / view = (%d %d)", \
     level, sample_level, view_X, view_Y)

#splot (x**2)*(y**2)

#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
set terminal gif

time_label = "20170428_140138"

set output sprintf("images_%s/5_1-2.countour.%s.%02d.gif", time_label, time_label, sequence)

splot (x**2)*(y**2)

count = count + 1

#if(count < 10) pause 1; level = level + 0.1; reread
#if(count < 10) pause 2; level = level + 0.1; sequence = sequence + 1; reread
if(count < 10)  level = level + 0.1; sequence = sequence + 1; reread

count=0


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
#if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (sequece < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#if (sequence < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#count = count_init
#sequence = sequence_init


