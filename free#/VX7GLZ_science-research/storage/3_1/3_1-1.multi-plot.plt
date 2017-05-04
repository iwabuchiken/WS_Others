#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\3_1\3_1-1.multi-plot.plt"
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
if (exist("count") == 0 || count < 0) count = count_init #�ϐ��̏�����

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #�ϐ��̏�����

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
set xrange [0:5]
set yrange [-1:1]

set multiplot layout 3,1  #multiplot�̊J�n�A�c3��1�����z�u

plot cos(5.0*x)*exp(-x) title "plot 1"

plot cos(5.0*(x-0.2))*exp(-x) title "plot 2"

plot cos(5.0*(x-0.4))*exp(-x) title "plot 3"

unset multiplot           #multiplot�̏I��

#terminal��output�̕ύX�i1��̂݁j
if (exist("TERM")==0 || TERM eq "Default") \
     pause -1 "click OK to make PS file";\
     TERM = "PS";\
     set out "multiplot_01.eps";\
     set term postscript color "Arial" 15 enhanced portrait size 7in,10in;\
     reread

#terminal��output�̃��Z�b�g
TERM = "Default"
set out
set term pop




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


