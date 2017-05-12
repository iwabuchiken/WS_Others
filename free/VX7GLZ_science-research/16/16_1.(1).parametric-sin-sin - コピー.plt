#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\16\16_1.(1).parametric-sin-sin.plt
#	
#       2017/05/12 11:36:05
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

############################
#
# animation: setup
#
############################
if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»

if (exist("n")==0 || n<0) n=0 #•Ï”‚Ì‰Šú‰»

############################
#
# params setup
#
############################
set parametric

set xrange [-5 : 5]

set urange [-5 : 5]
set vrange [-5 : 5]

#plot sin(x), cos(x)
#plot sin(u), cos(v)
plot sin(t), cos(t)



wait = 0

#if (n < 100)  n=n+1; reread
#if (n < 200)  n=n+1; reread
#

n = 0

############################
#
# save image
#
############################


#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
#set terminal gif

time_label = "20170424_132124"

#set output sprintf("image_%s/17_1-1.%s.%002d.gif", time_label, time_label, sequence)


############################
#
# animation: loop
#
############################
#if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (sequece < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#if (sequence < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#if (n < 200)  pause wait; n=n+1; reread

#count = count_init
#sequence = sequence_init


