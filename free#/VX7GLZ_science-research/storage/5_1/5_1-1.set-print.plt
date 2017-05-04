#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\3_1\5_1-1.set-print.plt"
#	
#       2017/04/25 12:13:53
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


############################
#
# params setup
#
############################


########## grid ##########


########## plot ##########
########## range ##########
a = 3
set xrange [0:5 * pi]

set yrange [-2 : 2]

set trange [0:5 * pi]

########## grid ##########
set grid lw 1

########## multi plot ##########

########## plot ##############################
#DATA = "Lorenz_Attractor.data"
DATA = "Lorenz_Attractor-2.data"

#ref append http://stackoverflow.com/questions/13196592/how-to-add-data-from-gnuplot-to-an-existing-file-without-overwiting-the-contents
set print DATA append
#set print DATA

print "count => ", count
#print "count => ", count
#print "count", count

count = count + 1

if(count < 10) reread

count=0

#tablefile="table3.dat"
#set table tablefile
#splot 0
#unset table

########## plot: 2 ###########
set xrange [-5 : 5]
set yrange [-5 : 5]

#set ticslevel 0
level = 10
set ticslevel level

set title sprintf(" ticslevel = %d", level)

splot (x**2)*(y**2)

#if (sequece < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread


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


