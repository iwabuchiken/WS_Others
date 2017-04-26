#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\3_1\3_1-2.multi-plot.sin-cos.plt"
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
if (exist("count") == 0 || count < 0) count = count_init #変数の初期化

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #変数の初期化

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
set xrange [-a * pi : a * pi]
set yrange [-2 : 2]
#set xrange [0:5]
#set xrange [0:5]
#set yrange [-1:1]

########## grid ##########
set grid lw 1

########## multi plot ##########
#set multiplot layout 3,1  #multiplotの開始、縦3横1自動配置
set multiplot layout ,1  #multiplotの開始、縦3横1自動配置

########## plot ##########
#plot cos(x) title "plot 1"
plot cos(x)  lc "red"
plot sin(x)  lc "blue"


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


